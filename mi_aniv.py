import os
import random
import markovify
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
        print(f'Logged into Twitch | {bot.nick}')

    async def event_message(self, ctx):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if ctx.echo:
            return

        # Print the contents of our message to console...
        print(ctx.content)
        # Incrementar el contador de mensajes
        self.messages_since_last_print += 1

        with open("chat.txt", encoding="utf-8", mode="a") as f:
            f.write(ctx.content + "\n")

        if self.messages_since_last_print >= random.randint(10, 15):
            print(f"mensaje de prueba: {self.messages_since_last_print}")
            self.messages_since_last_print = 0
            model = markovify.Text(self.text)
            response = model.make_sentence()
            # Verificar si el modelo de Markov está generando un mensaje
            if response:
                await ctx.channel.send(response)
            else:
                print("El modelo de Markov no generó un mensaje.")

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(ctx)

    @commands.command()
    async def hola(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g ?hello
        # We can also give our commands aliases (different names) to invoke with.

        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        await ctx.send(f'Hola uwu {ctx.author.name}!')


bot = Bot()
bot.run()
# bot.run() is blocking and will stop execution of any below code here until stopped or closed.
