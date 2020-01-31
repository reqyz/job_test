CREATE EXTENSION pgcrypto;

CREATE TABLE public.users
(
    user_id serial PRIMARY KEY,
    name text NOT NULL,
    email text NOT NULL UNIQUE,
    password text NOT NULL,
    reg_date date NOT NULL DEFAULT now()
);

CREATE TABLE public.links
(
    link_id serial PRIMARY KEY,
    link text NOT NULL,
    user_id integer NOT NULL REFERENCES users (user_id) ON DELETE CASCADE
);

