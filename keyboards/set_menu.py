from aiogram import Bot
from aiogram.types import BotCommand
from lexicon.lexicon import CommandsLexicon


async def set_main_menu(bot: Bot):

    # Создаем список с командами и их описанием для кнопки menu
    main_menu_commands = [BotCommand(command=command,
                                     description=description)
                                     for command, description
                                     in CommandsLexicon.get_user_commands().items()]



    await bot.set_my_commands(main_menu_commands)
