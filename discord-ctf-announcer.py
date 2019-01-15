import discord
import requests
import json
import hashlib

__version__= "0.0.1"
TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
CHANNEL = str('YYYYYYYYYYYYYYYYYYYY')
client = discord.Client()

'''make the bots life easier'''
class ctf_time:

    def Fetch_data():
        '''Gets data from ctftime'''

        url = 'https://ctftime.org/api/v1/events/?limit=1'
        headers = {'user-agent': 'discordbot/0.0.1'}

        Get_request = requests.get(url, headers=headers)
        data = json.loads(Get_request.text)

        with open('data.json', 'w') as outfile:
            outfile.write(json.dumps(data, indent=4))
            outfile.close()


        if ctf_time.Is_new() == True:
            print('it worked')

        # '''if its not true, it will update the hash and send'''
        else:

            with open('data.json.hash', 'w') as outfile:
                file = open('data.json')
                ToBeHashed = file.read()
                outfile.write(hashlib.sha256(ToBeHashed.encode()).hexdigest())


    def Is_new():
        '''Checks if the file has been updated'''

        with open('data.json.hash','r') as outfile:
            file = open('data.json')
            ToBeHashedJson = file.read()
            file.close()

        with open('data.json','r') as outfile:
            file = open('data.json')
            ToBeHashedHash = file.read()
            file.close()

        json_hash = hashlib.sha256(ToBeHashedJson.encode()).hexdigest()
        data_hash = hashlib.sha256(ToBeHashedHash.encode()).hexdigest()
        # print("First hash " +json_hash)
        # print("Second hash "+ data_hash)

        '''checks if the hashfile and the hash are the same and return true'''
        if json_hash == data_hash:
            return True

        else:
            return False


    def Message():
        f = open('data.json', 'r')
        data = json.load(f)
        print(data[0]['id'])
        announcement =  str(data[0]['title'])
        time = str(data[0]['start'])
        '''String that the bots prints out'''
        return str("**{0}** {1}" .format(announcement, time))

@client.event
async def on_message(message):

    '''Ensure's that the bots does not send things to itself'''
    if message.author == client.user:
        return

    '''Checks if  is new is false, sends the message to the channel'''
    if ctf_time.Is_new() == False:
        await client.send_message(discord.Object(id='534286729817882624'), ctf_time.Message())

@client.event
async def on_ready():
    print('Bot is running.')

'''runs the bot'''
client.run(TOKEN)
