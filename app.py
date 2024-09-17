from flask import Flask
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="my_postgres",
        database="testdb",
        user="vika_test",
        password="vika123"
    )
    return conn

@app.route('/add')
def add_record():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO test_table (name) VALUES ('DevOps')")
    conn.commit()
    cur.close()
    conn.close()
    return "Record with 'DevOps' added!"

@app.route('/delete')
def delete_record():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM test_table WHERE id = (SELECT id FROM test_table WHERE name = 'DevOps' ORDER BY id ASC LIMIT 1)")
    conn.commit()
    cur.close()
    conn.close()
    return "One 'DevOps' record deleted!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
