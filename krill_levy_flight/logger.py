import logging
import sys

__all__ = ("logger",)

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format="[%(asctime)s] [%(levelname)8s]:  %(message)s",
)

logger = logging.getLogger(__name__)
