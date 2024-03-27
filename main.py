import asyncio

import yaml

from ffmpeg_plugin import FFMpegPlugin
from file_watcher_plugin import FileWatcherPlugin
from telegram_plugin import TelegramPlugin


class ShittyClips:
    def __init__(self):
        self.plugins = []

    def register_plugin(self, plugin):
        self.plugins.append(plugin)

    async def run(self):
        tasks = [plugin.run() for plugin in self.plugins]
        await asyncio.gather(*tasks)


def main():
    with open("./config.yml", "r") as config_file:
        config = yaml.safe_load(config_file)

    app = ShittyClips()
    loop = asyncio.get_event_loop()

    file_watcher_plugin = FileWatcherPlugin(loop, config)
    ffmpeg_plugin = FFMpegPlugin(file_watcher_plugin, config)
    telegram_plugin = TelegramPlugin(file_watcher_plugin, config)
    app.register_plugin(file_watcher_plugin)
    app.register_plugin(ffmpeg_plugin)
    app.register_plugin(telegram_plugin)
    loop.run_until_complete(app.run())


if __name__ == "__main__":
    main()
