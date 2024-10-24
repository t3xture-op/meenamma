import discord
from BotToken import *
from discord.ext import commands
from discord import app_commands
from discord.ext.commands import has_permissions,MissingPermissions
from discord.ui import Button,View
from discord.utils import get



guild=discord.Object(id=1267143748320624711)
ModChannel=1274673257404170264
LogChannel=1294597383966949487
WaitingChannel=1296548824872910859
supportVC_1=1296721689266098187
supportVC_2=1296796806709252159
Admin=[1274694716373340233,1274694719443828847]


# class which contains buttons for support vc
class myview(View):
  @discord.ui.button(label='🔒 |│ SUPPORT VC-1',style=discord.ButtonStyle.red)
  async def vc1(self,interaction : discord.Interaction,button : Button):
    adm=interaction.user
    vc1=interaction.client.get_channel(supportVC_1)
    wait_vc=interaction.client.get_channel(WaitingChannel)
    if wait_vc and wait_vc.members:
        members_in_vc=wait_vc.members
        for members in members_in_vc:
         if  adm.voice and adm.voice.channel:
            if adm.voice.channel == wait_vc:
                await adm.move_to(vc1)
                await members.move_to(vc1)
                if not interaction.response.is_done():
                 await interaction.response.send_message(f'{members.mention} has moved to 🔒 |│ SUPPORT VC-2',ephemeral=True)

            elif  adm.voice and adm.voice.channel:
             await adm.move_to(vc1)
             await members.move_to(vc1)
             if not interaction.response.is_done():
              await interaction.response.send_message(f'{members.mention} has moved to 🔒 |│ SUPPORT VC-2',ephemeral=True)
        else:
             await members.move_to(vc1)
             if not interaction.response.is_done():
              await interaction.response.send_message(f'{members.mention} has moved to 🔒 |│ SUPPORT VC-2',ephemeral=True)

    

  @discord.ui.button(label='🔒 |│ SUPPORT VC-2',style=discord.ButtonStyle.blurple)
  async def vc2(self,interaction : discord.Interaction,button : Button):
    adm=interaction.user
    vc2=interaction.client.get_channel(supportVC_2)
    wait_vc=interaction.client.get_channel(WaitingChannel)
    if wait_vc and wait_vc.members:      
      members_in_vc=wait_vc.members
      for members in members_in_vc:
        if  adm.voice and adm.voice.channel:
            if adm.voice.channel == wait_vc:
                await adm.move_to(vc2)
                await members.move_to(vc2)
                if not interaction.response.is_done():
                 await interaction.response.send_message(f'{members.mention} has moved to 🔒 |│ SUPPORT VC-2',ephemeral=True)

            elif  adm.voice and adm.voice.channel:
             await adm.move_to(vc2)
             await members.move_to(vc2)
             if not interaction.response.is_done():
              await interaction.response.send_message(f'{members.mention} has moved to 🔒 |│ SUPPORT VC-2',ephemeral=True)
        else:
             await members.move_to(vc2)
             if not interaction.response.is_done():
              await interaction.response.send_message(f'{members.mention} has moved to 🔒 |│ SUPPORT VC-2',ephemeral=True)


# Main class
class Client(commands.Bot):
    async def on_ready(self):
        await client.change_presence(status='idle',activity=discord.Streaming(name='VALORANT',url='https://www.twitch.tv/texture_07'))
        print(f"{self.user} ready ahn sivadatheee")
        try:
           
            synced=await self.tree.sync(guild = guild)
            print(f"synced {len(synced)} commands to guild {guild.id}")
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



#on member leaving guild
    async def on_member_remove(self,user : discord.User):
        LeaveChannel=1274694860779159705
        leave_channel=client.get_channel(LeaveChannel)
        if leave_channel is None:
            await print('channel not found')
        else:
            embed=discord.Embed(title='LEAVE',description=f'{user.mention} left from our server\n **Good days ahead friend**',color=0x06e5fb)
            embed.set_author(name='MEENAKSHI',icon_url='https://cdn.discordapp.com/attachments/1041590475318104085/1294329717784313858/Designer_3.jpeg?ex=67108cbc&is=670f3b3c&hm=ac0021d33c7f950a32891ac2e317cdddf27818bbe7b844e46da460ae73ed3c51&')
            embed.set_thumbnail(url=user.avatar.url)
            embed.set_footer(text="Good Bye")
            await leave_channel.send(embed=embed)




    # Words detecting
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content == 'hai':
            await message.channel.send(f"Hello  {message.author.mention}, sukhamano 😚")
        elif message.content == 'hi':
            await message.channel.send(f"Hello  {message.author.mention}, kandathil santhosham")
        elif message.content.startswith('hello'):
            await message.channel.send(f"Hey! {message.author.mention},engane ponnu life?")
        elif 'fuck' in message.content:
            await message.delete()
            await message.channel.send(f"{message.author.mention}  ni shookshicho ente cherukkan kindum ninne")




  # voice channel codes
    async def on_voice_state_update(self,member : discord.Member,before,after):
      waiting_vc=client.get_channel(WaitingChannel)
      mod_channel=client.get_channel(ModChannel)
      room_join=client.get_channel(1298702896287842324)
      category=1297946320505405493 
      temp_voice_channels=[]
      if before.channel!= waiting_vc and after.channel == waiting_vc: #waiting vc
        if any(role.id in Admin for role in member.roles):
         return
        elif ModChannel is not None:
            View=myview()
            embed=discord.Embed(title='**SUPPORT**',description='Thank you for contacting suppoort.Our staffs have been notified.Kindly wait until they arrive',color=0x18f1a2)
            embed.set_author(name='MEENAKSHI',icon_url='https://cdn.discordapp.com/attachments/1041590475318104085/1294329717784313858/Designer_3.jpeg?ex=67108cbc&is=670f3b3c&hm=ac0021d33c7f950a32891ac2e317cdddf27818bbe7b844e46da460ae73ed3c51&')
            embed.set_footer(text='Supoort Team')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/1267463145509884034/1297063562220404756/66cd8567624cffc5d6b838dd.gif?ex=67149013&is=67133e93&hm=98795ac7de12eac645508a9ccb898da2076f0844d9f2e266e8deb5e7b0c243cf&')
            await member.send(embed=embed)
            await mod_channel.send(f'\n\n⚠️**ATTENTION**⚠️\n\n{member.mention} has joined waiting vc,need your support @everyone\n \n' ,view=View)
      
      
      if before.channel!= room_join and after.channel == room_join:  #private rooms
         room_category=client.get_channel(category)
         temp_voice_channel = await member.guild.create_voice_channel(name=f'{member.name} room',category=room_category,bitrate=64000)
         await member.move_to(temp_voice_channel)
         overwrite=temp_voice_channel.overwrites_for(member)
         overwrite.view_channel=True
         await temp_voice_channel.set_permissions(member,overwrite=overwrite)
         for role in member.roles:
            if role.permissions.administrator:
                return
            else:
                overwrite_role=temp_voice_channel.overwrites_for(role)
                overwrite_role.view_channel=False
                await temp_voice_channel.set_permissions(role,overwrite=overwrite_role)
         
         
      room_category=client.get_channel(category)
      temp_voice_channels=room_category.voice_channels
      for voicechannels in temp_voice_channels:
       if voicechannels == room_join:
         continue

      if before.channel == voicechannels and after.channel!= voicechannels:
         if len(voicechannels.members)== 0:   
          await  voicechannels.delete()



    # Cannot use commands error(not have permission) 
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
intents.voice_states=True
client = Client(command_prefix='!',intents = intents)



Guild_Id=discord.Object(id=1267143748320624711)



# join a voice channel
@client.tree.command(name='join',description='the bot will join in your voice channel',guild=Guild_Id)
@app_commands.default_permissions(move_members =True)
async def join(interaction:discord.Interaction,user: discord.Member):
     if user.voice:
        channel=user.voice.channel
        await channel.connect()
        await interaction.response.send_message("I have been connected",ephemeral=True)
     else:
        await interaction.response.send_message("You are not in a voice channel,you must be in a voice channel to use this command",ephemeral=True)




#leave leave a voice channel
@client.tree.command(name='leave',description='the bot will left its current voice channel',guild=Guild_Id)
@app_commands.default_permissions(move_members =True)
async def leave(interaction : discord.Interaction):
    voice_client= interaction.guild.voice_client
    if voice_client and voice_client.is_connected():
        await voice_client.disconnect()
        await interaction.response.send_message("I have been disconnected",ephemeral=True)
    else:
        await interaction.response.send_message("I am not in a voice channel",ephemeral=True)




#kick a user from server
@client.tree.command(name="kick",description="to kick a member from the server",guild=Guild_Id)
@app_commands.default_permissions(administrator =True)
async def   kick_memb(interaction : discord.Interaction,member: discord.Member,reason : str):
      await member.kick(reason=reason)
      await interaction.response.send_message(f"the user {member.mention} has been kicked from the server",ephemeral=True)





# Ban a user from the server
@client.tree.command(name='ban',description='to ban members from server',guild=Guild_Id)
@app_commands.default_permissions(administrator =True)
async def ban(interaction : discord.Interaction,user : discord.Member,reason : str):
    await user.ban(reason=reason)
    await interaction.response.send_message(f"The user {user.mention} has been banned from this server",ephemeral=True)
    



# Unban a user from the server
@client.tree.command(name='unban',description='to ban members from server',guild=Guild_Id)
@app_commands.default_permissions(administrator =True)
async def unban(interaction : discord.Interaction,user : discord.User,reason : str):
    try:
      guild=interaction.guild
      banned_users=guild.bans()
      async for ban_entry in banned_users:
        if ban_entry.user == user:
         await guild.unban(user,reason=reason)
         await interaction.response.send_message(f"{user.mention} ban has been revoked",ephemeral=True)
         return
        else:
         await interaction.response.send_message( f"{user.mention} has not banned",ephemeral=True)
    except Exception as e:
        await client.get_channel(LogChannel).send(e)




# sents a DM message to the user
@client.tree.command(name='dm',description='sends a message to the users dm',guild=Guild_Id)
@app_commands.default_permissions(administrator =True)
async def dm(interaction : discord.Interaction,user : discord.Member,message : str):
    await user.send(message)
    if dm:
     await interaction.response.send_message("DM message has sent successfully",ephemeral=True)
    else:
        await interaction.response.send_message("DM message cannot sent",ephemeral=True)


# send a messag ein a channel

@client.tree.command(name='send',description='sends a message in a text channel',guild=Guild_Id)
@app_commands.default_permissions(administrator =True)
async def  send(interaction : discord. Interaction,content : str,channel : discord.TextChannel):
     await channel.send( content)
     await interaction.response.send_message('message sent successfully',ephemeral=True)
    


#locks a channel
@client.tree.command(name='lock',description='lock a specific channel',guild=Guild_Id)
@app_commands.default_permissions(administrator=True)
async def lock_channel(interaction : discord.Interaction,channel : discord.TextChannel):
    for role in interaction.guild.roles:
        if role.permissions.administrator:
            continue
        else:
            overwrite= channel.overwrites_for(role)
            overwrite.send_messages=False
            await channel.set_permissions(role,overwrite=overwrite)

    await interaction.response.send_message("Channel has been locked")



#unlocks a channel
@client.tree.command(name='unlock', description='Unlocks a locked text channel', guild=Guild_Id)
@app_commands.default_permissions(administrator=True)
async def unlock_channel(interaction: discord.Interaction, channel: discord.TextChannel):
    is_locked =False
    for roles in interaction.guild.roles:
        if roles.permissions.administrator:
            continue
        else:
            overwrite = channel.overwrites_for(roles)
            if overwrite.send_messages is False:
                is_locked = True
                overwrite.send_messages=True
                await channel.set_permissions(roles, overwrite=overwrite)
            
    
    
    if is_locked:
        await interaction.response.send_message("Channel has unlocked")
    else:
         await interaction.response.send_message("Channel is not locked")

                




client.run(token())

