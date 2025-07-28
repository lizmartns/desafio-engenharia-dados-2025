import os
import json
from datetime import date
from pathlib import Path

# Simula chamadas para 5 endpoints
ENDPOINTS = {
    "getFiscalInvoice": {"invoiceNumber": "F1234", "total": 100.0},
    "getGuestChecks": {"checks": [{"id": 1, "amount": 109.9}]},
    "getChargeBack": {"chargeBacks": [{"storeId": "001", "reason": "cancel"}]},
    "getTransactions": {"transactions": [{"id": "TX987", "method": "credit_card"}]},
    "getCashManagementDetails": {"cash": {"open": 500.0, "close": 480.0}}
}

STORE_ID = "001"
TODAY = date.today()

BASE_PATH = Path("datalake/raw")

def simulate_api_call(endpoint: str, payload: dict) -> dict:
    """Simula uma resposta de API com um payload fixo."""
    return {
        "endpoint": endpoint,
        "date": TODAY.isoformat(),
        "storeId": STORE_ID,
        "data": payload
    }

def save_response(endpoint: str, response: dict):
    """Cria diretório e salva resposta como JSON."""
    path = BASE_PATH / endpoint / f"year={TODAY.year}" / f"month={TODAY.month:02}" / f"day={TODAY.day:02}" / f"store_id={STORE_ID}"
    os.makedirs(path, exist_ok=True)

    file_path = path / "response.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(response, f, ensure_ascii=False, indent=2)

    print(f"Simulação salva: {file_path}")

def main():
    print("Simulando chamadas de API e salvando no Data Lake...\n")

    for endpoint, payload in ENDPOINTS.items():
        response = simulate_api_call(endpoint, payload)
        save_response(endpoint, response)

    print("\n Finalizado. Respostas simuladas salvas em `datalake/raw/`.")

if __name__ == "__main__":
    main()
