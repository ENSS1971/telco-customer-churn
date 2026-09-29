{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c15941b3-c390-49e5-a8c0-6f766eae7afc",
   "metadata": {},
   "source": [
    "Este script treina o modelo campeão de Random Forest Otimizado com os hiperparâmetros ajustados e serializa o artefato em models/."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0e959882-8867-4585-a79a-22d490939860",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import joblib\n",
    "import pandas as pd\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "\n",
    "\n",
    "def train_model(data_dir=\"../data/processed\", model_dir=\"../models\"):\n",
    "    print(\"[Treinamento] Carregando dados de treino...\")\n",
    "    X_train = pd.read_csv(os.path.join(data_dir, \"X_train.csv\"))\n",
    "    y_train = pd.read_csv(os.path.join(data_dir, \"y_train.csv\")).squeeze()\n",
    "\n",
    "    print(\"[Treinamento] Treinando o Random Forest Otimizado...\")\n",
    "    rf_model = RandomForestClassifier(\n",
    "        n_estimators=100,\n",
    "        min_samples_split=5,\n",
    "        min_samples_leaf=4,\n",
    "        max_features=\"sqrt\",\n",
    "        max_depth=5,\n",
    "        class_weight=\"balanced_subsample\",\n",
    "        random_state=42,\n",
    "    )\n",
    "\n",
    "    rf_model.fit(X_train, y_train)\n",
    "\n",
    "    os.makedirs(model_dir, exist_ok=True)\n",
    "    model_path = os.path.join(model_dir, \"random_forest_tuned.joblib\")\n",
    "    joblib.dump(rf_model, model_path)\n",
    "\n",
    "    print(f\"[Treinamento] Modelo treinado e salvo em '{model_path}'!\")\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    train_model()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
