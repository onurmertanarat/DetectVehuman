import os
import logging

class LogSystem:
    def __init__(self, log_file="logs/system_log.txt"):
        self.log_file = log_file
        log_dir = os.path.dirname(self.log_file)

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(module)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    def log_event(self, event, level='info'):
        if level.lower() == 'debug':
            logging.debug(event)
        elif level.lower() == 'info':
            logging.info(event)
        elif level.lower() == 'warning':
            logging.warning(event)
        elif level.lower() == 'error':
            logging.error(event)
        elif level.lower() == 'critical':
            logging.critical(event)
        else:
            logging.info(event)

        print(f"Log ({level}): {event}")
