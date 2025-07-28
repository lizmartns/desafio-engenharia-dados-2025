import os
import sqlite3
import pytest

DB_PATH = "./database/erp.db"

TABLES = [
    "guest_checks",
    "detail_lines",
    "menu_items",
    "taxes",
    "discounts",
    "service_charges",
    "tender_media",
    "error_codes"
]

OPTIONAL_TABLES = {
    "discounts",
    "service_charges",
    "tender_media",
    "error_codes"
}

@pytest.fixture
def db_connection():
    assert os.path.exists(DB_PATH), "Banco de dados não foi criado."
    conn = sqlite3.connect(DB_PATH)
    yield conn
    conn.close()

@pytest.mark.parametrize("table", TABLES)
def test_table_exists_and_not_empty(db_connection, table):
    cursor = db_connection.cursor()

    # Verifica se a tabela existe
    cursor.execute(f"""
        SELECT COUNT(*) FROM sqlite_master 
        WHERE type='table' AND name='{table}'
    """)
    exists = cursor.fetchone()[0]
    assert exists == 1, f"Tabela {table} não existe no banco."

    # Verifica se há dados, exceto se a tabela for opcional
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]

    if table not in OPTIONAL_TABLES:
        assert count > 0, f"Tabela obrigatória {table} está vazia."
    else:
        print(f"Aviso: Tabela opcional {table} está vazia (permitido).")
