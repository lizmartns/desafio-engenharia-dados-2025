import json
import pandas as pd
from sqlalchemy import create_engine, text
import os

# --- Caminhos
JSON_PATH = "./data/ERP.json"
DB_PATH = "./database/erp.db"

# --- Garantir que a pasta do banco exista
os.makedirs("./database", exist_ok=True)

# --- Leitura do JSON
with open(JSON_PATH) as f:
    data = json.load(f)

guest_checks = data.get('guestChecks', [])

# --- Inicializar listas acumuladoras
guest_check_rows = []
details = []
menu_items = []
discounts = []
service_charges = []
tender_media = []
error_codes = []
taxes = []

# --- Processar todos os guestChecks
for guest_check in guest_checks:
    guest_check_rows.append({
        'guestCheckId': guest_check['guestCheckId'],
        'chkNum': guest_check.get('chkNum'),
        'opnBusDt': guest_check.get('opnBusDt'),
        'clsdBusDt': guest_check.get('clsdBusDt'),
        'empNum': guest_check.get('empNum'),
        'subTtl': guest_check.get('subTtl'),
        'chkTtl': guest_check.get('chkTtl'),
        'dscTtl': guest_check.get('dscTtl'),
        'payTtl': guest_check.get('payTtl'),
        'rvcNum': guest_check.get('rvcNum'),
        'tblNum': guest_check.get('tblNum'),
        'tblName': guest_check.get('tblName'),
        'gstCnt': guest_check.get('gstCnt'),
        'numSrvcRd': guest_check.get('numSrvcRd'),
        'numChkPrntd': guest_check.get('numChkPrntd'),
        'clsdFlag': guest_check.get('clsdFlag')
    })

    for line in guest_check.get('detailLines', []):
        line_id = line.get('guestCheckLineItemId')

        details.append({
            'guestCheckLineItemId': line_id,
            'guestCheckId': guest_check['guestCheckId'],
            'lineNum': line.get('lineNum'),
            'busDt': line.get('busDt'),
            'dspTtl': line.get('dspTtl'),
            'dspQty': line.get('dspQty'),
            'aggTtl': line.get('aggTtl'),
            'aggQty': line.get('aggQty'),
            'svcRndNum': line.get('svcRndNum'),
            'seatNum': line.get('seatNum'),
            'chkEmpId': line.get('chkEmpId'),
            'chkEmpNum': line.get('chkEmpNum'),
        })

        if 'menuItem' in line:
            menu_items.append({
                'guestCheckLineItemId': line_id,
                'miNum': line['menuItem'].get('miNum'),
                'modFlag': line['menuItem'].get('modFlag'),
                'inclTax': line['menuItem'].get('inclTax'),
                'activeTaxes': line['menuItem'].get('activeTaxes'),
                'prcLvl': line['menuItem'].get('prcLvl')
            })

        if 'discount' in line:
            discounts.append({
                'guestCheckLineItemId': line_id,
                'discountAmount': line['discount'].get('amount'),
                'discountType': line['discount'].get('type')
            })

        if 'serviceCharge' in line:
            service_charges.append({
                'guestCheckLineItemId': line_id,
                'chargeAmount': line['serviceCharge'].get('amount'),
                'chargeCode': line['serviceCharge'].get('code')
            })

        if 'tenderMedia' in line:
            tender_media.append({
                'guestCheckLineItemId': line_id,
                'mediaType': line['tenderMedia'].get('type'),
                'amount': line['tenderMedia'].get('amount')
            })

        if 'errorCode' in line:
            error_codes.append({
                'guestCheckLineItemId': line_id,
                'errorCode': line['errorCode'].get('code'),
                'message': line['errorCode'].get('message')
            })

    taxes_field = guest_check.get("taxes") or guest_check.get("taxation") or []
    for tax in taxes_field:
        taxes.append({
            'guestCheckId': guest_check['guestCheckId'],
            'taxNum': tax.get('taxNum'),
            'txblSlsTtl': tax.get('txblSlsTtl'),
            'taxCollTtl': tax.get('taxCollTtl'),
            'taxRate': tax.get('taxRate'),
            'type': tax.get('type')
        })

# --- Criar DataFrames com colunas bem definidas
guest_check_df = pd.DataFrame(guest_check_rows)
detail_df = pd.DataFrame(details)
menu_df = pd.DataFrame(menu_items, columns=["guestCheckLineItemId", "miNum", "modFlag", "inclTax", "activeTaxes", "prcLvl"])
tax_df = pd.DataFrame(taxes, columns=["guestCheckId", "taxNum", "txblSlsTtl", "taxCollTtl", "taxRate", "type"])
discount_df = pd.DataFrame(discounts, columns=["guestCheckLineItemId", "discountAmount", "discountType"])
service_df = pd.DataFrame(service_charges, columns=["guestCheckLineItemId", "chargeAmount", "chargeCode"])
tender_df = pd.DataFrame(tender_media, columns=["guestCheckLineItemId", "mediaType", "amount"])
error_df = pd.DataFrame(error_codes, columns=["guestCheckLineItemId", "errorCode", "message"])

# --- Criar banco SQLite
engine = create_engine(f"sqlite:///{DB_PATH}")

# --- Inserir DataFrames no banco
guest_check_df.to_sql("guest_checks", engine, if_exists="replace", index=False)
detail_df.to_sql("detail_lines", engine, if_exists="replace", index=False)
menu_df.to_sql("menu_items", engine, if_exists="replace", index=False)
tax_df.to_sql("taxes", engine, if_exists="replace", index=False)
discount_df.to_sql("discounts", engine, if_exists="replace", index=False)
service_df.to_sql("service_charges", engine, if_exists="replace", index=False)
tender_df.to_sql("tender_media", engine, if_exists="replace", index=False)
error_df.to_sql("error_codes", engine, if_exists="replace", index=False)

# --- Contagem por tabela
print("Dados carregados com sucesso no banco SQLite.")
print(f"Banco gerado em: {DB_PATH}")

with engine.connect() as conn:
    for table in [
        "guest_checks",
        "detail_lines",
        "menu_items",
        "taxes",
        "discounts",
        "service_charges",
        "tender_media",
        "error_codes"
    ]:
        result = conn.execute(text(f"SELECT COUNT(*) FROM {table}"))
        count = result.scalar()
        print(f"{table}: {count} registros")
