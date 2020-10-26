import logging
import logging.config

logging.config.fileConfig("logging.conf")

logger = logging.getLogger(__name__)
logger.warning("this is a debug message")


