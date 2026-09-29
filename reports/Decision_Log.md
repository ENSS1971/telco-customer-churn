# Registro de Decisões Técnicas (Decision Log) — Churn Prediction

## 1. Visão Geral e Objetivo
Este documento formaliza as decisões de arquitetura, engenharia de atributos, seleção de algoritmos e métricas aplicadas no projeto de previsão de cancelamento de clientes (*Churn*) para telecomunicações.

---

## 2. Engenharia e Pré-Processamento de Dados
* **Tratamento de Categóricas:** Aplicação de *One-Hot Encoding* (`pd.get_dummies(drop_first=True)`) para preservar a independência linear dos modelos estatísticos.
* **Normalização:** Utilização do `StandardScaler` encadeado em `Pipeline` do Scikit-Learn para evitar vazamento de dados (*data leakage*) entre treino e teste.
* **Estratificação:** Divisão de treino (80%) e teste (20%) com amostragem estratificada (`stratify=y`) para manter a proporção da classe minoritária (`Churn = 1`).

---

## 3. Racional de Escolha das Métricas de Avaliação
No contexto de telecomunicações:
* **Custo do Falso Negativo (FN):** Perder o ciclo de vida completo do cliente (*Lifetime Value*).
* **Custo do Falso Positivo (FP):** Enviar uma oferta preventiva ou desconto a um cliente leal.

Dado o desbalanceamento das classes (~26.5% de Churn), a **Acurácia foi descartada como métrica principal**. Definiram-se como métricas prioritárias:
1. **Recall (Sensibilidade):** Maximizar a captura de clientes mrsco real.
2. **F1-Score:** Garantir um equilíbrio sustentável com a Precisão.
3. **AUC-ROC:** Avaliar a capacidade geral de ordenação de risco do modelo.

---

## 4. Comparativo de Desempenho dos Modelos

| Algoritmo | AUC-ROC | F1-Score (Churn) | Recall (Churn) | Precisão (Churn) | Acurácia Geral |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Regressão Logística (Limiar 0.44)** | **0,6274** | **0,5540** | **78,79%** | 42,72% | 55,43% |
| **Random Forest Otimizado** | 0,6257 | 0,5397 | 72,73% | 42,91% | 56,42% |
| **Regressão Logística Base** | 0,6274 | 0,5409 | 72,12% | 43,27% | 56,99% |
| **XGBoost Classifier** | 0,6171 | 0,5328 | 68,89% | **43,44%** | 57,56% |
| **Random Forest Base** | 0,6170 | 0,4916 | 56,16% | 43,71% | **59,19%** |

---

## 5. Estratégia de Otimização de Limiar (Threshold Adjustment)
* **Problema:** A predição padrão em 0.50 com pesagem de classes gerava muitos alarmes falsos.
* **Solução:** Otimização via Curva *Precision-Recall* para encontrar o ponto d ote que maximiza a média harmônica (F1-Score).
* **Resultado:** O ajuste do limiar para **0.4360** elevou o Recall da Regressão Logística de **72,12% para 78,79%** (+6,67 p.p.), com variação negligenciável na precisão (-0,55 p.p.).

---

## 6. Interpretabilidade e Drives de Negócio (SHAP)
A análise de valores SHAP (*TreeExplainer*) revelou os principais fatores determinante no comportamento dos clientes:
1. **Tipo de Contrato:** Contratos anuais e bienais são as principais barreiras de proteção contra o cancelamento.
2. **Método de Pagamento:** Clientes que utilizam *Boleto* apresentam o maior indicador de risco de *Churn*.
3. **Faturamento Mensal:** Valores de cobrança elevados (*MonthlyCharges*) exercem pressão positiva direta no risco.