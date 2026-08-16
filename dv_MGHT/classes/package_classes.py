
from enum import Enum, Flag, auto
import json

# TODO

class DVgameStatus(Flag):
    UPCOMING     =  0 # silver
    SELECTED     =  1 # cyan
    CURRENT      =  2 # white
    SUCCESS      =  4 # green
    FAILED       =  8 # red
    FORCE_FAILED = 16 # emblem

    @classmethod
    def max(cls):
        i = 0
        for member in cls:
            i += member.value
        return i

class DVstatusColors(Enum):
    UPCOMING     = "#ccc" # silver
    SELECTED     = "#0ff" # cyan
    CURRENT      = "#fff" # white
    SUCCESS      = "#ff0" # green
    FAILED       = "#f11" # red
    FORCE_FAILED = "#f0f" # emblem

    @classmethod
    def get_color_from_status(cls, check_status: DVgameStatus):
        if check_status.name in cls.__members__:
            return cls.__members__[check_status.name]

# Class that contains and controls game contents
class DVmghtGame():
    class gameStatus():
        def __init__(self):
            self.__value: DVgameStatus = DVgameStatus.UPCOMING

        def set(self, other: int) -> None:
            if other > DVgameStatus.max():
                return
            self.__value = other

        @property
        def is_selected(self) -> bool:
            return self.__value & DVgameStatus.SELECTED
        @is_selected.setter
        def is_selected(self, other:bool):
            self.__set_bit(DVgameStatus.SELECTED)

        @property
        def is_current(self) -> bool:
            return self.__value & DVgameStatus.CURRENT
        @is_current.setter
        def is_current(self, other:bool):
            self.__set_bit(DVgameStatus.CURRENT)

        @property
        def is_success(self) -> bool:
            return self.__value & DVgameStatus.SUCCESS
        @is_success.setter
        def is_success(self, other:bool):
            self.__set_bit(DVgameStatus.SUCCESS)

        @property
        def is_failed(self) -> bool:
            return self.__value & DVgameStatus.FAILED
        @is_failed.setter
        def is_failed(self, other:bool):
            self.__set_bit(DVgameStatus.FAILED)

        @property
        def is_retry(self) -> bool:
            # Retry is a select, current, or success with failed
            # or where retry is forced.
            # If additional things are added to the future,
            # It will need to be updated.
            return self.__value > DVgameStatus.FAILED
        @is_retry.setter
        def is_retry(self, other:bool):
            self.__set_bit(DVgameStatus.FORCE_FAILED)

        @property
        def background_style(self) -> str:
            # TODO
            return ""

        def __set_bit(self, new_status: DVgameStatus, other: bool) -> None:
            if other:
                self.__value |= new_status
            else:
                self.__value &= ~new_status

    class gameName():
        def __init__(self, game_id: str, caption: str | None = None, game: str | None = None):
            self.id = game_id
            self.__caption = caption
            self.__game = game

        @property
        def caption(self) -> str:
            if self.__caption == "" or self.__caption == None:
                return self.id
            return self.__caption

        @property
        def game(self) -> str:
            if self.__game == "" or self.__game == None:
                return self.caption
            return self.__game

    class gameSplit():
        def __init__(
            self,
            split_id: str,
            caption: str | None = None,
            splits: list = [],
            pb: int = 0
        ):
            self.id = split_id
            self.__caption = caption
            # TODO
            self.splits: list[gameSplit] = []
            self.__pb = pb



        @property
        def personal_best(self):
            resultSum = self.__pb
            for split in splits:
                resultSum += split.personal_best
            return resultSum

        def add_split(self, other: dict | gameSplit) -> None:
            if isinstance(other, gameSplit):
                self.splits.append(other)
                return
            self.splits.append(gameSplit(**other))


    def __init__(
        self,
        game_id: str,
        caption: str | None = None,
        game: str | None = None,
        route: str | None = None,
        split_type: str | None = None,
        splits: list[dict | gameSplit] | None = None,
        pb: int = 0
    ):
        self.status = gameStatus()
        self.name = gameName(inputId, caption, game)
        self.route = route
        self.splitType = splitType
        self.splits: list[gameSplit] = []
        self.__pb = pb

        for new_split in splits or []:
            self.add_split(new_split)

    @property
    def personal_best(self):
        resultSum = self.__pb
        for split in splits:
            resultSum += split.personal_best
        return resultSum

    @property
    def personal_best_text(self) -> str:
        return int(max(self.personal_best, 0))

    def add_split(self, other: dict | gameSplit) -> None:
        if isinstance(other, gameSplit):
            self.splits.append(other)
            return
        self.splits.append(gameSplit(**other))

    def set_selected(self, other: bool | None = None) -> None:
        if other != None:
            self.status.is_selected = other
        else:
            self.status.is_selected = not self.status.is_selected


    def set_current(self, other: bool | None = None) -> None:
        if other != None:
            self.status.is_current = other
        else:
            self.status.is_current = not self.status.is_current

    def set_success(self, other: bool | None = None) -> None:
        if other != None:
            self.status.is_success = other
        else:
            self.status.is_success = not self.status.is_success

    def set_failed(self, other: bool | None = None) -> None:
        if other != None:
            self.status.is_failed = other
        else:
            self.status.is_failed = not self.status.is_failed

    def set_retried(self, other: bool | None = None) -> None:
        if other != None:
            self.status.is_retry = other
        else:
            self.status.is_retry = not self.status.is_retry