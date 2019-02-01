import json
import logging
import os

logger = logging.getLogger(__name__)

def check():
    '''
    check if there is a api.json
    :return: bolean
    '''
    logger.info('checking if true or false')

    if os.path.isfile('data/api.json'):
        logger.info('file found its true')
        return True

    else:
        logger.info('file not found')
        return False


def api(api_key, channel_id, admin_user):
    '''
    :param api_key: API key for the bot to connect to
    :param channel_id: what channel the bot shall send message's in
    :return:
    '''

    logger.info('setting API keys')
    data = {}
    try:
        data['api_key'] = api_key
        data['channel_id'] = channel_id
        data['admin_user'] = admin_user

        logger.info('got API keys')
        with open('data/api.json','w') as k:
            logger.info('attempting to write api keys to file')
            json.dump(data, k)

            logger.info('Success return True')
            return True
    except:

        logger.warning('something happened')
        return False