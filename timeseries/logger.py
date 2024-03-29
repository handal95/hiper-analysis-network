import logging.config
import structlog

timestamper = structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S")
pre_chain = [structlog.stdlib.add_log_level, timestamper]


class Logger:
    def __init__(self, file):
        self.init_config(file)
        self.logger = logging.getLogger(file)

    def init_config(self, file):
        logfile = file.replace(".py", "")
        logfile = logfile.split(".")[-1]

        logging.config.dictConfig(
            {
                "version": 1,
                "disable_existing_loggers": False,
                "formatters": {
                    "plain": {
                        "()": structlog.stdlib.ProcessorFormatter,
                        "processor": structlog.dev.ConsoleRenderer(colors=False),
                        "foreign_pre_chain": pre_chain,
                    },
                    "colored": {
                        "()": structlog.stdlib.ProcessorFormatter,
                        "processor": structlog.dev.ConsoleRenderer(colors=True),
                        "foreign_pre_chain": pre_chain,
                    },
                },
                "handlers": {
                    "default": {
                        "level": "INFO",
                        "class": "logging.StreamHandler",
                        "formatter": "colored",
                    },
                    "file": {
                        "level": "INFO",
                        "class": "logging.handlers.RotatingFileHandler",
                        "filename": "logs/core.log",
                        "formatter": "plain",
                        "backupCount": 20,
                    },
                },
                "loggers": {
                    "": {
                        "handlers": ["default", "file"],
                        "level": "INFO",
                        "propagate": True,
                    }
                },
            }
        )

    def info(self, message):
        return self.logger.info(message)

    def warn(self, message):
        return self.logger.warning(message)
