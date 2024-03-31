import asyncio
import logging
import os.path

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class FileWatcherPlugin(FileSystemEventHandler):
    def __init__(self, loop, config):
        super().__init__()
        self.to_process = asyncio.Queue()
        self.processed_files = asyncio.Queue()
        self.watch_folder = config["input_folder"]
        self.observer = Observer()
        self.loop = loop
        self.logger = logging.getLogger(f"{self.__class__.__name__}")

    async def add_file(self, filename):
        self.logger.debug(f"add file {filename} to be processed queue")
        await self.to_process.put(filename)

    async def mark_processed(self, processed_file):
        self.logger.debug(f"add file {processed_file} to processed queue")
        await self.processed_files.put((processed_file, True))

    async def get_next_processed_file(self):
        return await self.processed_files.get()

    async def get_file_to_process(self):
        return await self.to_process.get()

    def on_created(self, event):
        filename = os.path.basename(event.src_path)
        """
        AMD ReLive creates some temp folders and then saves the output file first as an "out.mp4"
        then as a Replay_*.mp4 in root folder and then finally moves it to corresponding sub-folder
        which is why there are these checks.
        Should probably work with other recording apps fine.
        """
        if os.path.dirname(os.path.abspath(event.src_path)) != os.path.normpath(self.watch_folder):
            if not event.is_directory and filename.endswith(".mp4") and filename != "out.mp4":
                self.logger.debug(f"new file added: `{event.src_path}`")
                asyncio.run_coroutine_threadsafe(self.add_file(event.src_path), self.loop)

    async def start_monitoring(self):
        self.logger.debug(f"starting folder monitoring for folder: `{self.watch_folder}`")
        self.observer.schedule(self, self.watch_folder, recursive=True)
        self.observer.start()

    async def stop_monitoring(self):
        self.logger.debug(f"stopped folder monitoring")
        self.observer.stop()
        self.observer.join()

    async def run(self):
        await self.start_monitoring()
        try:
            while True:
                await asyncio.sleep(1)
        finally:
            await self.stop_monitoring()
