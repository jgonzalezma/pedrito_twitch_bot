import random
import markovify
import asyncio
from twitchio.ext import commands

class Bot(commands.Bot):
    def __init__(self):
        self.messages_since_last_print = 0
        # Crear bot de Twitch
        with open("config.secret", "r") as fp:
            lines = fp.readlines()
            config = {}
            for line in lines:
                partes = line.replace("\n", "").split("=")
                config[partes[0]] = partes[1]

        super().__init__(
            token=config['TOKEN'],
            client_id=config['CLIENT_ID'],
            nick=config['BOT_NICK'],
            prefix=config['BOT_PREFIX'],
            initial_channels=[config['CHANNEL']]
        )

        with open("chat.txt", encoding="utf-8") as f:
            self.text = f.read()

    async def event_ready(self):
        print(f'Logged into Twitch | {self.nick}')

    async def event_message(self, ctx):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if ctx.echo:
            return

        # Print the contents of our message to console...
        print(ctx.content)
        # Incrementar el contador de mensajes
        self.messages_since_last_print += 1

        #Guarda todo lo que se escribe en el chat en chat.txt
        with open("chat.txt", encoding="utf-8", mode="a") as f:
            f.write(ctx.content + "\n")

        if self.messages_since_last_print >= random.randint(10, 16):
            self.messages_since_last_print = 0
            # Construir modelo de Markov con las palabras de longitud 1-3
            model = markovify.Text(self.text)
            # Generar una oración
            if random.random() < 0.07:
                with open("chat.txt", encoding="utf-8", mode="r") as f:
                    lines = f.readlines()
                    # Select a random line from the file
                    response = random.choice(lines)
            else:
                response = model.make_sentence()
            # Verificar si el modelo de Markov está generando un mensaje
            if response:
                # Limitar la longitud a 100 caracteres sin dividir palabras
                if random.random() < 0.05:
                    await asyncio.sleep(random.uniform(1, 10))
                    await ctx.channel.send(response)
                else:
                    if len(response) > 115:
                        response = response[:115].rsplit(' ', 1)[0]
                        # Esperar un tiempo aleatorio entre 1 y 7 segundos
                        await asyncio.sleep(random.uniform(1, 2))
                        await ctx.channel.send(response)
            else:
                print("El modelo de Markov no generó un mensaje.")
        
            # Verificar si el mensaje es una respuesta a un mensaje existente en el chat
        elif ctx.content.startswith('@'):
            # Crear modelo de Markov solo con el mensaje anterior
            model = markovify.Text(self.text)
            # Generar una oración
            response = model.make_sentence()
            # Verificar si el modelo de Markov está generando un mensaje
            if response:
                # Limitar la longitud a 110 caracteres sin dividir palabras
                if len(response) > 110:
                    response = response[:110].rsplit(' ', 1)[0]
                # Esperar un tiempo aleatorio entre 1 y 7 segundos
                await asyncio.sleep(random.uniform(1, 7))
                await ctx.channel.send(response)
            else:
                print("El modelo de Markov no generó un mensaje.")

            # Since we have commands and are overriding the default `event_message`
            # We must let the bot know we want to handle and invoke our commands...
            await self.handle_commands(ctx)

    @commands.command()
    async def hola(self, ctx: commands.Context):
        # comando !hola
        await ctx.send(f'Hola uwu {ctx.author.name}!')


bot = Bot()
bot.run()
# bot.run() is blocking and will stop execution of any below code here until stopped or closed.