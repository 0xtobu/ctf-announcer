import discord
import logging

logger = logging.getLogger(__name__)

class message:

    def set(raw_data):
        '''
        takes raw json input and return finished formated message.
        :param raw_data: json input
        :return: discord.embed object
        '''

        try:
            embed = discord.Embed(title=str(raw_data['title']), description=str(raw_data['description']), color=0x00ff00)
            embed.set_thumbnail(url=str(raw_data['logo']))
            embed.add_field(name='CTF-time link', value=str(raw_data['ctftime_url']), inline=True)
            embed.add_field(name='URL', value=str(raw_data['url']), inline=True)
            embed.add_field(name='Start', value=str(raw_data['start']), inline=True)
            embed.add_field(name='End', value=str(raw_data['finish']), inline=True)
            embed.add_field(name='Duration', value=str("Days: {0} Hours: {1}".format(raw_data['duration']['days'],raw_data['duration']['hours'])), inline=True)

            logger.info('parsed json, returning embed')
            return embed

        except:
            logger.warning('Could not parse json to embed')