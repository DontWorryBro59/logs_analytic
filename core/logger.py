import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
    ]
)

# Готовый к использованию логгер
logger = logging.getLogger(__name__)


def get_logger(name):
    return logging.getLogger(name)
