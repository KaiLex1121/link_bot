class CommandsLexicon:
    start_and_help_command: str = 'Привет, этот бот помогает возрождать канал'

    @staticmethod
    def get_user_commands() -> dict[str, str]:

        USER_COMMANDS: dict[str, str] = {
                '/help': 'О боте',
                '/get_link': 'Получить ссылку на канал',
        }

        return USER_COMMANDS


class UserKeyboardsLexicon:
    link_giving_button: str = 'Получить ссылку'
    back_button: str = 'Назад'
    main_channel_button: str = 'Ссылка на основной канал'
    second_channel_button: str = 'Ссылка на канал 18+'
