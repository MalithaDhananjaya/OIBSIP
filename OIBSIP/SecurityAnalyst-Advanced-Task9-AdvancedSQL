# Task 9: Advanced SQL Injection (SQLi) Demonstration and Remediation

## 📌 Executive Summary
This project demonstrates the exploitation and defensive remediation of an **Advanced SQL Injection (SQLi)** vulnerability using **Damn Vulnerable Web Application (DVWA)** configured at **High Security Level**. SQL Injection occurs when untrusted user input is directly concatenated into SQL database queries, allowing attackers to execute arbitrary database commands and extract sensitive information.

---

## 🎯 Technical Details
- **Target Application:** DVWA (High Security Level)
- **Vulnerability Type:** Union-Based SQL Injection
- **Target Endpoint:** SQL Injection (High Security Module)
- **Injected Parameter:** `id`

---

## 🛠️ Exploitation Methodology (Step-by-Step)

### 1. Security Level Configuration
Set the DVWA security level to `High`. At this level, input parameters are transferred via a secondary session window to evade standard automated query parameters.

### 2. Payload Selection
To break out of the original query structure and retrieve sensitive data from the `users` table, the following UNION-based SQLi payload was injected:

\```sql
1' UNION SELECT user, password FROM users #
\```

### 3. Execution & Results
The query executed successfully, rendering system credentials including usernames and their corresponding MD5 password hashes directly on the page:

| User ID / Input | First Name (Extracted User) | Surname (Extracted MD5 Hash)      |
|------------------|------------------------------|-------------------------------------|
| admin            | admin                        | 5f4dcc3b5aa765d61d8327deb882cf99   |
| gordonb          | gordonb                      | e99a18c428cb38d5f260853678922e03  |
| 1337             | 1337                          | 8d3533d75ae2c3966d7e0d4fcc69216b   |
| pablo            | pablo                        | 0d107d09f5bbe40cade3de5c71e9e9b7   |
| smithy           | smithy                       | 5f4dcc3b5aa765d61d8327deb882cf99   |

---

## 🔐 Remediation & Secure Defensive Architecture
To prevent SQL Injection completely, dynamic input concatenation must be replaced with **Parameterized Queries (Prepared Statements)** or an **Object-Relational Mapping (ORM)** framework.

### Secure Implementation (`secure_code.py`)
\```python
import mysql.connector

def get_user_details_secure(user_id):
    """
    Retrieves user details securely using Parameterized Queries.
    Prevents SQL Injection by ensuring user input is treated strictly as data.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="app_user",
            password="secure_password",
            database="dvwa"
        )
        cursor = connection.cursor(prepared=True)

        # Parameterized SQL query placeholder
        query = "SELECT first_name, last_name FROM users WHERE user_id = %s"

        # Input passed separately as a tuple
        cursor.execute(query, (user_id,))

        result = cursor.fetchall()
        return result
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return None

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
\```

---

## ✅ Key Mitigation Controls
- **Parameterized Queries (Prepared Statements):** Ensures the database compiler treats user input purely as data, never as executable SQL code.
- **Principle of Least Privilege (PoLP):** Restrict database service accounts from having administrative control (e.g., revoking `DROP` or `ALTER` permissions).
- **Input Validation & Sanitization:** Implement strong server-side validation alongside prepared statements as a defense-in-depth measure.

---

## 📸 Proof of Concept (Screenshots & Demo)
- **Proof Screenshots:** Uploaded within repository documentation.
- **Demonstration Video:** Shared via LinkedIn / YouTube post adhering to Oasis Infobyte task guidelines.

---

## ⚠️ Disclaimer
This exploitation was performed against DVWA, an application intentionally built with vulnerabilities for legal security training. Only test applications you own or have explicit written permission to assess.
