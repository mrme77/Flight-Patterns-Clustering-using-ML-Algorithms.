import socket
import time
import signal
import sys
import adsb_functions


#Handle Ctrl+C to gracefully exit the program
def signal_handler(sig, frame):
    print("Exiting the program.")
    sys.exit(0)

if __name__ == "__main__":
    # Register the signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    # Create the database and start the data stream and database operations
    create_database()
    data_stream_and_store()
