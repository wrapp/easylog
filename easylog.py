import logging
import sys


class IsError(logging.Filter):
    def filter(self, rec):
        return rec.levelno == logging.ERROR

class IsNotError(logging.Filter):
    def filter(self, rec):
        return rec.levelno != logging.ERROR


def configure_logger(logger):
    ''' Makes ERROR go to stderr and everything else to stdout. '''
    err = logging.StreamHandler(sys.stderr)
    err.setLevel(logging.ERROR)
    err.addFilter(IsError())

    out = logging.StreamHandler(sys.stdout)
    out.setLevel(logging.DEBUG)
    out.addFilter(IsNotError())

    logger.addHandler(out)
    logger.addHandler(err)
    logger.setLevel(logging.INFO)
