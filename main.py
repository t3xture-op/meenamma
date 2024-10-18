import discord
from BotToken import *
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import has_permissions,MissingPermissions



guild=discord.Object(id=1267143748320624711)
ModChannel=discord.Object(id=1274673257404170264)



class Client(commands.Bot):
    async def on_ready(self):
        await client.change_presence(status='idle',activity=discord.Streaming(name='VALORANT',url='https://www.twitch.tv/texture_07'))
        print(f"{self.user} ready ahn sivadatheee")
        try:
           
            synced=await self.tree.sync(guild = guild)
            print(f"synced{len(synced)} commands to guild {guild.id}")
        except Exception as e:
            print(f"Error syncing commands: {e}")



 #on member joining guild
    async def on_member_join( self,user: discord.Member):
        welchannel=1274694855037288598
        channel=client.get_channel(welchannel)
        if channel is None:
            await print("channel not found")
        else:
          embed=discord.Embed(title="WELCOME",description=f"HI {user.mention}🤍.\n WELCOME TO {user.guild.name}(❁´◡`❁)🎉\n<:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686><:D9:1278276802065862686> \n \n <a:yarrow:839825533831217162>check out <#1176551453343617065> before chatting!⚠️ \n \n <a:yarrow:839825533831217162>make use of <#1255170925528354886> for collecting your roles \n \n <a:yarrow:839825533831217162><#1252353141349945464> for text💬 \n \n <a:yarrow:839825533831217162><#1034805956611149827> for voice🔉 \n \n <a:yarrow:839825533831217162>   **TOTAL MEMBERS** :- **{user.guild.member_count}**",color=0xeef90d)
          embed.set_author(name='MEENAKSHI',icon_url='https://cdn.discordapp.com/attachments/1041590475318104085/1294329717784313858/Designer_3.jpeg?ex=67108cbc&is=670f3b3c&hm=ac0021d33c7f950a32891ac2e317cdddf27818bbe7b844e46da460ae73ed3c51&')
          embed.set_thumbnail(url=user.avatar.url)
          embed.set_image(url='https://cdn.discordapp.com/attachments/1265278107628212318/1278223785560113182/-_Find__Share_on_GIPHY.gif?ex=66d0062a&is=66ceb4aa&hm=d086877690fd2c3fc5a4b6537c3e8e4ed2a77f2dd699728b236efb3cda1ad4d4&')
          embed.set_footer(text="Enjoy your stay in the server")
          await channel.send(embed=embed)



    # Words detecting
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content == 'hai':
            await message.channel.send(f"Hello  {message.author.mention}, sukhamano 😚")
        elif message.content.startswith('hello'):
            await message.channel.send(f"Hey! {message.author.mention},engane ponnu life?")
        elif 'fuck' in message.content:
            await message.delete()
            await message.channel.send(f"{message.author.mention}  ni shookshicho ente cherukkan kindum ninne")



    # Cannot use commands(not have permission) error
    async def on_application_command_error(interaction:discord.Interaction,error : Exception):
        try:
          if isinstance(error, commands.MissingPermissions):
           await interaction.response.send_message("You need to have Administrator permissions to use this command.",ephemeral=True ) 
        except Exception as e:
            await interaction.response.send_message(f"errors are: {e}")

   
   
   
intents = discord.Intents.default()
intents.message_content = True
intents.guilds=True
intents.members=True
client = Client(command_prefix='!',intents = intents)



Guild_Id=discord.Object(id=1267143748320624711)



# join command
@client.tree.command(name='join',description='the bot will join in your voice channel',guild=Guild_Id)
@commands.has_permissions(use_application_commands=True)
async def join(interaction:discord.Interaction,user: discord.Member):
     if user.voice:
        channel=user.voice.channel
        await channel.connect()
        await interaction.response.send_message("I have been connected",ephemeral=True)
     else:
        await interaction.response.send_message("You are not in a voice channel,you must be in a voice channel to use this command",ephemeral=True)



#leave command
@client.tree.command(name='leave',description='the bot will left its current voice channel',guild=Guild_Id)
async def leave(interaction : discord.Interaction):
    voice_client= interaction.guild.voice_client
    if voice_client and voice_client.is_connected():
        await voice_client.disconnect()
        await interaction.response.send_message("I have been disconnected",ephemeral=True)
    else:
        await interaction.response.send_message("I am not in a voice channel",ephemeral=True)



#kick command
@client.tree.command(name="kick",description="to kick a member from the server",guild=Guild_Id)
async def   kick_memb(interaction : discord.Interaction,member: discord.Member,reason : str):
      await member.kick(reason=reason)
      await interaction.response.send_message(f"the user {member.mention} has been kicked from the server",ephemeral=True)




# Ban command
@client.tree.command(name='ban',description='to ban members from server',guild=Guild_Id)
async def ban(interaction : discord.Interaction,user : discord.Member,reason : str):
    await user.ban(reason=reason)
    await interaction.response.send_message(f"The user {user.mention} has been banned from this server",ephemeral=True)

# Unban command
@client.tree.command(name='unban',description='to ban members from server',guild=Guild_Id)
async def unban(interaction : discord.Interaction,user : discord.User,reason : str):
    guild=interaction.guild
    banned_users=guild.bans()
    async for ban_entry in banned_users:
        if ban_entry.user == user:
         await guild.unban(user,reason=reason)
         await interaction.response.send_message(f"{user.mention} ban has been revoked",ephemeral=True)
        else:
         await interaction.response.send_message( f"{user.mention} has not banned",ephemeral=True)



# DM command
@client.tree.command(name='dm',description='sends a message to the users dm',guild=Guild_Id)
async def dm(interaction : discord.Interaction,user : discord.Member,message : str):
    await user.send(message)
    if dm:
     await interaction.response.send_message("DM message has sent successfully",ephemeral=True)
    else:
        await interaction.response.send_message("DM message cannot sent",ephemeral=True)


client.run(token())

