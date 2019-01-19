import discord
import requests
import json
import hashlib
import os
import asyncio
import time

__version__= "0.0.2"
TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
CHANNEL = str('XXXXXXXXXXX')
client = discord.Client()

# ctf_time api parser
class ctf_time:

    def get_data():
        # Gets the data from CTFtime and save the json in a variable
        global raw_data

        url = 'https://ctftime.org/api/v1/events/?limit=1'
        headers = {'user-agent': 'discordbot/0.0.2'}

        Get_request = requests.get(url, headers=headers)
        raw_data = json.loads(Get_request.text)

        return raw_data

    def update_data():
        # updates data.json with new value from raw_data
        if os.path.isfile('data.json') == True:
            with open('data.json', 'w+') as outfile:
                ctf_time.sign_data(raw_data)
                outfile.write(json.dumps(raw_data, indent=4))

        else:
            with open('data.json', 'w') as outfile:
                outfile.write(json.dumps(raw_data, indent=4))
                outfile.close()

    def sign_data(ToBeHashedJson):
        # Creates a file with a hash of the json
        hashed = ctf_time.get_hash(ToBeHashedJson)
        with open('data.json.hash', 'w') as outfile:
            print('signed with {}'.format(hashed))
            outfile.write(hashed)
            outfile.close()

    def get_hash(ofthis):
        # take one argument and return that object as a string of sha256
        return hashlib.sha256(str(ofthis).encode()).hexdigest()

    def check_id():
        # checks the id in the json file and compare it with eachother, if they are the same, it will return true
        with open('data.json') as current_data:
            try:
                data = json.load(current_data)

                if str(data[0]['id']) == str(raw_data[0]['id']):
                    return True
            except:
                return False

    def Message(message):
        # Opens the json file and queries the input and return the value
        f = open('data.json', 'r')
        data = json.load(f)

        if message == 'title':
            title = str(data[0]['title'])
            return str(title)

        elif message == 'start':
            date = str(data[0]['start'])
            return str(date)

        elif message == 'url':
            url = str(data[0]['ctftime_url'])
            return str(url)

        elif message == 'type':
            type = str(data[0]['description'])
            return type

        return str('wtf, this is a bug')

@client.event
async def main():

    # main loop of program, wait for bot to come online
    await client.wait_until_ready()

    # Creates a loop so the event does not close
    while not client.is_closed:

        await asyncio.sleep(5)

        # checks if false, if so it will print a message to discord else it will sleep for 1 hour
        if ctf_time.check_id() == False:
            await client.change_presence(game=discord.Game(name='omgomg, new event!'))
            ctf_time.update_data()

            embed = discord.Embed(title="New CTF event!", color=0x00ff00)
            embed.add_field(name="Name", value=str(ctf_time.Message('title')), inline=False)
            embed.add_field(name="CTF type", value=str(ctf_time.Message('type')), inline=False)
            embed.add_field(name="Starts", value=str(ctf_time.Message('start')), inline=False)
            embed.add_field(name="URL", value=str(ctf_time.Message('url')), inline=False)
            await client.send_message(discord.Object(id=CHANNEL), embed=embed)


        # sleeps for an hour
        elif ctf_time.check_id() == True:
            await client.change_presence(game=discord.Game(name='ZZZzzZzzzZZzzz'))
            asyncio.sleep(3600)
            pass

@client.event
async def on_ready():
    # Inform the user that the bot is online
    print('Bot is online!')
    await client.change_presence(game=discord.Game(name='starting!'))

    # updates to be sure there's data
    ctf_time.update_data()

    # prints out the last message that are in the json file
    embed = discord.Embed(title="New CTF event!", color=0x00ff00)
    embed.add_field(name="Name", value=str(ctf_time.Message('title')), inline=False)
    embed.add_field(name="CTF type", value=str(ctf_time.Message('type')), inline=False)
    embed.add_field(name="Starts", value=str(ctf_time.Message('start')), inline=False)
    embed.add_field(name="URL", value=str(ctf_time.Message('url')), inline=False)
    await client.send_message(discord.Object(id=CHANNEL), embed=embed)




ctf_time.get_data()
time.sleep(10)
client.loop.create_task(main())
client.run(TOKEN)
