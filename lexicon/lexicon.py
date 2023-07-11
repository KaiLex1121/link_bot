class CommandsLexicon:
    start_and_help_command = 'Привет, этот бот помогает возрождать канал'

    @staticmethod
    def get_user_commands():

        USER_COMMANDS: dict[str, str] = {
                '/help': 'О боте',
                '/get_link': 'Получить ссылку на канал',
        }

        return USER_COMMANDS
