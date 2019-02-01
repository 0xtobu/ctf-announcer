import logging
logging.basicConfig(filename='./data/log.txt', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

logger = logging.getLogger(__name__)
logger.info('started')