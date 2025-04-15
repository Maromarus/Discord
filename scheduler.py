from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
import pytz
import discord
import os
from dotenv import load_dotenv
from utils import read_link
import discord.utils

load_dotenv()

tz = pytz.timezone('Asia/Seoul')
CHANNEL_NAME = os.getenv("CHANNEL_NAME")

def setup_scheduler(bot, stop_flag):
    scheduler = AsyncIOScheduler(timezone=tz)

    # ✅ 테스트용: 10초 후 단일 알림
    scheduler.add_job(
        send_message,
        trigger='date',
        run_date=datetime.now(tz) + timedelta(seconds=10),
        args=[bot, stop_flag, "⏰ [테스트] 10초 후 도착한 알림입니다."]
    )

    # 출근 알림
    scheduler.add_job(
        send_image_message,
        trigger='cron',
        hour=8, minute=50,
        args=[
            bot, stop_flag,
            lambda: f"@everyone 🚪 곧 수업 시간입니다! 어서 입장해서 카메라를 세팅해주세요! 입장 링크: {read_link()}",
            "images/QR_test.png"
        ]
    )

    # 퇴근 알림
    scheduler.add_job(
        send_image_message,
        trigger='cron',
        hour=17, minute=55,
        args=[
            bot, stop_flag,
            "@everyone ✅ 수고하셨습니다! 꼭 퇴실 체크 해주시고, 화이팅 하시길 바라겠습니다!",
            "images/QR_test.png"
        ]
    )

    # 정각/50분 알림
    for h in range(9, 18):
        for m in [0, 50]:
            if (h, m) in [(8, 50), (17, 55), (12, 0), (12, 50)]:
                continue

            if m == 0:
                scheduler.add_job(
                    send_message,
                    trigger='cron',
                    hour=h, minute=m,
                    args=[bot, stop_flag, "@everyone 정각입니다! 수업 시작을 위해 카메라를 켜주세요!"]
                )
            elif m == 50:
                if h == 11:
                    scheduler.add_job(
                        send_message,
                        trigger='cron',
                        hour=h, minute=m,
                        args=[bot, stop_flag, "@everyone 점심시간입니다! 맛있는 식사 하시고 1시에 다시 뵙겠습니다!"]
                    )
                else:
                    scheduler.add_job(
                        send_message,
                        trigger='cron',
                        hour=h, minute=m,
                        args=[bot, stop_flag, "@everyone 쉬는 시간입니다! 10분 후 수업을 다시 시작할게요!"]
                    )

    scheduler.start()

async def get_target_channel(bot):
    for guild in bot.guilds:
        channel = discord.utils.get(guild.text_channels, name=CHANNEL_NAME)
        if channel and channel.permissions_for(guild.me).send_messages:
            return channel
    return None

async def send_message(bot, stop_flag, message):
    if stop_flag["stop"]:
        return
    channel = await get_target_channel(bot)
    if channel:
        await channel.send(message)

async def send_image_message(bot, stop_flag, message, image_path):
    if stop_flag["stop"]:
        return
    channel = await get_target_channel(bot)
    if channel:
        if callable(message):
            message = message()
        if os.path.exists(image_path):
            with open(image_path, 'rb') as f:
                file = discord.File(f)
                await channel.send(content=message, file=file)
        else:
            await channel.send(message)
