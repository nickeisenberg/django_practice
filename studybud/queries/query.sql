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

select * from base_room;
