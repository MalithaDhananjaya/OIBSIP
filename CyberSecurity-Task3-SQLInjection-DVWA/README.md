# Task 3: SQL Injection on DVWA (Low Security)

## 📌 Overview
This project demonstrates the exploitation of a classic SQL Injection (SQLi) vulnerability on the Damn Vulnerable Web Application (DVWA) running on Low Security mode.

---

## 🎯 Target Information
- **Application:** DVWA (Damn Vulnerable Web Application)
- **Environment:** Docker / Kali Linux
- **Security Level:** Low
- **Vulnerability:** SQL Injection (Authentication & Logic Bypass)

---

## 🛠️ Exploitation Steps

### 1. Verification
Inputting a single quote (`'`) in the User ID field triggered a database syntax error, confirming the presence of an un-sanitized SQL query.

### 2. Logic Bypass Payload
\```sql
1' OR '1'='1
\```

### 3. Execution & Results
Executing the payload modified the query logic to always evaluate to `TRUE`, dumping all registered user accounts from the database:

- ID 1: Admin (admin / admin)
- ID 2: Gordon Brown
- ID 3: Hack Me
- ID 4: Pablo Picasso
- ID 5: Bob Smith

---

## 🕵️ Red Team Assessment & Remediation
- **Impact:** Critical (Full unauthorized database read access).
- **Mitigation:** Use Prepared Statements (Parameterized Queries) and input validation to prevent user input from modifying SQL query structure.

---

## ⚠️ Disclaimer
This exploitation was performed against DVWA, an application intentionally built with vulnerabilities for legal security training. Only test applications you own or have explicit written permission to assess.
