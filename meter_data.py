'''
Data class to hold the meter data values:
load: current load in Wh
pv: current PV production in Wh
grid_feed_in: current grid feed-in power in Wh
grid_purchase: current grid purchase power in Wh
saveTimsteestamp: timestamp when the data was saved

Create-Statement for mySQL:
CREATE TABLE IF NOT EXISTS meter_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    load INT,
    pv INT,
    grid_feed_in INT,
    grid_purchase INT,
    saveTimestamp DATETIME
);

'''

class MeterData:
    def __init__(self, load: int, pv: int, feed_in: int, purchase: int, saveTimestamp):
        self.load = load
        self.pv = pv
        self.grid_feed_in = feed_in
        self.grid_purchase = purchase
        self.saveTimestamp = saveTimestamp

    def __repr__(self):
        return (f"MeterData(load={self.load}, pv={self.pv}, "
                f"grid_feed_in={self.grid_feed_in}, grid_purchase={self.grid_purchase}, "
                f"timestamp={self.saveTimestamp})")