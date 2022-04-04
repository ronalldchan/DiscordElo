# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import asyncio
import discord
from discord.ext import commands
from JsonReadWrite import *

token = ''
confirmation_emote = '👍'
client = commands.Bot(command_prefix='.')
default_timeout = 60


def red_message(message: str):
    return discord.Embed(description=message, colour=discord.Colour.red())


def blue_message(message: str):
    return discord.Embed(description=message, colour=discord.Colour.blue())


def green_message(message: str):
    discord.Embed(description=message, colour=discord.Colour.green())


@client.event
async def on_ready():
    print('Bot is ready')


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@client.command()
async def leaderboard(ctx):
    embed = discord.Embed(title='Top 3 Players',
                          colour=discord.Colour.blue())
    player_list = read_file('elo_player_data.json')
    sorted_list = sorted(player_list, key=lambda p: p.rating, reverse=True)
    count = 1
    for x in sorted_list:
        name = await client.fetch_user(x.user_id)
        embed.add_field(name=f'{count}. {name}',
                        value=f'Rating: {x.rating}\nWins: {x.wins}\nLosses: {x.losses}',
                        inline=False)
        count += 1
    await ctx.send(embed=embed)


@client.command()
async def match(ctx, player1: discord.User, player2: discord.User, draw: bool = False):
    if player1 == player2:
        player_error_msg = red_message('Cannot have a match against the same player')
        return await ctx.send(embed=player_error_msg)
    else:
        try:
            confirmation_embed = blue_message(f'Waiting for confirmation from players. React with {confirmation_emote} to confirm')
            confirmation_msg = await ctx.send(embed=confirmation_embed)
            await confirmation_msg.add_reaction(confirmation_emote)
            players = {player1.id, player2.id}

            def check(reaction, user):
                if user.id in players and str(reaction) == confirmation_emote:
                    players.remove(user.id)
                    return len(players) == 0
                return False

            await client.wait_for('reaction_add', timeout=default_timeout, check=check)
            player_list = read_players()
            player1_data = get_player_from_list(player_list, player1.id)
            player2_data = get_player_from_list(player_list, player2.id)

            (player1_diff, player2_diff) = player_match_difference(player1_data, player2_data, draw)
            player_match(player1_data, player2_data, draw)
            if draw:
                player1_status = player2_status = 'Draw'
            else:
                player1_status = "Winner"
                player2_status = "Loser"

            embed = discord.Embed(title="Match Result", colour=discord.Colour.green())
            embed.add_field(name=str(player1), value=f'{player1_status}\n'
                                                     f'New Rating: {player1_data.rating} ({player1_diff})\n'
                                                     f'Wins: {player1_data.wins}\n'
                                                     f'Losses: {player1_data.losses}')
            embed.add_field(name=str(player2), value=f'{player2_status}\n'
                                                     f'New Rating: {player2_data.rating} ({player2_diff})\n'
                                                     f'Wins: {player2_data.wins}\n'
                                                     f'Losses: {player2_data.losses}')
            write_players(player_list)
            await ctx.send(embed=embed)
        except asyncio.TimeoutError:
            timeout_embed = red_message('Match canceled: Failed to get player confirmation in time')
            await confirmation_msg.edit(embed=timeout_embed)
            await confirmation_msg.clear_reaction(confirmation_emote)


@client.command()
async def stats(ctx):
    player_list = read_file('elo_player_data.json')
    player_data = get_player_from_list(player_list, ctx.message.author.id)
    player_name = ctx.message.author
    embed = discord.Embed(title=f"{player_name}'s Stats",
                          colour=discord.Colour.blue(),
                          description=f'Rating: {player_data.rating}\nWins: {player_data.wins}\nLosses: {player_data.losses}')
    await ctx.send(embed=embed)

client.run(token)
