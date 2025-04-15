import discord
from discord.ext import commands
from scheduler import setup_scheduler
from dotenv import load_dotenv
import os

from utils import read_link, write_link 

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

daily_stop_flag = {"stop": False}

@bot.event
async def on_ready():
    print(f'✅ 봇 로그인 성공: {bot.user}')
    setup_scheduler(bot, daily_stop_flag)

@commands.has_permissions(administrator=True)
@bot.command(name="알림끄기")
async def 알림끄기(ctx):
    daily_stop_flag["stop"] = True
    await ctx.send("🔕 오늘 하루는 알림을 보내지 않겠습니다!")

@commands.has_permissions(administrator=True)
@bot.command(name="사진변경")
async def 출근사진변경(ctx):
    if ctx.message.attachments:
        await ctx.message.attachments[0].save("images/QR_test.png")
        await ctx.send("🌅 QR 사진이 변경되었습니다.")
    else:
        await ctx.send("❗ 이미지를 첨부해주세요.")

@commands.has_permissions(administrator=True)
@bot.command(name="입장링크변경")
async def 입장링크변경(ctx, *, new_link=None):
    if new_link:
        write_link(new_link)
        await ctx.send(f"🔗 입장 링크가 변경되었습니다:\n{new_link}")
    else:
        await ctx.send("❗ 링크를 함께 입력해주세요.\n예: `!입장링크변경 https://your.new.link`")

@bot.command(name="도움말")
async def help_command(ctx):
    help_text = """
📌 사용 가능한 명령어 목록:

- `!도움말` : 명령어 목록을 확인합니다.
- `!알림끄기` : 오늘 하루 알림을 끕니다. (🔒 관리자만 가능)
- `!입장링크변경 [링크]` : 출근 알림에 포함될 링크를 변경합니다. (🔒 관리자만 가능)
- `!사진변경` + 이미지 첨부 : 출근 시 전송할 이미지를 변경합니다. (🔒 관리자만 가능)
"""
    await ctx.send(help_text)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ 이 명령어는 관리자만 사용할 수 있습니다.")
    else:
        raise error


bot.run(TOKEN)
