import logging
import os

# Create a logger
logger = logging.getLogger('AntivirusLogger')
logger.setLevel(logging.DEBUG)

# Create file handler for logging to a file
log_file = 'antivirus.log'
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)

# Create console handler for logging to console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Example log messages
logger.debug('Debugging message from the antivirus. ')
logger.info('Informational message from the antivirus. ')
logger.warning('Warning message from the antivirus. ')
logger.error('Error message from the antivirus. ')
logger.critical('Critical message from the antivirus.')
