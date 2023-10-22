import socket
import sqlite3
import configparser
import time
import signal
import sys
from adsb_functions import create_database, data_stream_and_store

# Load configuration from a file
config = configparser.ConfigParser()
config.read('config.ini')

# Get the PiAware configuration parameters
piaware_ip = config.get('PiAware', 'IP')
piaware_port = config.getint('PiAware', 'Port')

if __name__ == "__main__":
    # Register the signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    
    # Start the data stream and database operations
    data_stream_and_store()


