import discord
import os

client = discord.Client()

@client.event
async def on_ready():
   print('Logged in as')
   print(client.user.name)
   print(client.user.id)
   print('------')

@client.event
async def on_message(message):

   if message.content.startswith("!시간표"):
      embed = discord.Embed(title="시간표", color=0xffffff)
      embed.set_image(url="https://cdn.discordapp.com/attachments/859373484563628055/859714401455308810/KakaoTalk_20210622_094009324.jpg")
      # embed.add_field(name="월", value="실험\n수학\n통과\n미술\n한A\n창체\n창체", inline=True)
      # embed.add_field(name="화", value="수학\n수학\n영B\n사A\n한국\n영A\n통과", inline=True)
      # embed.add_field(name="수", value="외국\n외국\n논리\n수학\n한국\n국A\n통과", inline=True)
      # embed.add_field(name="목", value="음악\n체육\n프밍\n영A\n수학\n사A\n국B", inline=True)
      # embed.add_field(name="금", value="영A\n국A\n한국\n한B\n수학\n국B\n사B", inline=True)
      embed.set_footer(text="Hyunder#2422", icon_url="https://cdn.discordapp.com/attachments/859373484563628055/859714258252857364/KakaoTalk_20200814_135403033.png")

      await message.channel.send(embed=embed)


access_token = os.environ['BOT_TOKEN']
client.run(access_token)
