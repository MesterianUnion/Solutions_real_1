# import datetime
from datetime import datetime, timedelta, timezone
import json
# from datetime import datetime, timedelta
import discord
# import interaction as interaction
from discord import app_commands
from models import Base, BotAnswer, BotSession
# Sql test
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import requests
# from discord.ext import commands

# Create a Bot instance with a 120-second timeout
# bot = commands.Bot(command_prefix='/', timeout=120.0)

engine = create_engine('sqlite:///bot_database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

def get_token():
    print("Getting Token")
    with open("config.json", 'r') as file:
        data = json.load(file)
    return data["token"]

def run_discord_bot():
    token = get_token()
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    tree = app_commands.CommandTree(client)


    @tree.command(name="testcommand2", description="test 2", guild=discord.Object(id=ServerID))
    async def second_command(interaction, string: str):
        await interaction.response.send_message(string)

    @tree.command(name="jeppe", description="Spørg Jeppe: /jeppe Hvor er du? - /jeppe Er du konge? - /jeppe Du tyk", guild=discord.Object(id=ServerID))
    async def jeppe(interaction, string: str):
        responses = {
            'Hvor er du?': 'Så er kongerne lige landet på toilettet',
            'Er du konge?': 'Ja, jeg er konge',
            'Du tyk': 'Jeg er ikke tyk, jeg er bare stor',
        }
        response = responses.get(string, 'Jeg forstår ikke spørgsmålet')
        await interaction.response.send_message(response)

        # Save the command and the bot's response to the database
        session = Session()
        bot_answer = BotAnswer(answer=response, command_used=f"/{interaction.data['name']} {string}", user=interaction.user.name, timestamp=datetime.now())
        session.add(bot_answer)
        session.commit()

    @tree.command(name="hvem_er", description="Fx: /hvem_er MrMasterTop1 - /hvem_er Youtube - /hvem_er MrBeast", guild=discord.Object(id=ServerID))
    async def hvem_er(interaction, string: str):
        string = string.lower()
        from interactions_files.youtuber_info import youtuber_info  # Update the import statement
        youtuber_info = youtuber_info.get(string, f"Jeg kender desværre ikke {string} endnu. Vil du fortælle mig, hvem det er?")
        await interaction.response.send_message(youtuber_info)

        # Save the command and the bot's response to the database
        session = Session()
        bot_answer = BotAnswer(answer=youtuber_info, command_used=f"/{interaction.data['name']} {string}", user=interaction.user.name, timestamp=datetime.now())
        session.add(bot_answer)
        session.commit()

    #LANDE


    def get_country_info(country_name):
        # Offenlig API
        url = f"https://restcountries.com/v3.1/name/{country_name}"

        try:
            # Make a GET request to the API
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad responses (4xx or 5xx)

            # Parse the API response as JSON
            country_info_list = response.json()

            # Create a dictionary with the country name as the key and the country info as the value
            country_info_dict = {country['name']['common']: country for country in country_info_list}

            return country_info_dict
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"Something went wrong: {err}")
        return None

    @tree.command(name="land", description="/land  Fx: Land-navn (Kun på engelsk [lige pt.])", guild=discord.Object(id=Server-id))
    async def hvad_er(interaction, string: str):
        print(interaction)
        string = string.lower()

        # Get country information
        country_info_dict = get_country_info(string)

        if country_info_dict:
            # Get the first country info that matches the country name
            country_info = next(iter(country_info_dict.values()), None)

            # Create a description based on country information
            description = f"{country_info.get('name', {}).get('official', 'N/A')}: -/- Hovedstad: {country_info.get('capital', 'N/A')}, Befolkning -/- {country_info.get('population', 'N/A')}  -/- Contient: {country_info.get('region', 'N/A')}: Placering; {country_info.get('subregion', 'N/A')} {country_info.get('flags', {}).get('png', 'N/A')}"
        else:
            description = f"Jeg kender desværre ikke {string} endnu. Vil du fortælle mig, hvilket land det er?"

        await interaction.response.send_message(description)

        # Save command and bot's response in the database
        session = Session()
        bot_answer = BotAnswer(answer=description, command_used=f"/{interaction.data['name']} {string}", user=interaction.user.name, timestamp=datetime.now())
        session.add(bot_answer)
        session.commit()



    #LANDE OPPE


    # /list, /kommando eller /liste - viser en liste over alle kommandoer

    @tree.command(name="list", description="Viser en liste over alle kommandoer", guild=discord.Object(id=Server-id))
    async def list(interaction):
        svar = "Her er en liste over alle kommandoer: \n"
        svar += "/hvem_er \n"
        svar += "/land \n"
        svar += "/næste_video \n"
        svar += "/jeppe \n"
        svar += "/list \n"
        svar += "/vejret \n"
        svar += "/subs \n"
        svar += "Opdateret: 24.10.2023--09:35"

        await interaction.response.send_message(svar)

        session = Session()
        bot_svar = BotAnswer(answer=svar, command_used=f"/list", user=interaction.user.name, timestamp=datetime.now())
        try:
            session.add(bot_svar)
            session.commit()
            print("🏁 Dataen er blevet gemt i databasen.")

        except Exception as e:
            session.rollback()
            print("📛 Fejl ved backup af data i databasen:", str(e))


    #
    ##
    ###
    ####

    # Update the `get_subscriber_count` function
    # import requests
    # import discord
    # from discord.ext import commands

    API_NØGLE = "PLACE YOUR API KEY!"
    # Find on google devolper api keys

    BRUGERNAVN_TIL_KANAL_ID = {
        "mrmastertop1": "UCb_4RTqZ9fjC46YQ0vZONKQ",  # Bruger små bogstaver for brugernavn
        "the economist": "UC0p5jTq6Xx_DosDFxVXnWaQ",
        "tierrg": "UCNUHige4gOBa9buy8sV6pqw",
        "mrbeast": "UCX6OQ3DkcsbYNE6H8uQQuVA",
        "zeqodes": "UCmGdpCTUDzoVKyrEwIh-WKg",
        "charlie2game": "UCYLS4xFy3LTbWNxM5hHPS7Q",
        "mrmasterbottom": "UCimHmnWrz-cz7ZvwrsRM44g",
        "mrmasterbottom1": "UCimHmnWrz-cz7ZvwrsRM44g",
        "shadysmc": "UCrAXM-2iPzEVsJvHUGTIM-A",
        "alexanderhusum": "UCy_FdfBF-YReHm5NYnZ7zcA",
        "mortenmunster": "UC7t9L74u7n6OiTgnHzP0B4g",
        "ourwaytogame": "UCkIp54hQ_OY0IJc4iTYeIJA",
        "kakao_dk": "UCuY8Dpu0vJZSL4BxpCvQNlQ",
        # Tilføj flere tilsvarende som nødvendigt
    }

    @tree.command(name="subs", description="Se live antallet af en youtuber", guild=discord.Object(id=discord-server-id))
    async def få_abonnentantal(interaktion, identifikator: str):
        try:
            # Konverter identifikatoren til små bogstaver for at gøre sammenligningen til ikke at være casesensitiv
            identifikator_små_bogstaver = identifikator.lower()
            # #

            # Tjek om den konverterede identifikator er i de konverterede nøgler fra BRUGERNAVN_TIL_KANAL_ID
            if identifikator_små_bogstaver in {nøgle.lower() for nøgle in BRUGERNAVN_TIL_KANAL_ID.keys()}:
                kanal_id = BRUGERNAVN_TIL_KANAL_ID[identifikator_små_bogstaver]
            else:
                kanal_id = identifikator

            # Hent antallet af abonnenter for den angivne kanal-ID
            url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={kanal_id}&key={API_NØGLE}"
            respons = requests.get(url)
            data = respons.json()

            if 'items' in data and data['items']:
                antal_abonnenter = data['items'][0]['statistics']['subscriberCount']

                # Get the UTC offset in hours and minutes
                utc_offset = datetime.now(timezone.utc).astimezone().utcoffset()
                hours, remainder = divmod(utc_offset.seconds, 3600)
                minutes = remainder // 60

                # Format the UTC offset as "+HH:MM" or "-HH:MM"
                utc_offset_str = f"{hours:+03d}:{minutes:02d}"

                await interaktion.response.send_message(f"Antallet af abonnenter for kanalen er: {antal_abonnenter} abonnenter. \n Sidst opdateret: {datetime.now().strftime('%Y-%m-%d  |  %X')}")

            else:
                await interaktion.response.send_message("Kunne ikke hente antallet af abonnenter for kanalen... Prøv at skrive kanal-id i stedet for. \n(Du kan finde kanal-id'et ved at hente det fra URL'en på kanalens side på YouTube.) \n \nDenne funktion er i BETA, så der kan være fejl. (Opdateret: 2023-10-12--13:24)")
        except requests.exceptions.RequestException as e:
            print("Fejl:", str(e))
            await interaktion.response.send_message("Der opstod en fejl under hentning af antallet af abonnenter.")

        # Save command and bot's response in the database
        session = Session()
        try:
            bot_answer = BotAnswer(answer=antal_abonnenter, command_used=f"/{interaktion.data['name']} {identifikator}", user=interaktion.user.name, timestamp=datetime.now())
            session.add(bot_answer)
            session.commit()
            print("🏁 Dataen er blevet gemt i databasen.")
        except Exception as e:
            session.rollback()
            print("📛 Fejl ved backup af data i databasen:", str(e))

  
####################'

  

    ################

    # WEATHER /vejret bynavn
    weather_translation = {
        "Clear": "Klart ⛱",
        "Clouds": "Overskyet ☁",
        "Drizzle": "Støv regn 🌈",
        "Rain": "Rejnvejr ☔",
        "Snow": "Snevejr ☃",
    }

    def translate_weather_description(english_description):
        return weather_translation.get(english_description, english_description)

    KEY = "API KEY"
    #FIND ON OPENWEATHER

    def weather_now(city, key=KEY):
        url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&APPID=" + key
        response = requests.get(url)
        weather = json.loads(response.text)
        return weather

    @tree.command(name="vejret", description="Se vejret i en by", guild=discord.Object(id=discord-server-id))
    async def vejret(interaction, string: str):
        string = string.lower()
        weather = weather_now(string, KEY)

        if weather["cod"] == 404:
            svar = "Kunne ikke finde nogle værdier der matcher!"
        elif weather["cod"] == 200:
            english_description = weather["weather"][0]["main"]
            danish_description = translate_weather_description(english_description)
            temperature_celsius = int(weather["main"]["temp"])
            weather_report = f"{danish_description}, {temperature_celsius}°C"
            await interaction.response.send_message(weather_report)
        else:
            svar = f'Kunne ikke finde en by ved navn: {string}.'

        #Database
        session = Session()
        try:
            bot_answer = BotAnswer(answer=svar, command_used=f"/{interaction.data['name']} {string}", user=interaction.user.name, timestamp=datetime.now())
            session.add(bot_answer)
            session.commit()
            print("🏁 Dataen er blevet gemt i databasen.")
        except Exception as e:
            session.rollback()
            print("📛 Fejl ved backup af data i databasen:", str(e))

    #########################


    ####


    ####



    ####
    ###



    # @tree(command(name="NÆSTE VIDEO"
    @tree.command(name="næste_video", description="Se hvornår den næste video bliver uploadet", guild=discord.Object(id=discord-server-id))
    async def næste_video(interaction):

        nu = datetime.now()
        lørdag = 5  # Lørdag
        onsdag = 2  # Onsdag
        upload_tidspunkt = datetime(nu.year, nu.month, nu.day, 15, 15)  # 15:15

        # Beregn dage indtil næste upload for lørdag og onsdag
        dage_indtil_lørdag = (lørdag - nu.weekday() + 7) % 7
        dage_indtil_onsdag = (onsdag - nu.weekday() + 7) % 7

        if dage_indtil_lørdag < dage_indtil_onsdag:
            næste_video = nu + timedelta(days=dage_indtil_lørdag)
            svar_dag = 'Lørdag'
        else:
            næste_video = nu + timedelta(days=dage_indtil_onsdag)
            svar_dag = 'Onsdag'

        næste_video = næste_video.replace(hour=15, minute=15)
        svar = f"Den næste video bliver uploadet på {svar_dag} kl. 15.15"

        await interaction.response.send_message(svar)

        session = Session()
        bot_svar = BotAnswer(answer=svar, command_used=f"/næste_video", user=interaction.user.name, timestamp=næste_video)

        try:
            session.add(bot_svar)
            session.commit()
            print("🏁 Dataen er blevet gemt i databasen.")
        except Exception as e:
            session.rollback()
            print("📛 Fejl ved backup af data i databasen:", str(e))
        finally:
            session.close()

    @client.event
    async def on_message(message):
        if message.author == client.user:  # checks if the message is sent by the bot
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} sadge '{user_message}' i '{channel}'")

        session = Session()
        bot_answer = BotAnswer(answer=user_message, user=username, timestamp=datetime.now())
        session.add(bot_answer)
        session.commit()

    @client.event
    async def on_ready():
        await tree.sync(guild=discord.Object(id=discord-server-id))
        print(f"{client.user} Er nu aktiv på Wolt!")

        session = Session()
        bot_session = BotSession(end_time=datetime.now(), start_time=datetime.now())
        session.add(bot_session)
        session.commit()

    client.run(token)