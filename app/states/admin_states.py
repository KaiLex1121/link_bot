from aiogram.filters.state import StatesGroup, State


class EditLinkState(StatesGroup):
    FILL_MAIN_LINK = State()
    FILL_SECOND_LINK = State()
    FILL_ANIMAL_LINK = State()


class MakeBroadcastState(StatesGroup):
    MESSAGE_TEXT_WRITING = State()
    BROADCAST_PREVIEW = State()
    MESSAGE_TEXT_REWRITING = State()
    BROADCAST_CANCDELED = State()
    BACK_BUTTON_PRESSED = State()
    SUCCESS_BROADCAST = State()


class GetStatisticState(StatesGroup):
    ...