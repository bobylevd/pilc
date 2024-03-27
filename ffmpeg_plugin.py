import asyncio
import logging
import os
import subprocess


class FFMpegPlugin:
    def __init__(self, file_queue_plugin, config):
        self.file_queue = file_queue_plugin
        self.output_folder = config["output_folder"]
        self.ffmpeg_flags = config["ffmpeg_flags"]
        self.logger = logging.getLogger(f"{self.__class__.__name__}")

    async def process_file(self, filename):
        if not os.path.isdir(self.output_folder):
            os.makedirs(self.output_folder)

        out = os.path.join(self.output_folder, os.path.basename(filename))

        ffmpeg_command = ["ffmpeg", "-i", filename, *self.ffmpeg_flags, out]

        self.logger.debug(f"processing file {filename} with ffmpeg")
        process = await asyncio.create_subprocess_exec(*ffmpeg_command, creationflags=subprocess.CREATE_NO_WINDOW)

        await process.wait()
        await self.file_queue.mark_processed(out)

    async def run(self):
        while True:
            filename = await self.file_queue.get_file_to_process()
            await self.process_file(filename)
            await asyncio.sleep(1)
