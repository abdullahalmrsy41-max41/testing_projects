import logging
class CustomLogger:
    @staticmethod
    def method_logger():
        logging.basicConfig(filename="logs/automation.log",
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S',level=logging.INFO,force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger