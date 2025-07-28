-- Tabela de taxas de serviço aplicadas a um item
CREATE TABLE service_charges (
    guestCheckLineItemId INTEGER PRIMARY KEY,
    chargeAmount REAL,
    chargeCode TEXT,
    FOREIGN KEY (guestCheckLineItemId) REFERENCES detail_lines(guestCheckLineItemId)
);