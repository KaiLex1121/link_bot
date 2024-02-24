class CommandsLexicon:
    start_and_help_command: str = """Привет, этот бот помогает возрождать канал

Hi, this bot helps to revive our channel """


class UserMessages:

    get_link: str = " Выбери канал | Choose the chanel"

    help_message: str = """ Чтобы отключить ограничения в телеграме на айфоне или андроиде, нужно:
1. Перейти в веб-версию Телеграма: web.telegram.org
2. Авторизоваться в аккаунт и зайти в "Настройки"
3. Выбрать раздел "Конфиденциальность"
4. Найти блок "Материалы деликатного характера"
5. Поставить галку на пункт "Выключить ограничения" """

    start_text: str = " Выбери нужное | Choose one of the following "


class AdminMessages:

    def get_links_message(first_link, second_link):
        message = f""" Ссылка на основной канал: {first_link}

Ссылка на порно канал: {second_link} """

        return message
