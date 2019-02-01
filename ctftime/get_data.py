import logging
import requests
import json

logger = logging.getLogger(__name__)

url = 'https://ctftime.org/api/v1/events/?limit=3'
headers = {'user-agent': 'discordbot/0.1.3'}

def new():
    logger.info('Attempting to fetch data.')

    '''
    This class fetches json from ctf-time.
    :return: json data
    '''

    try:
        Get_request = requests.get(url, headers=headers)
        json.loads(Get_request.text)
        logger.info(Get_request.status_code)

        if str(Get_request.status_code) == '200':
            logger.info('Got data.')
            raw_data = json.loads(Get_request.text)

            return raw_data

        else:
            logger.warning(Get_request.status_code)
            return

    except:
        logger.warning('Could not reach server')
        return json.dumps('{null}')

def current():

    '''
    gets the current data saved on disk
    :return: saved json data or false if data not found
    '''

    try:
        saved_data = open('data/data.json', 'r')
        data = json.load(saved_data)

        return data

    except:
        logger.warn('unable to find saved data')
        return False

def check(user_input):
    '''
    takes json userinput and returns the first orinisation ID
    :param user_input:
    :return: str of data
    '''

    try:
        data = user_input[0]['id']
        logger.info(data)
        return str(data)

    except:
        logger.warning('invalid input')
        pass



