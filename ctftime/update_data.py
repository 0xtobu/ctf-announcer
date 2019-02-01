import logging
import json
from ctftime import get_data

logger = logging.getLogger(__name__)

'''
updates data to local disk
'''

try:
    data = get_data.new()
    with open('data/data.json','w+') as file:
        file.write(json.dumps(data, indent=4))
    logger.info('Save completed')

except:
    logger.warning('Could not save data to disk')
