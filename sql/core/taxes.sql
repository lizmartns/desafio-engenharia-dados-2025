-- Tabela de impostos aplicados ao pedido
CREATE TABLE taxes (
    guestCheckId INTEGER,
    taxNum INTEGER,
    txblSlsTtl REAL,
    taxCollTtl REAL,
    taxRate REAL,
    type INTEGER,
    FOREIGN KEY (guestCheckId) REFERENCES guest_checks(guestCheckId)
);