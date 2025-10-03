from flask import Flask, render_template
import mysql.connector


app = Flask(__name__)

def read_all_meter_data(db_config):

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM meter_data")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

@app.route('/')
def get_meter_data():
    # Auslesen der Zählerdaten
    db_config = {
    "host": "192.168.178.100",
    "user": "jojo",
    "password": "jojo",
    "database": "jojo"
    }
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM meter_data")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    print(f"Fetched {len(results)} records from database.")
    print(results)

    return render_template("meter_table.html", data=results)


if __name__ == '__main__':
    app.run(debug=True)
