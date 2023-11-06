-- Show all the available tables
.tables

-- Show all the columns from auth_user
pragma table_info(auth_user);

select username from auth_user;

-- Show all the columns from auth_user_groups
pragma table_info(auth_user_groups);

select * from auth_user_groups;

-- Show all the columns from auth_user_groups
pragma table_info(base_room);

select id, name from base_room;

pragma table_info(base_room);

select name from base_topic;

pragma table_info(base_message);

select * from base_message;

