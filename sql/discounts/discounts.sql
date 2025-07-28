-- Tabela de descontos aplicados a um item
CREATE TABLE discounts (
    guestCheckLineItemId INTEGER PRIMARY KEY,
    discountAmount REAL,
    discountType TEXT,
    FOREIGN KEY (guestCheckLineItemId) REFERENCES detail_lines(guestCheckLineItemId)
);