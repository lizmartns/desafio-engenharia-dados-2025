# schema_builder.py

import json
import os
from genson import SchemaBuilder
from jsonschema import validate, ValidationError

# --- Caminho do JSON de entrada
JSON_INPUT_PATH = "./data/ERP.json"
SCHEMA_OUTPUT_PATH = "./schema/erp_schema.json"

# --- Leitura do JSON
with open(JSON_INPUT_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

# --- Construção do schema
builder = SchemaBuilder()
builder.add_object(data)
json_schema = builder.to_schema()

# --- Exibir o schema no terminal
print("JSON Schema gerado:")
print(json.dumps(json_schema, indent=2))

# --- Garantir que a pasta 'schema/' exista
os.makedirs(os.path.dirname(SCHEMA_OUTPUT_PATH), exist_ok=True)

# --- Salvar o schema no arquivo
with open(SCHEMA_OUTPUT_PATH, "w", encoding="utf-8") as schema_file:
    json.dump(json_schema, schema_file, indent=2)

# --- Validação do JSON
print("\nValidando JSON de entrada com o schema...")

try:
    validate(instance=data, schema=json_schema)
    print("✅ JSON válido conforme o schema.")
except ValidationError as e:
    print("❌ JSON inválido:")
    print(e.message)
