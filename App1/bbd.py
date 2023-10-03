import sqlite3
import bcrypt

usuarios = [
        ('Ricardo', 'triste'),
        ('Paco', 'churro'),
        ('Alejandro', '123'),
        ('Angel', '1234'),
        ('Checo', 'crudo')
    ]
if __name__ == '__main__':
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    table = """
    CREATE TABLE IF NOT EXISTS usuarios (
        usuario VARCHAR(20) NOT NULL,
        password BLOB NOT NULL
    );
    """
    cursor.execute(table)
    conn.commit()

for usuario, password in usuarios:
    hashed_password = bcrypt.hashpw(password.encode('latin-1'), bcrypt.gensalt())
    cursor.execute("INSERT INTO usuarios (usuario, password) VALUES (?, ?)",
                    (usuario, hashed_password))
    conn.commit()
