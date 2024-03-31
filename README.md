# pilc - clip

Welcome to pilc! 🎮📹 

This little project of mine is all about sharing those epic, funny, or downright ridiculous moments from our gaming sessions, without the hassle of manual editing and uploading. Whether it's that impossible sniper shot, a hilarious glitch, or an unexpected win, pilc makes it easy to share these moments with friends in our Telegram chat, almost instantly.

## How It Works

pilc monitors a specified folder on your computer for new video clips (like those saved by your game's replay feature or a screen recording tool). Whenever a new clip is detected, the app springs into action:

1. **Automagic Conversion:** First off, it uses FFMpeg to make sure the clip is in a Telegram-friendly format, tweaking it to look good without taking forever to upload.
2. **Teleporting to Telegram:** Once the clip is ready to roll, pilc then posts it directly to our designated Telegram chat, ready for all the "oohs" and "ahhs" (or laughs, we don't judge).

## Setting Up

Here's how to get your own pilc up and running:

### Prerequisites

- **FFMpeg:** Make sure you have FFMpeg installed on your system because, well, magic needs wands.
- **Python 3.11+:** The whole shebang is written in Python, so you'll need that too.

### Installation

1. **Clone the repository:** Grab the code.
2. **Install dependencies:** Jump into your terminal, navigate to the project folder, and run `pip install -r requirements.txt` to get all the Python goodies lined up.
3. **Configuration:** You'll need to set up a `config.yml` file in the project root. Create one from config_template.yml that's provided
4. **Run pilc:** With everything in place, start the app by running `python path/to/ShittyClips/main.py.`
5. **Login to telegram:** For the first login you'll be asked to enter your 2FA code in terminal, consequent runs can be done by `clip.bat` (don't forget to update paths in there too)

### Usage
- **Saving Clips:** Just save your gameplay clips to the input_folder you specified in your config. ShittyClips will take it from there.
- **Watching the Magic:** Kick back and see your clips pop up in the Telegram chat. Grab some popcorn while you're at it.

### Troubleshooting

- **"It's not working!":** Check the logs; I've set up some pretty verbose logging to help figure out what's going wrong. Make sure your config paths are correct and that FFMpeg is properly installed.
- **"Why is it slow?":** Video processing can be a bit heavy, so give it some time. The speed can also depend on your computer's specs.

### Contribute

Got ideas to make ShittyClips better? Found a bug that needs squashing? Feel free to fork, submit issues, or send pull requests. Let's make ShittyClips the best darn quick clip-sharing tool for gamers out there!

That's all, folks! Get out there and start sharing those legendary gaming moments with ShittyClips! 🚀