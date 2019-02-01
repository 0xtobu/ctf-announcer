from ctftime import setup
from ctftime import check
from ctftime import update_data
from ctftime import send
from ctftime import get_data
import json
import discord
from discord.ext import commands
import asyncio


if check.api() == False:
    setup.api(input('API key: '), input('CHANNEL ID: '),input('ADMIN_USER ID: '))

    update_data
    file = open('data/api.json', 'r')
    settings = json.load(file)
    TOKEN = settings['api_key']
    CHANNEL = settings['channel_id']
    ADMIN = settings['admin_user']

    data = get_data.current()
    client = commands.Bot(command_prefix='/')

else:
    file = open('data/api.json', 'r')
    settings = json.load(file)
    TOKEN = settings['api_key']
    CHANNEL = settings['channel_id']
    ADMIN = settings['admin_user']

    client = commands.Bot(command_prefix='/')
    data = get_data.current()


@client.event
async def on_message(message):
    reactions = ['✅', '❌']

    if message.author.id == ADMIN:
        await client.process_commands(message)

    elif message.author == client.user:
        for reaction in reactions:
            await asyncio.sleep(1)
            await client.add_reaction(message, reaction)

@client.event
async def main():
    while not client.is_closed:
        client.send_message(discord.Object(id=CHANNEL), 'doing check')
        print(get_data.check(get_data.new()))
        print(get_data.check(get_data.current()))

        if get_data.check(get_data.new()) == get_data.check(get_data.current()):
            update_data
            await asyncio.sleep(1000)

        else:

            data = get_data.current()
            msg = send.message.set(data[0])
            await client.send_message(discord.Object(id=CHANNEL), embed=msg)
            await asyncio.sleep(1000)


@client.command()
async def overwrite():

    for i in data:
        msg = send.message.set(i)
        await client.say(embed=msg)

@client.command()
async def ping():
    print('ping')
    message = 'ping pong'
    await client.say(message)
    await asyncio.sleep(2)


@client.command()
async def start():

    client.loop.create_task(main())
    await asyncio.sleep(2)


@client.command(pass_context=True)
async def clear(ctx, amount=4):
    channel = ctx.message.channel
    messages = []

    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)

    await client.delete_messages(messages)



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
