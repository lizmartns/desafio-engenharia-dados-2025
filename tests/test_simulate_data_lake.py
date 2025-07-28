import os
import json
from datetime import date
from pathlib import Path
import pytest

TODAY = date.today()
STORE_ID = "001"
ENDPOINTS = [
    "getFiscalInvoice",
    "getGuestChecks",
    "getChargeBack",
    "getTransactions",
    "getCashManagementDetails"
]

BASE_PATH = Path("datalake/raw")

@pytest.mark.parametrize("endpoint", ENDPOINTS)
def test_api_response_saved(endpoint):
    path = BASE_PATH / endpoint / f"year={TODAY.year}" / f"month={TODAY.month:02}" / f"day={TODAY.day:02}" / f"store_id={STORE_ID}" / "response.json"
    assert path.exists(), f"Arquivo não encontrado: {path}"

    with open(path) as f:
        data = json.load(f)
        assert "data" in data, f"Campo 'data' ausente na resposta simulada de {endpoint}"
