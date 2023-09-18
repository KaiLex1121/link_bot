from aiogram.filters.state import StatesGroup, State


class EditLinkState(StatesGroup):
    FILL_MAIN_LINK = State()
    FILL_SECOND_LINK = State()
