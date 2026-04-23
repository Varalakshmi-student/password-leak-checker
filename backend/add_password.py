import hashlib
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="example@2026",
        database="password_leak_db"
    )

def add_leaked_password(password, source):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT IGNORE INTO leaked_passwords (password_hash, source) VALUES (%s, %s)",
            (hashed, source)
        )
        conn.commit()
        print(f"✅ Added: {password}")
    except Exception as e:
        print(f"❌ Error adding {password}: {e}")
    finally:
        cursor.close()
        conn.close()

# ── Most Common Breached Passwords ──────────────────────────────

numeric_passwords = [
    "123456", "12345", "123456789", "1234", "12345678",
    "1234567", "1234567890", "000000", "111111", "222222",
    "333333", "444444", "555555", "666666", "777777",
    "888888", "999999", "112233", "121212", "123123",
    "123321", "654321", "987654321", "11111111", "00000000",
    "1111111", "7777777", "1q2w3e4r", "1qaz2wsx", "123qwe",
]

simple_passwords = [
    "password", "password1", "password123", "passw0rd", "p@ssword",
    "qwerty", "qwerty123", "qwertyuiop", "qazwsx", "qweasdzxc",
    "abc123", "abcd1234", "abcdef", "abcd", "abc",
    "iloveyou", "iloveyou1", "iloveyou2", "iloveme",
    "admin", "admin123", "admin1234", "administrator",
    "letmein", "letmein1", "letmein123",
    "welcome", "welcome1", "welcome123",
    "monkey", "monkey1", "monkey123",
    "dragon", "dragon1", "dragon123",
    "master", "master1", "master123",
    "sunshine", "sunshine1",
    "princess", "princess1",
    "football", "football1",
    "superman", "superman1",
    "batman", "batman123",
    "hello", "hello123", "hello1234",
    "shadow", "shadow1", "shadow123",
    "michael", "michael1",
    "jessica", "jessica1",
    "charlie", "charlie1",
    "donald", "donald1",
    "soccer", "soccer1",
    "hockey", "hockey1",
    "killer", "killer1",
    "george", "george1",
    "jordan", "jordan1",
    "harley", "harley1",
    "ranger", "ranger1",
    "daniel", "daniel1",
    "andrew", "andrew1",
    "andrea", "andrea1",
    "joshua", "joshua1",
    "hunter", "hunter1",
    "thomas", "thomas1",
    "robert", "robert1",
    "matrix", "matrix1",
    "cheese", "cheese1",
]

common_words = [
    "login", "login123",
    "pass", "pass123", "pass1234",
    "test", "test123", "test1234",
    "user", "user123", "user1234",
    "guest", "guest123",
    "demo", "demo123",
    "root", "root123",
    "toor", "toor123",
    "access", "access1",
    "secret", "secret1", "secret123",
    "mypass", "mypassword",
    "newpass", "newpassword",
    "changeme", "changeme1",
    "default", "default1",
    "temp", "temp123",
    "sample", "sample1",
    "example", "example1",
    "super", "super123",
    "system", "system1",
    "server", "server1",
    "internet", "internet1",
    "network", "network1",
    "computer", "computer1",
    "windows", "windows1",
    "office", "office123",
    "google", "google123",
    "amazon", "amazon123",
    "apple", "apple123",
    "netflix", "netflix1",
    "youtube", "youtube1",
    "twitter", "twitter1",
    "facebook", "facebook1",
    "instagram", "instagram1",
]

name_passwords = [
    "john", "john123",
    "jane", "jane123",
    "james", "james1",
    "david", "david1",
    "chris", "chris1",
    "peter", "peter1",
    "kevin", "kevin1",
    "steven", "steven1",
    "richard", "richard1",
    "joseph", "joseph1",
    "charles", "charles1",
    "william", "william1",
    "jennifer", "jennifer1",
    "ashley", "ashley1",
    "amanda", "amanda1",
    "melissa", "melissa1",
    "michelle", "michelle1",
    "sarah", "sarah123",
    "laura", "laura123",
    "lisa", "lisa123",
]

pattern_passwords = [
    "aaaaaa", "bbbbbb", "cccccc",
    "aabbcc", "abcabc",
    "asdfgh", "asdfghjkl",
    "zxcvbn", "zxcvbnm",
    "poiuyt", "lkjhgf",
    "pass@123", "pass@1234",
    "p@ss123", "p@ss1234",
    "P@ssw0rd", "P@ssword1",
    "Admin@123", "Admin@1234",
    "Welcome@1", "Welcome@123",
    "Test@123", "Test@1234",
    "India@123", "India@1234",
    "Password@1", "Password@123",
]

# ── Add All Passwords ────────────────────────────────────────────

all_passwords = {
    "numeric-breach":  numeric_passwords,
    "simple-breach":   simple_passwords,
    "common-breach":   common_words,
    "names-breach":    name_passwords,
    "pattern-breach":  pattern_passwords,
}

print("🚀 Starting to add breached passwords...\n")

total = 0
for source, passwords in all_passwords.items():
    print(f"\n📂 Adding {source}:")
    for pwd in passwords:
        add_leaked_password(pwd, source)
        total += 1

print(f"\n✅ Done! Total {total} passwords added to database.")