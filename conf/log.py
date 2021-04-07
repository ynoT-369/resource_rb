import logging
import logging.config
import logging.handlers
from datetime import datetime
import random
import string
import pytz

# from app.util.api_util import ApiUtil


def random_string(k=10):
    """
    Generate a random string of fixed length
    :param k: length of random string
    """
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=k))


class LogConfig:
    # Logging settings
    @staticmethod
    def get_logger(logger_key: str):
        logging.getLogger("werkzeug").disabled = True
        logger = logging.getLogger(logger_key)

        handler = logging.handlers.TimedRotatingFileHandler(filename="logs/logger.log." + str(datetime.today().date()),
                                                            when="midnight",
                                                            interval=1,
                                                            backupCount=30,
                                                            encoding="utf-8")
        logger.addHandler(handler)

        def japan_time(*args):
            return datetime.now(pytz.timezone('Asia/Tokyo')).timetuple()

        formatter = logging.Formatter(
            fmt="%(asctime)s,%(msecs)3d JST [%(levelname)s] (%(filename)s:%(lineno)s) %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        formatter.converter = japan_time
        handler.setFormatter(formatter)

        logger.setLevel(logging.DEBUG)
        return logger
