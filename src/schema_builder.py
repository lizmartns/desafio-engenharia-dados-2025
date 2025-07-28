# schema_builder.py
import json
from genson import SchemaBuilder
from jsonschema import validate, ValidationError

with open("./data/ERP.json", "r") as f:
    data = json.load(f)

builder = SchemaBuilder()
builder.add_object(data)

json_schema = builder.to_schema()

print("JSON Schema gerado:")
print(json.dumps(json_schema, indent=2))

with open("./schema/erp_schema.json", "w") as schema_file:
    json.dump(json_schema, schema_file, indent=2)

# Validação do JSON

print("\nValidando JSON de entrada com o schema...")

try:
    validate(instance=data, schema=json_schema)
    print("✅ JSON válido conforme o schema.")
except ValidationError as e:
    print("❌ JSON inválido:")
    print(e.message)
