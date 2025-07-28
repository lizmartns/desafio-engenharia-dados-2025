# Estratégia Técnica — Desafios 1 e 2 (Coco Bambu 2025)

Este documento descreve as abordagens, decisões técnicas e justificativas adotadas para a execução dos dois desafios.

---

## Desafio 1 — Modelagem, Transformação e Carga de JSON

### Estrutura do JSON

O arquivo `ERP.json` representa uma transação de venda com os seguintes níveis:

- `guestChecks[]`
  - `detailLines[]`
    - `menuItem`
  - `taxes`

### Abordagem adotada

- **Análise do schema JSON:** realizada com `genson` e `jsonschema`, armazenado em `schema/erp_schema.json`.
- **Modelagem relacional:** separada por domínio funcional, com chaves primárias e estrangeiras bem definidas, normalização adequada e foco em integridade.
- **Carga em banco de dados SQLite:** com `pandas` e `sqlalchemy`, suportando múltiplas tabelas, inclusive campos opcionais.
- **Evolução de schema (`taxes → taxation`):** detectada e tratada dinamicamente no código.

---

## Desafio 2 — Ingestão de APIs e Armazenamento em Data Lake

### Por que armazenar as respostas das APIs?

- Preserva o histórico para reprocessamento e auditoria
- Permite rastreabilidade e debugging
- Suporta versionamento e evolução de schema
- Reduz dependência de disponibilidade em tempo real

### Estrutura do Data Lake

Os dados são armazenados conforme:

datalake/raw/<endpoint>/year=YYYY/month=MM/day=DD/store_id=XXX/response.json


### Organização e coleta

- Script `simulate_data_lake.py` cria a estrutura acima e salva JSONs simulados.
- Cada endpoint é salvo de forma isolada, com separação lógica e temporal.

### Tratamento de evolução de schema

O campo `guestChecks.taxes` foi renomeado para `guestChecks.taxation`. O pipeline foi adaptado com:

```python
taxes_field = guest_check.get("taxes") or guest_check.get("taxation") or []
Garantindo:

Compatibilidade com múltiplas versões de JSON

Robustez contra alterações da API