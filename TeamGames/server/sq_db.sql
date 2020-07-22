CREATE TABLE
IF NOT EXISTS users
(
id integer PRIMARY KEY AUTOINCREMENT,
user_login text NOT NULL,
user_password text NOT NULL,
user_email text NOT NULL
);