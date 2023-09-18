from config_data.config import get_channel_link
from services.redis_logic import get_from_redis

class CommandsLexicon:
    start_and_help_command: str = 'Привет, этот бот помогает возрождать канал'


class UserKeyboardsLexicon:
    link_giving_button: str = 'Получить ссылку'
    help_button = "Помощь"
    how_to_join_button = "Как зайти на порно канал"
    message_to_admin_button = "Связаться с админом"
    back_button: str = 'Назад'
    main_channel_button: str = 'Ссылка на основной канал'
    second_channel_button: str = 'Ссылка на канал 18+'


class AdminKeyboardsLexicon:
    administer_button: str = "Модерация бота"
    cancel_editing_button: str = "Отменить редактирование"


class UserMessagesLexicon:
    help_message: str = """ Чтобы отключить ограничения в телеграме на айфоне или андроиде, нужно:
1. Перейти в веб-версию Телеграма: web.telegram.org.
2. Зайти в настройки и авторизоваться по номеру телефона.
3. В настройках следует выбрать раздел "Конфиденциальность"
4. Найти блок "Материалы деликатного характера".
5. Поставить галку "Выключить ограничения".
"""


# class AdminMessagesLexicon:
#     get_links_message: str = f"""
# Ссылка на основной канал: {get_from_redis('main_link')}

# Ссылка на порно канал: {get_from_redis('second_link')}"""
