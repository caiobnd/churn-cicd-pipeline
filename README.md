# Churn CI/CD Pipeline

Pipeline de CI/CD para modelos de Machine Learning — testes automatizados, validação de métricas e deploy controlado via GitHub Actions.

![CI/CD Pipeline](https://github.com/caiobnd/churn-cicd-pipeline/actions/workflows/ml_pipeline.yml/badge.svg)

---

## Visão Geral

Treinar um modelo é só o começo. Em produção, qualquer mudança no código pode quebrar silenciosamente o pipeline ou degradar a performance do modelo.

Este projeto automatiza todo o ciclo de validação — a cada push na `main`, o GitHub Actions executa automaticamente:

1. Instala as dependências
2. Treina o modelo
3. Valida se o modelo foi gerado corretamente
4. Valida se o Recall está acima do threshold mínimo (0.70)

Se qualquer etapa falhar, o pipeline para e o merge é bloqueado.

---

## Pipeline

```
Push na main
      ↓
Instala dependências
      ↓
Treina o modelo (train.py)
      ↓
pytest tests/
  ├── test_cleaning.py → valida o pipeline de dados
  └── test_model.py   → valida recall > 0.70
      ↓
✅ Passa → pipeline verde
❌ Falha → pipeline bloqueado
```

---

## Testes

### `test_cleaning.py`
- `test_clean` — valida que nulos foram removidos e `customerID` foi dropado
- `test_encoding` — valida que todas as colunas foram encodadas corretamente
- `test_split` — valida shape e ausência do target nas features

### `test_model.py`
- `test_model_file_exists` — valida que o `.pkl` foi gerado
- `test_model_recall` — valida que Recall > 0.70 na classe minoritária (churn)

---

## Estrutura do Projeto

```
churn-cicd-pipeline/
├── .github/
│   └── workflows/
│       └── ml_pipeline.yml    ← pipeline CI/CD
├── tests/
│   ├── conftest.py            ← fixtures compartilhadas
│   ├── test_cleaning.py
│   └── test_model.py
├── data/
│   └── .gitkeep
├── model/
│   └── .gitkeep
├── cleaning.py
├── constants.py
├── model.py
├── train.py
├── requirements.txt
└── README.md
```

---

## Como Executar Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/caiobnd/churn-cicd-pipeline.git
cd churn-cicd-pipeline
```

### 2. Configure o ambiente

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Baixe o dataset

Baixe o [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) e coloque o CSV em `data/`.

### 4. Treine o modelo

```bash
python train.py
```

### 5. Rode os testes

```bash
pytest tests/
```

---

## Workflow CI/CD

```yaml
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
```

O pipeline dispara automaticamente em qualquer push ou pull request na `main`.

---

## Tecnologias Utilizadas

- **GitHub Actions** — orquestração do pipeline CI/CD
- **pytest** — testes unitários
- **scikit-learn** — modelo e métricas de validação
- **pandas** — manipulação de dados
- **joblib** — serialização do modelo

---

## Próximos Passos

- [ ] Adicionar cobertura de testes com `pytest-cov`
- [ ] Integrar MLflow para rastrear cada run do pipeline
- [ ] Adicionar step de deploy automático após validação
- [ ] Implementar Feature Store para servir features em produção
