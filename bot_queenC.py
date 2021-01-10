# bot.py
import os
import re
import discord
import csv
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#DISCORD_GUILD=os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_message(message):

    if message.author==client.user:
        return

    if message.author.bot:
        return

    message_norm = message.content.lower()
    if 'dis queenc' in message_norm or 'dis queen c' in message_norm:
        cours_abbrev={"é":"e","lexico":"lexicologie", "stats":"statistiques","model":"modelisation","fouilles":"fouilles de textes", "cnn": "reseaux de neurones", "calcul":"calculabilite", "docs struct" : "documents structures", "xml": "documents structures","python":"langages de script"}
        cours=["lexicologie", "statistiques","modelisation","documents structures", "fouilles de texte", "langages de script", "java", "calculabilite", "reseaux de neurones", "semantique"]
        matiere_concerne = []
        for abbreviation in cours_abbrev:
            message_norm = re.sub(rf'\b{abbreviation}\b',f' {cours_abbrev[abbreviation]}', message_norm)
        for cour in cours:
            if cour in message_norm:
                matiere_concerne.append(cour)
        if len(matiere_concerne) == 0:
            await message.channel.send(f"Je n'ai pas compris sur quel cours porte votre question...")
        elif len(matiere_concerne) != 1:
            await message.channel.send(f"Il y a ambiguité, votre question porte-t-elle sur : {' ou '.join(matiere_concerne)} ? Merci de reformuler sans ambiguités parce que je suis un peu con")
        else:
            cours = matiere_concerne[0]
            infos = []
            if "partiel" in message_norm or "exam" in message_norm or "test" in message_norm:
                infos.append("partiel")
            if "projet" in message_norm:
                infos.append("projet")
            if "devoir" in message_norm:
                infos.append("devoir")

            if len(infos)==0:
                await message.channel.send(f"Votre question semble porter sur le cours : {cours}, mais quelle est la question exactement ? Devoir, partiel, projet ? J'ai pas compris...")
            elif len(infos)>1:
                await message.channel.send(f"Il y a ambiguité, votre question porte-t-elle sur : {' ou '.join(infos)} ? Merci de reformuler sans ambiguités parce que je suis un peu con")
            else:
                info = infos[0]
                with open('infos_im.csv') as csvfile:
                    reader = csv.DictReader(csvfile, delimiter=';',quotechar='"')
                    for row in reader:
                        if row['matiere'] == cours:
                            if row[info+'_contenu']=="None" and row[info+'_date']=="None":
                                await message.channel.send(f"Il n'y a pas de {info} pour le cours {cours}")
                            elif "quand" in message_norm or "date" in message_norm or "deadline" in message_norm:
                                if row[info+'_date'] != "":
                                    await message.channel.send(f"Pour le cours : {cours}, la date/deadline de {info} est : {row[info+'_date']}")
                                else:
                                    await message.channel.send(f"Je n'ai pas encore l'info concernant la date/deadline du {info} de {cours}, désolée :(")
                            elif "quoi" in message_norm or "consigne" in message_norm or "contenu" in message_norm:
                                if row[info+'_contenu'] != "":
                                    await message.channel.send(f"Pour le cours : {cours}, le contenu/consigne de {info} est :\n {row[info+'_contenu']}")
                                else:
                                    await message.channel.send(f"Je n'ai pas encore l'info concernant la consigne/le contenu du {info} de {cours}, désolée :(")
                            else:
                                if row[info+'_contenu'] == "None" and row[info+'_date'] == "None":
                                    await message.channel.send(f"Il n'y a pas de {info} pour le cours de {cours}.")
                                elif row[info+'_contenu'] != "" or row[info+'_date'] != "":
                                    await message.channel.send(f"Pour le cours : {cours}, le contenu/consigne de {info} est : \n{row[info+'_contenu']} \n--- la date/deadline est {row[info+'_date']}")
                                else:
                                    await message.channel.send(f"Je n'ai pas encore toutes les infos, essayez peut-être une requête plus précise ? (sur la date/deadline ou le contenu/consigne)")
client.run(TOKEN)
