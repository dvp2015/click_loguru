# -*- coding: utf-8 -*-
"""Log from another module."""

# third-party imports
from loguru import logger


def other_module_levels():
    """Log at different severity levels."""
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
