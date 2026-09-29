# 📉 Telco Customer Churn Prediction & Retention Analytics

Projeto de Machine Learning de ponta a ponta para previsão e mitigação de cancelamento de clientes (*Churn*) em telecomunicações, cobrindo desde a Análise Exploratória de Dados (EDA) até a otimização de limiares de decisão, interpretação agnóstica via valores SHAP e modularização para produção.

---

## 📂 Arquitetura do Repositório

```text
.
├── data/
│   ├── processed/         # Conjuntos de dados divididos e normalizados (X_train, X_test, y_train, y_test)
│   └── telco_customer_churn.xlsx
├── models/                # Artefatos e pipelines serializados (.joblib)
├── notebooks/             # Ciclo experimental em Jupyter Notebooks
│   ├── 01_EDA_Churn.ipynb
│   ├── 02_Data_Preprocessing.ipynb
│   ├── 03_Modeling_RandomForest.ipynb
│   ├── 04_Modeling_LogisticRegression.ipynb
│   ├── 04_Modeling_LogisticRegression_Otimizado.ipynb
│   ├── 05_Modeling_XGBoost.ipynb
│   └── 06_Model_Interpretation_SHAP.ipynb
├── reports/               # Artefatos de análise visual, relatórios e documentação
│   ├── Decision_Log.md
│   ├── eda_sweetviz_report.html
│   ├── shap_bar_plot.png
│   ├── shap_beeswarm_plot.png
│   └── shap_waterfall_cliente_0.png
├── src/                   # Scripts Python modularizados
│   ├── data_preprocessing.py
│   ├── train_model.py
│   └── predict.py
├── .gitignore
├── README.md
└── requirements.txt       # Dependências e bibliotecas do projeto

---

## 📊 Comparativo de Modelos

Dado o desbalanceamento inerente ao problema (~26.5% de Churn), a Acurácia foi descartada como métrica principal. Priorizou-se o Recall (Sensibilidade) para maximizar a captura de cancelamentos reais, balanceado pelo $F_1$-Score:

|          Algoritmo              | AUC-ROC|F1-Score (Churn)|Recall (Sensibilidade)|Precisão (Churn)|Acurácia Geral|
|Regressão Logística(Limiar 0,44) | 0,6274 |      0,5540    |       78,79%         |     42,72%     |    55,43%    |
|Random Forest Otimizado          | 0,6257 |      0,5397    |       72,73%         |     42,91%     |    56,42%    |
|Regressão Logística Base         | 0,6274 |      0,5409    |       72,12%         |     43,27%     |    56,99%    |
|XGBoost Classifier               | 0,6171 |      0,5328    |       68,89%         |     43,44%     |    57,56%    |
|Random Forest Base               | 0,6170 |      0,4916    |       56,16%         |     43,71%     |    59,19%    |

---

## 🔍Principais Insights de Negócio (SHAP)

1. Retenção por Contrato: Contratos anuais e beinais atuam como os melhores fatores de proteção contra o cancelamento.
2. Método de Pagamento: Clientes em cobranã via Pagamento Boleto apresentam a maior taxa de atrito.
3. Ponto de Corte Reajustado: Reduzir o limir de decisão para 0,4360 permitiu capturar + 6,67% de cancelamentos reais sem comprometer o volume de alarmes falsos.

---

## ⚙️ Como Executar o Projeto

1. Clonar o repositório e instalar dependências

git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
cd SEU_REPOSITORIO
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt

2. Executar a pipeline via scripts src/

# Processar os dados brutos
python src/data_preprocessing.py

# Treinar o modelo
python src/train_model.py

# Executar inferências em novos dados
python src/predict.py

---

##🔧 Ferramentas Utilizadas
pandas>=2.0.0
numpy>=1.24.0
scikit-learn>=1.2.0
xgboost>=1.7.0
shap>=0.41.0
matplotlib>=3.7.0
seaborn>=0.12.0
joblib>=1.2.0
openpyxl>=3.1.0
streamlit>=1.22.0


 
