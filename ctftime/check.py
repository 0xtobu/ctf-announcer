import logging
import os
import json

logger = logging.getLogger(__name__)

def api():
    '''
    checks if the API keys has been setup
    :return: True if they have been configured
    '''

    if os.path.isfile('data/api.json'):
        with open('data/api.json') as file:
            data = json.load(file)

            if data['api_key'] and data['channel_id']:
                logger.info('api is set return True')
                return True

            else:
                logger.warning('could not load keys')
                return False


    else:
        logger.warning('file not found')
        return False

def data():
    '''
    this function checks if there are any data in data.json
    and verifies that it is json.
    :return: True if data is ok
    '''


    if os.path.isfile('data/data.json'):
        with open('data/data.json') as file:
            try:
                json.load(file)
                logger.info('is valid json')
                return True

            except:
                logger.warning('file is not json')
                return False
    else:
        logger.warning('Could not find data.json')
        return False


