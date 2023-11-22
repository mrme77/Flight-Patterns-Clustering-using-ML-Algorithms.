import sqlite3
import socket
import configparser
import time


# Create a SQLite database and define flight_data and navigation tables
def create_database():
    with sqlite3.connect('flight_data.db') as conn:
         cursor = conn.cursor()

        # Create the flight_data and navigation_data tables using a single loop
        for table_name in ['flight_data', 'navigation_data']:
            cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INTEGER PRIMARY KEY,
                    message_type TEXT,
                    aircraft_icao_id TEXT,
                    date TEXT,
                    timestamp TEXT,
                    altitude REAL,
                    latitude REAL,
                    longitude REAL,
                    speed REAL,
                    heading REAL
                )
            ''')

        conn.commit()

# Create a function to handle the data stream and database operations
def data_stream_and_store():
     """
    Continuously streams and stores data received from a network socket connected to a Raspberry Pi running PI Aware 7.2.

    This function connects to a SQLite database, establishes a network socket connection, and continuously receives data from the
    socket. It processes and inserts the data into the appropriate tables in the database based on message type, including flight
    data and navigation data. The function also handles socket timeouts and errors gracefully.

    Returns:
        None
    """
    while True:
        try:
            # Connect to the SQLite database
            with sqlite3.connect('flight_data.db') as conn:
                cursor = conn.cursor()

                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(600)

                try:
                    sock.connect((piaware_ip, piaware_port))
                    print('Connection established')

                    while True:
                        data = sock.recv(4096)

                        if not data:
                            print("No data received.")
                            print('Restarting socket')
                            sock.close()
                            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            sock.settimeout(600)
                            sock.connect((piaware_ip, piaware_port))
                            continue

                        data_str = data.decode('utf-8')
                        fields = data_str.split(',')

                        # Check for valid message type
                        if fields[0] == 'MSG' and (fields[1] == '3' or fields[1] == '4') and len(fields) > 20:
                            message_type = fields[0] + fields[1]
                            aircraft_icao_id, date, timestamp = fields[4], fields[6], fields[7]

                            if fields[1] == '3':
                                altitude, latitude, longitude = fields[11], fields[14], fields[15]
                                cursor.execute("INSERT INTO flight_data (message_type, aircraft_icao_id, date, timestamp, altitude, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?)",
                                               (message_type, aircraft_icao_id, date, timestamp, altitude, latitude, longitude))
                                print(f"Record added - Message Type: {message_type}, Aircraft: {aircraft_icao_id}, Altitude: {altitude}, Latitude: {latitude}, Longitude: {longitude}")
                            else:
                                speed, heading = fields[12], fields[13]
                                cursor.execute("INSERT INTO navigation_data (message_type, aircraft_icao_id, date, timestamp, speed, heading) VALUES (?, ?, ?, ?, ?, ?)",
                                               (message_type, aircraft_icao_id, date, timestamp, speed, heading))
                                print(f"Record added - Message Type: {message_type}, Aircraft: {aircraft_icao_id}, Speed: {speed}, Heading: {heading}")

                            conn.commit()
                            time.sleep(10)

                except socket.timeout:
                    print("Socket timeout, waiting for data...")
                    time.sleep(10)
                    print('Restarting socket')
                    sock.close()
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(600)
                    sock.connect((piaware_ip, piaware_port))
                except Exception as e:
                    print(f"Error: {e}")

        except Exception as e:
            print(f"Outer Error: {e}")
