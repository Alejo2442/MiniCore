CREATE TABLE vendedores (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
);

CREATE TABLE reglas (
    id INTEGER PRIMARY KEY,
    monto_minimo REAL NOT NULL,
    porcentaje INTEGER NOT NULL
);

CREATE TABLE ventas (
    id INTEGER PRIMARY KEY,
    vendedor_id INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    monto REAL NOT NULL,
    FOREIGN KEY (vendedor_id) REFERENCES vendedores (id)
);

INSERT INTO vendedores (id, nombre) VALUES
(1, 'Alejandro Martinez'),
(2, 'Camilo Nunez'),
(3, 'Julian Pacheco'),
(4, 'Diego Vera'),
(5, 'Elena Pinango');

INSERT INTO reglas (id, monto_minimo, porcentaje) VALUES
(1, 500, 4),
(2, 1000, 7),
(3, 2000, 10),
(4, 3000, 13);

INSERT INTO ventas (id, vendedor_id, fecha, monto) VALUES
(1, 1, '2026-08-03', 450.00),
(2, 2, '2026-08-07', 1200.00),
(3, 3, '2026-08-10', 300.00),
(4, 4, '2026-08-14', 850.00),
(5, 5, '2026-08-18', 2100.00),
(6, 1, '2026-08-22', 700.00),
(7, 3, '2026-09-28', 950.00),
(8, 2, '2026-09-02', 600.00),
(9, 4, '2026-09-06', 1500.00),
(10, 5, '2026-09-11', 400.00),
(11, 1, '2026-09-15', 1800.00),
(12, 3, '2026-09-19', 250.00),
(13, 2, '2026-09-24', 980.00),
(14, 4, '2026-09-29', 320.00),
(15, 5, '2026-10-02', 1350.00),
(16, 1, '2026-10-08', 520.00),
(17, 2, '2026-10-12', 2300.00),
(18, 3, '2026-10-17', 1100.00),
(19, 4, '2026-10-23', 760.00),
(20, 5, '2026-10-28', 480.00);
