from config_data.config import get_channel_link
from services.redis_logic import get_from_redis

class CommandsLexicon:
    start_and_help_command: str = 'Привет, этот бот помогает возрождать канал'


class UserKeyboardsLexicon:
    link_giving_button: str = 'Получить ссылку | Get a link'
    help_button = "Помощь | Help"
    how_to_join_button = "Как зайти на порно канал"
    message_to_admin_button = "Связаться с админом"
    back_button: str = 'Назад | Back'
    main_channel_button: str = 'Основа | Gore'
    second_channel_button: str = '18+ | Porn'


class AdminKeyboardsLexicon:
    administer_button: str = "Модерация бота"
    cancel_editing_button: str = "Отменить редактирование"


class UserMessagesLexicon:

    get_link: str = """
Выбери канал

Choose the chanel
    """

    help_message: str = """ Чтобы отключить ограничения в телеграме на айфоне или андроиде, нужно:
1. Перейти в веб-версию Телеграма: web.telegram.org.
2. Авторизоваться в аккаунт и зайти в "Настройки".
3. Выбрать раздел "Конфиденциальность"
4. Найти блок "Материалы деликатного характера".
5. Поставить галку на пункт "Выключить ограничения".
"""

    start_text: str = """
Выбери нужное

Choose one of the following
    """