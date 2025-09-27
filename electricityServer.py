from flask import Flask, render_template_string
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

    html = """
    <html>
    <head><title>Tabelle</title></head>
    <body>
        <h2>Meter Data</h2>
        <table border="1">
            <tr>
                <th>id</th>
                <th>load</th>
                <th>pv</th>
                <th>feedIn</th>
                <th>purchase</th>
                <th>timestamp</th>
            </tr>
            {% for row in data %}
            <tr>
                <td>{{ row.id }}</td>
                <td>{{ row.loadVal }}</td>
                <td>{{ row.pv }}</td>
                <td>{{ row.grid_feed_in }}</td>
                <td>{{ row.grid_purchase }}</td>
                <td>{{ row.saveTimestamp }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """

    return render_template_string(html, data=results)  

@app.route('/test')
def table():
    data = [
        {'Name': 'Alice', 'Alter': 30},
        {'Name': 'Bob', 'Alter': 25},
        {'Name': 'Charlie', 'Alter': 35}
    ]
    html = """
    <html>
    <head><title>Tabelle</title></head>
    <body>
        <h2>Personenliste</h2>
        <table border="1">
            <tr><th>Name</th><th>Alter</th></tr>
            {% for row in data %}
            <tr><td>{{ row.Name }}</td><td>{{ row.Alter }}</td></tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """
    return render_template_string(html, data=data)

if __name__ == '__main__':
    app.run(debug=True)
