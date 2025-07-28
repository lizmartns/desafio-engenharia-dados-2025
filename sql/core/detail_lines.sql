-- Tabela de itens da conta (detalhes)
CREATE TABLE detail_lines (
    guestCheckLineItemId INTEGER PRIMARY KEY,
    guestCheckId INTEGER NOT NULL,
    lineNum INTEGER,
    busDt DATE,
    dspTtl REAL,
    dspQty INTEGER,
    aggTtl REAL,
    aggQty INTEGER,
    svcRndNum INTEGER,
    seatNum INTEGER,
    chkEmpId INTEGER,
    chkEmpNum INTEGER,
    FOREIGN KEY (guestCheckId) REFERENCES guest_checks(guestCheckId)
);