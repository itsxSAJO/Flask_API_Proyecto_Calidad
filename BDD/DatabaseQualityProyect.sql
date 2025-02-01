-- Tabla: terapeuta
CREATE TABLE public.terapeuta (
    id SERIAL PRIMARY KEY,
    nui VARCHAR(10) UNIQUE,
    nombre VARCHAR(20),
    apellido VARCHAR(20),
    especialidad VARCHAR(100),
    estado BOOLEAN NOT NULL,
    contrasena VARCHAR
);

-- Tabla: paciente
CREATE TABLE public.paciente (
    id SERIAL PRIMARY KEY,
    nui VARCHAR(10) UNIQUE,
    nombre VARCHAR(20),
    apellido VARCHAR(20),
    edad INTEGER,
    direccion VARCHAR(100),
    id_terapeuta INTEGER NOT NULL REFERENCES public.terapeuta(id) ON DELETE CASCADE,
    estado BOOLEAN NOT NULL DEFAULT true
);

-- Tabla: sesion
CREATE TABLE public.sesion (
    id_intento SERIAL PRIMARY KEY,
    id_paciente INTEGER NOT NULL REFERENCES public.paciente(id) ON DELETE CASCADE,
    fecha DATE NOT NULL,
    duracion TIME NOT NULL,
    puntaje INTEGER,
    aciertos INTEGER DEFAULT 0,
    errores INTEGER DEFAULT 0
);

-- Insertar datos en la tabla terapeuta
INSERT INTO public.terapeuta (nui, nombre, apellido, especialidad, estado, contrasena) VALUES
('0102034567', 'Carlos', 'Perez', 'Psicologia Clinica', true, 'abcd'),
('0102045678', 'Ana', 'Lopez', 'Psicologia Infantil', true, 'abcd'),
('0102056789', 'Luis', 'Gomez', 'Psicologia Educativa', true, 'abcd'),
('0102067890', 'Maria', 'Martinez', 'Psicologia Familiar', true, 'abcd'),
('0102078901', 'Jose', 'Hernandez', 'Psicologia Laboral', true, 'abcd');

-- Insertar datos en la tabla paciente
INSERT INTO public.paciente (nui, nombre, apellido, edad, direccion, id_terapeuta, estado) VALUES
('0102089012', 'Juan', 'Rodriguez', 30, 'Av. Amazonas 123', 1, true),
('0102090123', 'Maria', 'Gonzalez', 25, 'Calle 10, Quito', 2, true),
('0102101234', 'Pedro', 'Jimenez', 40, 'Calle El Oro 456', 3, true),
('0102112345', 'Luisa', 'Vargas', 35, 'Calle Jose Marti 789', 4, true),
('0102123456', 'Carlos', 'Mendez', 28, 'Calle 2, Guayaquil', 5, true);

-- Insertar datos en la tabla sesion
INSERT INTO public.sesion (id_paciente, fecha, duracion, puntaje) VALUES
(1, '2024-11-01', '00:45:00', 80),
(2, '2024-11-02', '01:00:00', 90),
(3, '2024-11-03', '00:30:00', 70),
(4, '2024-11-04', '01:15:00', 85),
(5, '2024-11-05', '00:50:00', 88);
