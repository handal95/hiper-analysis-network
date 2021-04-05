import sys
import logging
import structlog


def init_logger():
    logging.basicConfig(
        format="%(message)s", stream=sys.stdout, level=logging.INFO)
    structlog.configure(
        logger_factory=structlog.stdlib.LoggerFactory())


class Logger:
    def __init__(self):
        self.logger = structlog.get_logger()

    def log(self, msg=None, log_type='info', level=0):
        msg = str(' '.ljust((level * 3))) + str(msg)

        if log_type == 'info':
            self.logger.info(msg)
        else:
            self.logger.info(msg)
