{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "fcc3e632-9106-4689-90cf-f2414f18aa21",
   "metadata": {},
   "source": [
    "Este script carrega o modelo serializado e executa inferências para novos registros de clientes."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "033707b9-d047-47d6-b035-80f33cb61caf",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import joblib\n",
    "import pandas as pd\n",
    "\n",
    "\n",
    "def predict_churn(\n",
    "    input_data_path=\"../data/processed/X_test.csv\",\n",
    "    model_path=\"../models/random_forest_tuned.joblib\",\n",
    "):\n",
    "    if not os.path.exists(model_path):\n",
    "        raise FileNotFoundError(\n",
    "            f\"Modelo não encontrado no caminho: {model_path}\"\n",
    "        )\n",
    "\n",
    "    model = joblib.load(model_path)\n",
    "    data = pd.read_csv(input_data_path)\n",
    "\n",
    "    probabilities = model.predict_proba(data)[:, 1]\n",
    "    predictions = model.predict(data)\n",
    "\n",
    "    results = pd.DataFrame(\n",
    "        {\"Probabilidade_Churn\": probabilities, \"Predicao_Churn\": predictions}\n",
    "    )\n",
    "\n",
    "    print(\"[Inferência] Previsões executadas com sucesso!\")\n",
    "    return results\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    df_results = predict_churn()\n",
    "    print(df_results.head(10))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "spark-project",
   "language": "python",
   "name": "spark-project"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
