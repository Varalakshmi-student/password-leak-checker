# 🔐 SecureCheck — Password Leak Checker

A web application to check if your password has been 
exposed in known data breaches.



![Python](https://img.shields.io/badge/Python-3.8+-blue)




![Flask](https://img.shields.io/badge/Flask-2.0+-green)




![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange)



## 🖥️ Project Screenshots

> Home Page — Enter password and check

## ✨ Features
- 🔍 Check if password is leaked
- 💪 Password strength meter
- ✨ Strong password generator
- 📋 Check history
- 🚨 Security recommendations
- 🔒 SHA-256 encryption

## 🛠️ Technologies Used
- **Backend** — Python, Flask
- **Frontend** — HTML, CSS, JavaScript
- **Database** — MySQL

## 📁 Project Structure
\`\`\`
password-leak-checker/
├── backend/
│   ├── app.py
│   ├── db.py
│   ├── add_password.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── database/
│   ├── schema.sql
│   ├── sample_data.sql
│   └── procedures.sql
├── docs/
│   ├── ER_diagram.png
│   └── report.pdf
└── README.md
\`\`\`

## ⚙️ How to Run

### 1. Clone Repository
\`\`\`bash
git clone https://github.com/YourUsername/password-leak-checker.git
cd password-leak-checker
\`\`\`

### 2. Install Requirements
\`\`\`bash
pip install flask mysql-connector-python flask-cors
\`\`\`

### 3. Setup MySQL Database
\`\`\`sql
CREATE DATABASE password_leak_db;
USE password_leak_db;
\`\`\`

### 4. Run Database Setup
\`\`\`bash
cd backend
python add_password.py
\`\`\`

### 5. Start Application
\`\`\`bash
python app.py
\`\`\`

### 6. Open Browser
\`\`\`
http://127.0.0.1:5000
\`\`\`

## 🔐 How It Works
1. User enters a password
2. Password is hashed using SHA-256
3. Hash is checked against breach database
4. Result shows if password is LEAKED or SAFE

## 👩‍💻 Developed By
**Varalakshmi**