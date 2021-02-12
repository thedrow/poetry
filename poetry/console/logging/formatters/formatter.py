import logging


class Formatter:
    def format(self, record):  # type: (logging.LogRecord) -> str
        raise NotImplementedError()
