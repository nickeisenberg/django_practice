-- sql can be interpreted. In the other tmux pane, run sqlite3 db.sqlite3
-- to connect to the projects database. Then just run sql code line by line
-- for whatever query you want.

-- We can get all the table names
.tables

-- We can run standard queries
SELECT id, username FROM auth_user;

-- We can get the column names of a table
PRAGMA table_info(blog_post);

PRAGMA table_info(auth_user);

-- We can run standard sql code
SELECT * FROM blog_post 
where 
;
