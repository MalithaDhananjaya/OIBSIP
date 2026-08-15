cat << 'EOF' > secure_code.py
import mysql.connector

def get_user_details(user_id):
    connection = mysql.connector.connect(
        host="localhost",
        user="db_user",
        password="db_password",
        database="dvwa"
    )
    cursor = connection.cursor(prepared=True)
    
    # Parameterized Query prevents SQL Injection
    query = "SELECT first_name, last_name FROM users WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    
    result = cursor.fetchall()
    return result
EOF
