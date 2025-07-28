-- Tabela principal do pedido (guest check)
CREATE TABLE guest_checks (
    guestCheckId INTEGER PRIMARY KEY,
    chkNum INTEGER,
    opnBusDt DATE,
    clsdBusDt DATE,
    empNum INTEGER,
    subTtl REAL,
    chkTtl REAL,
    dscTtl REAL,
    payTtl REAL,
    rvcNum INTEGER,
    tblNum INTEGER,
    tblName TEXT,
    gstCnt INTEGER,
    numSrvcRd INTEGER,
    numChkPrntd INTEGER,
    clsdFlag BOOLEAN
);