import requests
import re
import datetime
import mysql.connector
from meter_data import MeterData

# Electricity Meter
# It reads data from an electricity meter and stores it in a database.

# URL, the edm file represents the right frame of the hansol ess web interface
RAW_DATA_URL = "http://192.168.178.36:21710/R3EMSAPP_EDM.edm?mode=monitor&submode=ems"
#RAW_DATA_URL = "http://192.168.178.36/R3EMSAPP_REAL.ems?file=ESSRealtimeStatus.json" # Echzeitdaten im JSON-Format
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process


# reads http output from configured RAW_DATA_URL and returns the text
def read_data_raw():
    response = requests.get(RAW_DATA_URL, timeout=10)
    response.raise_for_status()
    return response.text


def extract_val_from_table(table_html, label):
    match = re.search(rf'<td[^>]*>\s*{label}\s*</td>\s*<td[^>]*align=center[^>]*>(\d+)</td>', table_html, re.IGNORECASE)
    if match:
        return match.group(1)
    return None

def get_current_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# extracts the relevant values from the raw data using regex
def extract_today_wh_values(raw_data: str):
    # Suche den Abschnitt "Today Wh Value"
    pattern = r'<table[^>]*?>\s*<tr><td[^>]*?>\s*Today Wh Value\s*</td></tr>.*?</table>'
    match = re.search(pattern, raw_data, re.DOTALL | re.IGNORECASE)
    table_html = ""
    if match:
        table_html = match.group(0)

    print(f"Section Text: {table_html}")

    # Extrahiere die Werte mit Regex
    grid_pur = extract_val_from_table(table_html, "Grid-Pur")
    grid_feed = extract_val_from_table(table_html, "Grid-Feed")
    load = extract_val_from_table(table_html, "Load")
    pv = extract_val_from_table(table_html, "PV")
    print(f"Extracted values - Load: {load}, PV: {pv}, Grid Feed: {grid_feed}, Grid Purchase: {grid_pur}")

    return MeterData(
        load=int(load) if load else 0,
        pv=int(pv) if pv else 0,
        feed_in=int(grid_feed) if grid_feed else 0,
        purchase=int(grid_pur) if grid_pur else 0,
        saveTimestamp=get_current_timestamp()
    )


# stores the meter data in the MySQL database
def store_data_in_db(db_config, meter_data):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = """
        INSERT INTO meter_data (saveTimestamp, loadVal, pv, grid_feed_in, grid_purchase)
        VALUES (%s, %s, %s, %s, %s)
    """ 
    
    values = (
        meter_data.saveTimestamp,
        meter_data.load,
        meter_data.pv,
        meter_data.grid_feed_in,
        meter_data.grid_purchase
    )
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Electricity Meter program started')

    raw_data = read_data_raw()
    print(f"Raw data read: {raw_data}")
    meter_data = extract_today_wh_values(raw_data)
    db_config = {
    "host": "192.168.178.100",
    "user": "jojo",
    "password": "jojo",
    "database": "jojo"
    }
    store_data_in_db(db_config, meter_data)
    print(f"Electricity Meter program finished: {meter_data}")
