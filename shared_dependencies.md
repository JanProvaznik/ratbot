1. discord.py: This is a Python library that will be used across all the files for interacting with Discord's API. It will be included in the "requirements.txt" file and imported in "main.py", "message_handler.py", and "react_handler.py".

2. Configurations: The "config.py" file will contain shared configurations like the Discord bot token, which will be used in "main.py" to authenticate the bot.

3. MessageHandler: This is a class defined in "message_handler.py" that will handle incoming messages. It will be used in "main.py" to set up the bot's message handling.

4. ReactHandler: This is a class defined in "react_handler.py" that will handle reactions to messages. It will be used in "main.py" to set up the bot's reaction handling.

5. on_message and on_reaction_add: These are event names defined by discord.py that will be used in "message_handler.py" and "react_handler.py" respectively to handle new messages and reactions.

6. Client: This is a class provided by discord.py that will be used in "main.py" to create the bot client. It will also be used in "message_handler.py" and "react_handler.py" to interact with the Discord API.

7. asyncio: This is a Python library for asynchronous I/O that will be used in "main.py" to run the bot. It may also be used in "message_handler.py" and "react_handler.py" for any asynchronous operations.

8. Message and Reaction: These are classes provided by discord.py that will be used in "message_handler.py" and "react_handler.py" to interact with messages and reactions.