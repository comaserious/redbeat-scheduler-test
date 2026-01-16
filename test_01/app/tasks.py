# app/tasks.py
import random
from app.celery_app import celery_app

import logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

@celery_app.task(name="tasks.add_random_numbers")
def add_random_numbers():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    result = a + b
    logger.info(f"[TASK] {a} + {b} = {result}")
    return result
