#!/usr/bin/env python3
"""
Domain92 Discord Bot Launcher
A Discord bot wrapper for the domain92 freedns automation tool
"""

import os
import sys

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import and run the bot
from discord_bot import bot, TOKEN

if __name__ == "__main__":
    print("Starting Domain92 Discord Bot...")
    print("Bot will connect to Discord and be ready for commands!")
    print("Use !help in Discord to see available commands.")
    bot.run(TOKEN) 