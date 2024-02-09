import logging


class Logger:
    @staticmethod
    def loggen():
        logger = logging.getLogger("Test Login")
        file_handler = logging.FileHandler('./logs/logs.txt')
        formatter = logging.Formatter(f"{'*' * 80}\n %(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger
