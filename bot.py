import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure  
import random
import asyncio
import level
import json
from collections import OrderedDict
from discord.utils import get

bot = commands.Bot(command_prefix = '.'  )

async def background():
   await bot.wait_until_ready()
   channel = bot.get_channel(int(770431887206383648))
   
   while True :
        Messages = ["Wesh les pds" , "bien ou quoi || je m'en fous|| " , "ça fait quoi ici || m'en fous ||" , "vs etes chiants" , "j'en ai marre de vous" , "je vous aimes <3 ||c'est faux mdrr || ", "allez dormir" , "j'ai envie de baisez" , "Bande de puceaux" , "Saber ou rin ?" , "Fate c'est éclaté au sol" , "Frigiel jtm || c est fo ||" , "putain je me sens seul" , "minecraft ça a toujours etait un jeu de merde.." , "pourquoi j'existe :(" , "je vais devenir fou" , "laissez moi pas seul..."  ]
        if((random.randrange(0 , 10) % 10) == 0):
            await channel.send(random.choice(Messages))
        await asyncio.sleep(3600)

bot.loop.create_task(background())

@bot.event
async def on_ready():
    print('bot is ready !')

#affiche dans la console quand un membre rejoins le serveur
@bot.event
async def on_member_join(member):
    print(member,"à rejoins notre serveur !")


#affiche dans la console quand un membre quitte le serveur
@bot.event
async def on_member_remove(member):
    print(member," est partit jouer à fornite :( !")


@bot.command()
async def fluffy(ctx):
    #if(arg == "suce"):
     #   await ctx.send("je vais appeler la fbi")    
    #else:
    await ctx.send("Ta cru que je suis ton chien ou quoi fdp ")

@bot.command()
async def ip(ctx):
    await ctx.send("anilounge.starmine.pro")

@bot.command()
async def levels(ctx):
    await ctx.send("Calcul en cours veuillez patienter...")
    with open('../database/user.json' , 'r') as f:
        users = json.load(f)
    with open('../../var/www/html/levels/ranking.json' , 'r' , encoding="utf-8") as d:
        ranking = json.load(d)
    sorted_users = OrderedDict(sorted(users.items(), key=lambda x:int(x[1]['experience']) , reverse=True)) 

    for r in sorted_users :
        user = await bot.fetch_user(r)
        ranking[str(list(sorted_users).index(str(user.id)))] = {}
        ranking[str(list(sorted_users).index(str(user.id)))]['url_avatar'] = str(user.avatar_url)
        ranking[str(list(sorted_users).index(str(user.id)))]['username'] = str(user)
        ranking[str(list(sorted_users).index(str(user.id)))]['level'] = users[str(user.id)]['level']
    
    with open('../../var/www/html/levels/ranking.json', 'w' , encoding="utf-8") as f:
            json.dump(ranking , f , sort_keys=True , indent=4 , ensure_ascii=False)
    

    with open('../../var/www/html/levels/ranking.json' , 'r' ,  encoding='utf-8') as f:
        test = json.load(f)   
    

        
          
    await ctx.send("Le ranking list de Biscrew : http://vps74604.serveur-vps.net/levels/ ")


@bot.command()
async def seed(ctx):
    await ctx.send("-1264021667289678156")

@bot.command()
async def question_fluffy(ctx , * , question):    
    reponse = ["Oui !" ,  "Non." , "Exactement" , "D'accord" , "NTM" , "Fuck" , "Oui tkt", "Je pense pas" , "Casse toi" , "Sale fdp" , "Même pas en rêve" , "Mdrrr" ,"Bien sur" , "Evidemment sale con" , "jsp" , "vous me soulez" , "enfaite j'en rien a foutre" , "je vais pas te répondre" , "Ok." , "Effectivement" , "rien a foutre" , "Tu es qu'une merde" , "Laissez moi fumez ma clope ptn" , "Frigiel dit lui de fermez sa geule" , "RedChilax sale fdp tu m'a créer pour répondre a ses fdp" , "Baise ta mère" , "Tu ose me poser une question" , "Je pense que oui" , "je vais être sympa et je vais te répondre (non)" , "Comment tu peux etre aussi débile pour me poser se genre de question ptn" , "oui oui c'est ça" , "Fc ta mère" , "c'est vrai" , "oui tu as raison " , "non tu as tord fdp parle pas avec moi" , "je vous aimes UwU || enculé ne te touche pas la nouille ||" , "ouer c'est faux" , "Yes Yes Yes" , "ftgl" , "Okay" , "t chelou mon reuf" , "mon reuf t srx" , "t srx ?" , "oh ptn" , "je sais pas de quoi penser de votre discussion de merde " , "sortez dehors à la place de me poser des questions débiles" , "Tu es trop intéligent toi" , "c'est ptet pas faux mais je vais ntm quand même" , "oh la la ptn tu as pas d'autre question genre" , "Oui <3" , "Je vous aimes <3" , "C'est Noel !!!!!" , "Je vous souhaite le bonheur" , "Oui tkt et je crois en toi" , "Je te fait confiance et je vais dire oui" , "<3" , "Non mais tu mérite tout mon amour" , "Oui oui c'est ca , Crois en toi !" , "Osef des questions mais je t'aime quand même <3" , "non , mais de fait de ton mieux ! ","Peace nd lové <3 " , "Bande de gay bloqué" , "Sucez des bites putain ça va vous détendre" , "Ton père le chauve" , "Les animés vous en baisez le cerveau " , "bande de weeb puceau" , "suce moi la queu sale lolicon" , "Sale lolicon  , plus lolicon que qqun dans ce serveur" , "Tu te crois marrant fdp" , "vas faire du sport gros lard" , "sale pd (j'aime les bites)" , "-8 de qi" , "c'est incroyable putain" , "Sale idiot" ]
    await ctx.send(f"Question: {question} \nRéponse:"+random.choice(reponse))

#pour kick
@bot.command()
@has_permissions(administrator=True, manage_messages=True, manage_roles=True)
async def kick(ctx , member : discord.Member , *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(str(member)+" est parti joué à fornite :( ")

#pour ban
@bot.command()
@has_permissions(administrator=True, manage_messages=True, manage_roles=True)
async def ban(ctx , member : discord.Member , *, reason=None):
    await member.ban(reason=reason)


bot.add_cog(level.CogLevel(bot))
#PrivateToken
bot.run('')
