CREATE DATABASE ma0yleidy;

CREATE USER ma0yleidy_user WITH PASSWORD '<secret_password>';
ALTER DATABASE ma0yleidy OWNER TO ma0yleidy_user;
GRANT ALL PRIVILEGES ON DATABASE ma0yleidy TO ma0yleidy_user;