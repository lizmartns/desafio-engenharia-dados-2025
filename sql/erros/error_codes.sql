-- Tabela de códigos de erro relacionados a um item
CREATE TABLE error_codes (
    guestCheckLineItemId INTEGER PRIMARY KEY,
    errorCode TEXT,
    message TEXT,
    FOREIGN KEY (guestCheckLineItemId) REFERENCES detail_lines(guestCheckLineItemId)
);