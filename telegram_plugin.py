import asyncio
import logging

from pyrogram import Client


class TelegramPlugin:
    def __init__(self, file_queue_plugin, config):
        self.file_queue_plugin = file_queue_plugin
        self.chat_id = config["chat_id"]
        self.logger = logging.getLogger(f"{self.__class__.__name__}")
        self.client = Client(
            "shitty clips", api_id=config["api_id"], api_hash=config["api_hash"], phone_number=config["phone_number"]
        )

    async def start_client(self):
        if not self.client.is_connected:
            self.logger.debug("starting telegram client")
            await self.client.start()

    async def stop_client(self):
        if self.client.is_connected:
            self.logger.debug("stopping telegram client")
            await self.client.stop()

    async def post_file(self, filename):
        self.logger.debug(f"posting file `{filename}` to chat: `{self.chat_id}`")
        await self.client.send_video(chat_id=self.chat_id, video=filename)

    async def run(self):
        await self.start_client()
        try:
            while True:
                filename, processed = await self.file_queue_plugin.get_next_processed_file()
                if processed:
                    await self.post_file(filename)
                await asyncio.sleep(1)
        finally:
            await self.stop_client()
