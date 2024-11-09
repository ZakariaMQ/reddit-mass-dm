import colorlog
import logging

log_colors = {
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}

formatter = colorlog.ColoredFormatter(
    fmt='[%(asctime)s] | %(log_color)s%(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors=log_colors
)

logger = logging.getLogger("RumbleBot")
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

httpx_logger = logging.getLogger("httpx")
httpx_logger.setLevel(logging.WARNING)