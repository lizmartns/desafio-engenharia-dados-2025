import json
import pytest
from jsonschema import validate, ValidationError

@pytest.fixture
def schema_and_data():
    with open("./schema/erp_schema.json") as schema_file:
        schema = json.load(schema_file)
    with open("./data/ERP.json") as data_file:
        data = json.load(data_file)
    return schema, data

def test_json_validation(schema_and_data):
    schema, data = schema_and_data
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        pytest.fail(f"JSON inválido conforme o schema: {e.message}")
