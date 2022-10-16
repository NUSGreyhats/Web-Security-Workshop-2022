USER_SETUP_QUERY = "CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)"
INSERT_ADMIN_USER = "INSERT INTO users (username, password) VALUES('admin', 'thisIsARandomAdminPassword')"
FLAG = r'flag{you_found_the_admin_flag}'