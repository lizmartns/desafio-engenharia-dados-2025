-- Tabela de métodos de pagamento associados a um item
CREATE TABLE tender_media (
    guestCheckLineItemId INTEGER PRIMARY KEY,
    mediaType TEXT,
    amount REAL,
    FOREIGN KEY (guestCheckLineItemId) REFERENCES detail_lines(guestCheckLineItemId)
);