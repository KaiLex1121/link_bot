import enum


class TypeOfChat(enum.Enum):
    private = enum.auto()
    channel = enum.auto()
    group = enum.auto()
    supergroup = enum.auto()