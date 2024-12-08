--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2
-- Dumped by pg_dump version 17.2

-- Started on 2024-12-08 13:28:19

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: pg_database_owner
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO pg_database_owner;

--
-- TOC entry 4876 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: pg_database_owner
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 220 (class 1259 OID 16398)
-- Name: paciente; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.paciente (
    id integer NOT NULL,
    nui character varying(10),
    nombre character varying(20),
    apellido character varying(20),
    edad integer,
    direccion character varying(100),
    id_terapeuta integer NOT NULL,
    estado boolean NOT NULL
);


ALTER TABLE public.paciente OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16397)
-- Name: paciente_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.paciente_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.paciente_id_seq OWNER TO postgres;

--
-- TOC entry 4877 (class 0 OID 0)
-- Dependencies: 219
-- Name: paciente_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.paciente_id_seq OWNED BY public.paciente.id;


--
-- TOC entry 222 (class 1259 OID 16412)
-- Name: sesion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sesion (
    id_intento integer NOT NULL,
    id_paciente integer NOT NULL,
    fecha date NOT NULL,
    duracion time without time zone NOT NULL,
    puntaje integer
);


ALTER TABLE public.sesion OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16411)
-- Name: sesion_id_intento_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sesion_id_intento_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.sesion_id_intento_seq OWNER TO postgres;

--
-- TOC entry 4878 (class 0 OID 0)
-- Dependencies: 221
-- Name: sesion_id_intento_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sesion_id_intento_seq OWNED BY public.sesion.id_intento;


--
-- TOC entry 218 (class 1259 OID 16389)
-- Name: terapeuta; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.terapeuta (
    id integer NOT NULL,
    nui character varying(10),
    nombre character varying(20),
    apellido character varying(20),
    especialidad character varying(100),
    estado boolean NOT NULL,
    contrasena character varying
);


ALTER TABLE public.terapeuta OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16388)
-- Name: terapeuta_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.terapeuta_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.terapeuta_id_seq OWNER TO postgres;

--
-- TOC entry 4879 (class 0 OID 0)
-- Dependencies: 217
-- Name: terapeuta_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.terapeuta_id_seq OWNED BY public.terapeuta.id;


--
-- TOC entry 4706 (class 2604 OID 16401)
-- Name: paciente id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paciente ALTER COLUMN id SET DEFAULT nextval('public.paciente_id_seq'::regclass);


--
-- TOC entry 4707 (class 2604 OID 16415)
-- Name: sesion id_intento; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sesion ALTER COLUMN id_intento SET DEFAULT nextval('public.sesion_id_intento_seq'::regclass);


--
-- TOC entry 4705 (class 2604 OID 16392)
-- Name: terapeuta id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.terapeuta ALTER COLUMN id SET DEFAULT nextval('public.terapeuta_id_seq'::regclass);


--
-- TOC entry 4868 (class 0 OID 16398)
-- Dependencies: 220
-- Data for Name: paciente; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.paciente (id, nui, nombre, apellido, edad, direccion, id_terapeuta, estado) FROM stdin;
1	0102089012	Juan	Rodriguez	30	Av. Amazonas 123	1	t
2	0102090123	Maria	Gonzalez	25	Calle 10, Quito	2	t
3	0102101234	Pedro	Jimenez	40	Calle El Oro 456	3	t
4	0102112345	Luisa	Vargas	35	Calle Jose Marti 789	4	t
5	0102123456	Carlos	Mendez	28	Calle 2, Guayaquil	5	t
\.


--
-- TOC entry 4870 (class 0 OID 16412)
-- Dependencies: 222
-- Data for Name: sesion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sesion (id_intento, id_paciente, fecha, duracion, puntaje) FROM stdin;
1	1	2024-11-01	00:45:00	80
2	2	2024-11-02	01:00:00	90
3	3	2024-11-03	00:30:00	70
4	4	2024-11-04	01:15:00	85
5	5	2024-11-05	00:50:00	88
\.


--
-- TOC entry 4866 (class 0 OID 16389)
-- Dependencies: 218
-- Data for Name: terapeuta; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.terapeuta (id, nui, nombre, apellido, especialidad, estado, contrasena) FROM stdin;
1	0102034567	Carlos	Perez	Psicologia Clinica	t	abcd
2	0102045678	Ana	Lopez	Psicologia Infantil	t	abcd
3	0102056789	Luis	Gomez	Psicologia Educativa	t	abcd
4	0102067890	Maria	Martinez	Psicologia Familiar	t	abcd
5	0102078901	Jose	Hernandez	Psicologia Laboral	t	abcd
\.


--
-- TOC entry 4880 (class 0 OID 0)
-- Dependencies: 219
-- Name: paciente_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.paciente_id_seq', 5, true);


--
-- TOC entry 4881 (class 0 OID 0)
-- Dependencies: 221
-- Name: sesion_id_intento_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sesion_id_intento_seq', 5, true);


--
-- TOC entry 4882 (class 0 OID 0)
-- Dependencies: 217
-- Name: terapeuta_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.terapeuta_id_seq', 5, true);


--
-- TOC entry 4713 (class 2606 OID 16405)
-- Name: paciente paciente_nui_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paciente
    ADD CONSTRAINT paciente_nui_key UNIQUE (nui);


--
-- TOC entry 4715 (class 2606 OID 16403)
-- Name: paciente paciente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paciente
    ADD CONSTRAINT paciente_pkey PRIMARY KEY (id);


--
-- TOC entry 4717 (class 2606 OID 16417)
-- Name: sesion sesion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sesion
    ADD CONSTRAINT sesion_pkey PRIMARY KEY (id_intento);


--
-- TOC entry 4709 (class 2606 OID 16396)
-- Name: terapeuta terapeuta_nui_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.terapeuta
    ADD CONSTRAINT terapeuta_nui_key UNIQUE (nui);


--
-- TOC entry 4711 (class 2606 OID 16394)
-- Name: terapeuta terapeuta_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.terapeuta
    ADD CONSTRAINT terapeuta_pkey PRIMARY KEY (id);


--
-- TOC entry 4719 (class 2606 OID 16418)
-- Name: sesion fk_paciente; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sesion
    ADD CONSTRAINT fk_paciente FOREIGN KEY (id_paciente) REFERENCES public.paciente(id) ON DELETE CASCADE;


--
-- TOC entry 4718 (class 2606 OID 16406)
-- Name: paciente fk_terapeuta; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paciente
    ADD CONSTRAINT fk_terapeuta FOREIGN KEY (id_terapeuta) REFERENCES public.terapeuta(id) ON DELETE CASCADE;


-- Completed on 2024-12-08 13:28:19

--
-- PostgreSQL database dump complete
--

