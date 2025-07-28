# Desafio de Engenharia de Dados — Coco Bambu 2025

Este repositório contém a solução completa dos Desafios 1 e 2 da vaga de Engenheiro de Dados da rede Coco Bambu. O projeto foi estruturado com foco em clareza, escalabilidade, compatibilidade com produção e boa prática de engenharia de dados em ambientes reais.

## Conceitos Fundamentais

  
- **JSON (JavaScript Object Notation)**  

  Formato leve de troca de dados baseado em texto, estruturado em pares chave-valor. É amplamente utilizado em APIs para comunicação entre sistemas distintos.

- **Requisições HTTP**  

  Mecanismo de comunicação entre cliente e servidor via API. Os principais métodos são `GET`, `POST`, `PUT`, `DELETE` e `PATCH`.

---

## Desafio 1 — Modelagem e Carga de JSON

### Objetivo

- Analisar e entender o schema de uma resposta JSON simulada da API de ERP de um restaurante.
- Modelar as entidades representadas no JSON em tabelas relacionais coerentes com operações reais de restaurantes.
- Criar e executar um pipeline ETL que transforme os dados JSON e carregue em um banco relacional.
- Tratar estruturas opcionais e aninhadas no JSON (`menuItem`, `discount`, `tenderMedia`, `serviceCharge`, `errorCode`).

### Entradas

- Arquivo: `data/ERP.json`

### Resultados

- Modelagem relacional em arquivos SQL separados por domínio funcional.
- Pipeline funcional (`src/data_loader.py`) que carrega o JSON em um banco SQLite.
- Suporte à evolução de schema: reconhecimento dinâmico de mudanças como `taxes → taxation`.
- Geração e validação de schema JSON com `src/schema_builder.py`.

---

## Desafio 2 — Ingestão Simulada e Data Lake

### Objetivo

- Simular ingestão de 5 APIs REST da rede de restaurantes.
- Armazenar os dados brutos em uma estrutura de Data Lake particionada.
- Criar uma estrutura que suporte versionamento e evolução de schema.
- Implementar scripts de coleta simulada de dados para múltiplas lojas e datas.

### Endpoints Simulados

- `/bi/getFiscalInvoice`
- `/res/getGuestChecks`
- `/org/getChargeBack`
- `/trans/getTransactions`
- `/inv/getCashManagementDetails`

### Resultados

- Script `src/simulate_data_lake.py` que simula as chamadas e grava JSONs organizados por:
  - endpoint
  - data (ano, mês, dia)
  - loja (store_id)
- Diretório `datalake/raw/` com estrutura de partições.
- Documentação da estratégia de versionamento de schema em `docs/estrategia.md`.

---

## Estrutura do Projeto

desafio-engenharia-dados-2025/

├── data/

│ ├── ERP.json

│ └── ERP_taxation.json

├── datalake/

│ └── raw/

├── database/

├── docs/

│ ├── estrategia.md    # para pensamentos, justificativas e estratégias

│ └── Diagrama_ER.drawio.png

│ └── kanban.md

├── sql/

│ ├── core/

│ ├── payments/

│ ├── discounts/

│ ├── service/

│ └── errors/

├── src/

│ ├── data_loader.py

│ ├── schema_builder.py

│ └── simulate_data_lake.py

├── requirements.txt

├── .gitignore

└── README.md


---

## Como Executar
1. Clonar o repositório

```bash

git clone https://github.com/lizmartns/desafio-engenharia-dados-2025.git

cd desafio-engenharia-dados-2025
```
2. Criar ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows
```
3. Instalar dependências
```bash
Copiar código
pip install -r requirements.txt
```
4. Executar simulação de ingestão (Desafio 2)
```bash
Copiar código
python src/simulate_data_lake.py
```
5. Validar schema JSON (Desafio 1)
```bash
Copiar código
python src/schema_builder.py
```
6. Carregar JSON no banco de dados
```bash
Copiar código
python src/data_loader.py
```
# Considerações Finais
A modelagem relacional foi baseada em entidades reais de operação de restaurante e estruturada por domínio funcional (core, pagamentos, descontos, etc.).

Os scripts foram desenvolvidos com foco em clareza, reutilização e preparo para expansão futura.

A estrutura de Data Lake é compatível com práticas modernas de ingestão em larga escala, com particionamento lógico e organização consistente.