COMPANY_SETUP_QUERY = "CREATE TABLE IF NOT EXISTS companies (name TEXT PRIMARY KEY, bio TEXT);"
INSERT_COMPANIES = "INSERT INTO companies VALUES ('Company 1', 'We care for worker rights! We fight for worker rights'), ('Company 2', 'Our workers are treated like kings'), ('NUS Greyhats', 'Please visit us at https://nusgreyhats.org/ or join us on telegram at https://t.me/+MZn4ohHrPj42NTU1');"
FLAG = r'greyhats{n0_u5e_h1ding_1n_und3r_th3_t4bl3s}'
FLAG_SETUP_QUERY = "CREATE TABLE IF NOT EXISTS flags (flag TEXT)"
INSERT_FLAG = f"INSERT INTO flags (flag) VALUES('{FLAG}')"
SECRET = "ThisIsTheFlaskSecretKey1234567890!@#$%^&*()ASDsgdg"

