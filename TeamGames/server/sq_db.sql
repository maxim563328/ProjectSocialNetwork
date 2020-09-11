CREATE TABLE
IF NOT EXISTS users
(
id integer PRIMARY KEY AUTOINCREMENT,
user_login text NOT NULL,
user_password text NOT NULL,
user_email text NOT NULL
);

CREATE TABLE
IF NOT EXISTS posts
(
id integer PRIMARY KEY AUTOINCREMENT,
title text NOT NULL,
text text NOT NULL,
time integer NOT NULL
);

CREATE TABLE
IF NOT EXISTS dialog
(
sender_id integer NOT NULL,
recip_id integer NOT NULL,
chat_id integer NOT NULL,
);

CREATE TABLE
IF NOT EXISTS message
(
chat_messages_id integer NOT NULL,
chat_messages_text text NOT NULL,
chat_messages_fk_dialog_id integer NOT NULL,
chat_messages_fk_user_id integer NOT NULL,
chat_messages_fk_to_user_id integer NOT NULL,
chat_messages_isRead integer NOT NULL,
chat_messages_time integer NOT NULL DEFAULT 0
);
