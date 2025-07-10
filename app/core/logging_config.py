import logging, sys
from pythonjsonlogger import jsonlogger

def init_logging(level: str = "INFO"):
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(jsonlogger.JsonFormatter())
    logging.basicConfig(level=level, handlers=[handler])
