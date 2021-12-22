import logging

class PerfLogger:
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)
    
    def get_logger(self, name=None, log_file='./logs/output.log'):
        logger = logging.getLogger(name)
        formatter = logging.Formatter(u'%(asctime)s [%(levelname)8s] | %(message)s')
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        return logger
