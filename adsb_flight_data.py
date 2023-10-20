import socket
import sqlite3
import configparser
import time
import signal
import sys

# Load configuration from a file
config = configparser.ConfigParser()
config.read('config.ini')

# Get the PiAware configuration parameters
piaware_ip = config.get('PiAware', 'IP')
piaware_port = config.getint('PiAware', 'Port')


# Create a SQLite database and define flight_data and navigation table
def create_database():
    conn = sqlite3.connect('flight_data.db')  # Replace with the desired database name
    cursor = conn.cursor()

    # Create the flight_data table
    cursor.execute(''' DROP TABLE IF EXISTS flight_data''')
    cursor.execute(''' DROP TABLE IF EXISTS navigation_data''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS flight_data (
            id INTEGER PRIMARY KEY,
            message_type TEXT,
            aircraft_icao_id TEXT,
            date TEXT,
            timestamp TEXT,
            altitude REAL,
            latitude REAL,
            longitude REAL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS navigation_data (
            id INTEGER PRIMARY KEY,
            message_type TEXT,
            aircraft_icao_id TEXT,
            date TEXT,
            timestamp TEXT,
            speed REAL,
            heading REAL
            
        )
    ''')
    conn.commit()
    conn.close()

# Create the database and flight_data table
create_database()

# Handle Ctrl+C to gracefully exit the program
def signal_handler(signal, frame):
    print("Exiting the program.")
    sys.exit(0)


# Create a function to handle the data stream and database operations
def data_stream_and_store():
    # Connect to the SQLite database
    conn = sqlite3.connect('flight_data.db')
    cursor = conn.cursor()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(600)  

    try:
        sock.connect((piaware_ip, piaware_port))
        print('Connection established')

        while True:
            try:
                data = sock.recv(4096)
                if not data:
                    print("No data received.")
                    break

                data_str = data.decode('utf-8')
                fields = data_str.split(',')
                
                
                # Handle the case where the MSG message type is not 3 or 4
                if not fields[0] == 'MSG' or not (fields[1] == '3' or fields[1] == '4'):
                    continue


                # Insert the data into the correct table
                if fields[1] == '3':
                      cursor.execute("INSERT INTO flight_data (message_type, aircraft_icao_id, date, timestamp, altitude, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (fields[0]+fields[1], fields[4], fields[6], fields[7], fields[11], fields[14], fields[15]))
                      print(f"Record added - Message Type: {fields[0]+fields[1]}, Aircraft: {fields[4]}, Altitude: {fields[11]}, Latitude: {fields[14]}, Longitude: {fields[15]}")
                
                elif fields[1] == '4':
                      cursor.execute("INSERT INTO navigation_data (message_type, aircraft_icao_id, date, timestamp, speed, heading) VALUES (?, ?, ?, ?, ?, ?)",
                  (fields[0]+fields[1], fields[4], fields[6], fields[7], fields[12], fields[13]))
                      print(f"Record added - Message Type: {fields[0]+fields[1]}, Aircraft: {fields[4]}, Speed: {fields[12]}, Heading: {fields[13]}")
                # Commit the changes to the database
                conn.commit()

            except socket.timeout:
                print("Socket timeout, waiting for data...")
                time.sleep(10)
            except Exception as e:
                print(f"Error: {e}")
    except socket.error as e:
        print(f"Socket error: {e}")
    finally:
        cursor.close()
        conn.close()
        sock.close()

# Start the data stream and database operations
if __name__ == "__main__":
    # Register the signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    
    # Start the data stream and database operations
    data_stream_and_store()
