-- A script that creates a table called first_table in the current database in your MySQL server
-- first_table description:
--   id INT
--   name VARCHAR(256)
-- The database name will be passed as an arguement of the mysql command
-- If the table already exists, the script should not fail
-- Not allowed to use the SELECT and SHOW statements

CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
