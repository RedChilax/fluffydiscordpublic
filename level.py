import discord
import json
import os
import time
import operator
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure 
from PIL import Image , ImageDraw , ImageFont
from collections import OrderedDict
from discord import User

os.chdir(".")
class CogLevel(commands.Cog):
    def __init__(self , bot):
        self.bot = bot
    
    @commands.command() 
    async def rank(self , ctx , user :User=None) :
        if(str(ctx.channel.id) == "770999486310383646") :
            if user is None :
                await self.generate_template(ctx , ctx.message.author)
            else :
                await self.generate_template(ctx , user)
        else :
            await ctx.send("Tu es con ou tu fait exprès ? ")
                


    @commands.Cog.listener()
    async def on_member_join(self , member):
        with open('../database/user.json', 'r') as f:
            users = json.load(f)

        await self.update_data(users , member)

        with open('../database/user.json', 'w') as f:
            json.dump(users , f)


    @commands.Cog.listener()
    async def on_message(self , message):
        with open('../database/user.json', 'r') as f:
            users = json.load(f)

        await self.update_data(users , message.author)
        await self.add_experience(users , message.author , 10 , message.channel)
        await self.level_up(users , message.author , message.channel)

        with open('../database/user.json', 'w') as f:
            json.dump(users , f , sort_keys=True , indent=4 , ensure_ascii=False)
        

    
        
        
    async def generate_template(self , ctx , user):
        with open('../database/user.json', 'r') as f:
            users = json.load(f)
            
        await self.update_data(users , ctx.message.author)
            
        im = Image.open("template/template.png")
        im = im.resize((350,90),Image.ANTIALIAS)
        fnt = ImageFont.truetype('fonts/AldotheApache.ttf', 13)
        fnt2 = ImageFont.truetype('fonts/big_noodle_titling.ttf', 19)
        fnt3 = ImageFont.truetype('fonts/AldotheApache.ttf', 30)
        fnt4 = ImageFont.truetype('fonts/AldotheApache.ttf', 15)
        d = ImageDraw.Draw(im)

        experience = users[str(user.id)]['experience']
        lvl_start = users[str(user.id)]['level']
        lvl_end = experience ** (1/4)
        add = ((232)*(lvl_end - int(lvl_end))) 
        print(lvl_end - int(lvl_end))
        pourcentage = int((lvl_end - int(lvl_end))*100)

        d.rectangle((93 , 68 , 325 , 72), fill=(150,150,150), outline=None)
        d.rectangle((93 , 68 , 93+add , 72), fill=(150,255,150), outline=None)
            
            
        sorted_users = OrderedDict(sorted(users.items(), key=lambda x:int(x[1]['experience']) , reverse=True)) 
        rank = list(sorted_users).index(str(user.id))
            


        lev = ("Level : "+ str(users[str(user.id)]["level"])) 
        username , ids = str(user).split("#")
        await user.avatar_url.save("temp/pp.webp")

        

            
        img2 = Image.open("temp/pp.webp")
        img2 = img2.resize((65,65), Image.ANTIALIAS)
        size = (13 ,  11)
            
        d.text((94,50), lev, font=fnt ,fill=(255,255,255))
        d.text((93,13), username.lower().capitalize()[:32]+"#"+ids, font=fnt2 ,fill=(255,255,255))
        d.text((285,13), "#"+str(rank+1), font=fnt3 ,fill=(220,220,220))
        d.text((300,50), str(pourcentage)+"%", font=fnt4 ,fill=(220,220,220))
        im.paste(img2 , size)
        im.save("temp/temp.png")
        with open('temp/temp.png' , 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=discord.File('temp/temp.png'))
    

    async def update_data(self , users , user):
        if not str(user.id) in users:
            users[str(user.id)] = {}
            users[str(user.id)]['experience'] = 5
            users[str(user.id)]['level'] = 1
            users[str(user.id)]['time'] = time.time()

    async def add_experience(self , users , user , exp , channel ):
        if(((time.time() - users[str(user.id)]['time']) >= 20 ) and user.id != 772477764430594078 and user.id != 235088799074484224 and user.id != 640030784023166987 and channel.id != 770996439454318614 and channel.id != 770999486310383646):
            users[str(user.id)]['experience'] += exp
            users[str(user.id)]['time'] = time.time()
        

    async def level_up(self , users , user , channel):
        experience = users[str(user.id)]['experience']
        lvl_start = users[str(user.id)]['level']
        lvl_end = int(experience ** (1/4))

        if lvl_start < lvl_end:
            await channel.send('{} c\'est bien tu as level up au niveau {} btr '.format(user.mention , lvl_end))
            users[str(user.id)]['level'] += 1
        if(int(users[str(user.id)]['level']) == 2):
            role = 'Kikou'
            await user.add_roles(discord.utils.get(user.guild.roles , name=role))
        if(int(users[str(user.id)]['level']) == 10):
            role = 'Charbon Tier'
            await user.add_roles(discord.utils.get(user.guild.roles , name=role))
        if(int(users[str(user.id)]['level']) == 25):
            role = 'Fer Tier'
            await user.add_roles(discord.utils.get(user.guild.roles , name=role))
        if(int(users[str(user.id)]['level']) == 40):
            role = 'Redstone Tier'
            await user.add_roles(discord.utils.get(user.guild.roles , name=role))
        if(int(users[str(user.id)]['level']) == 50):
            role = 'Gold Tier'
            await user.add_roles(discord.utils.get(user.guild.roles , name=role))
        if(int(users[str(user.id)]['level']) == 60):
            role = 'Diamond Tier'
            await user.add_roles(discord.utils.get(user.guild.roles , name=role))
        