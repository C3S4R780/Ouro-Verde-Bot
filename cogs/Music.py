import nextcord
from nextcord.ext import commands
from nextcord import Interaction, FFmpegPCMAudio

class Music(commands.Cog):

    def __init__(self, client):
        self.client = client

    server_id = 821937691167162379

    # Commands
    # Command to call the bot into voice chat and play the radio's audio
    @nextcord.slash_command(name="tocar", description="Me chama para o canal de voz atual para tocar a rádio 😁", guild_ids=[server_id])
    async def tocar(self, interaction: Interaction):

        if (interaction.user.voice):
            userVoiceChannel = interaction.user.voice.channel
        else:
            await interaction.response.send_message("⚠️ Você precisar estar em um canal de voz para usar este comando.")
            return

        if (interaction.client.voice_clients):
            for client in interaction.client.voice_clients:
                if client.channel == userVoiceChannel:
                    await interaction.response.send_message("⚠️ Já estou tocando nesse canal.")
                else:
                    roles = [];
                    for role in interaction.user.roles:
                        roles.append(role.name)
                    if "DJ" in roles:
                        await interaction.response.send_message("🏃 Indo para o canal: " + userVoiceChannel.name)
                        await client.move_to(userVoiceChannel)
                    else:
                        await interaction.response.send_message("⚠️ Você não tem permissão para me mover de canal")

        else:
            source = FFmpegPCMAudio("https://servidor18.brlogic.com:7484/live")
            voice = await userVoiceChannel.connect()
            player = voice.play(source)
            await interaction.response.send_message("✅ Tocando no canal: " + userVoiceChannel.name)

    # Command to remove the bot from the current voice channel
    @nextcord.slash_command(name="sair", description="Me remove do canal de voz 😔", guild_ids=[server_id])
    async def sair(self, interaction: Interaction):
        if (interaction.client.voice_clients):
            for client in interaction.client.voice_clients:
                if (client.channel != interaction.user.voice.channel):
                    await interaction.response.send_message("⚠️ Você não está no mesmo canal para me remover.")
                    return
                else:
                    client.cleanup()
                    await client.disconnect()
                    await interaction.response.send_message("❤️ Até a proxima.")
        else:
            await interaction.response.send_message("⚠️ Ainda não estou em nenhum canal de voz.")

def setup(client):
    client.add_cog(Music(client))