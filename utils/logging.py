import logging 

"""
This module provides logging configuration for the application.

The `configure_logging` function sets up the logging system to output messages
with a level of INFO or higher, formatted to include the timestamp, log level,
and the actual log message.
"""

def configure_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')