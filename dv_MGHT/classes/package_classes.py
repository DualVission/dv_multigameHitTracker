from __future__ import annotations

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

    CLEAR        =  0

    @classmethod
    def max(cls) -> int:
        i = 0
        for member in cls:
            i += member.value
        return i


class DVstatusColors(Enum):
    UPCOMING     = "#ccc" # silver
    SELECTED     = "#0ff" # cyan
    CURRENT      = "#fff" # white
    SUCCESS      = "#1f1" # green
    FAILED       = "#d21" # red
    FORCE_FAILED = "#f0f" # emblem

    @classmethod
    def get_color_from_status(cls, check_status: DVgameStatus):
        if check_status.name in cls.__members__:
            return cls.__members__[check_status.name].value

# Class that contains split information, needs to be separate from games
class gameSplit():
    def __init__(
        self,
        split_id: str,
        caption: str | None = None,
        splits: list = [],
        pb: int = 0,
        path: str | None = None
    ):
        self.id = split_id
        self.__caption = caption
        # TODO
        self.splits: list[dict] = []
        self.__pb = pb
        self.__path = path



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


# Class that contains and controls game contents
class DVmghtGame():
    class gameStatus():
        def __init__(self):
            self.__value: DVgameStatus = DVgameStatus.UPCOMING

        def set(self, other: DVgameStatus) -> None:
            if other.value > DVgameStatus.max():
                return
            self.__value &= DVgameStatus.CLEAR
            self.__value = other

        @property
        def name(self):
            if self.is_forced and self.is_selected:
                return "FORCE_FAILED"
            elif self.is_success:
                return "SUCCESS"
            elif self.is_failed and self.is_selected:
                return "FAILED"
            elif self.is_current:
                return "CURRENT"
            elif self.is_selected:
                return "SELECTED"
            elif self.is_failed:
                return "FAILED"
            else:
                return "UPCOMING"
        

        @property
        def is_selected(self) -> bool:
            return self.__value & DVgameStatus.SELECTED
        @is_selected.setter
        def is_selected(self, other:bool):
            self.__set_bit(DVgameStatus.SELECTED, other)

        @property
        def is_current(self) -> bool:
            return self.__value & DVgameStatus.CURRENT
        @is_current.setter
        def is_current(self, other:bool):
            self.__set_bit(DVgameStatus.CURRENT, other)

        @property
        def is_success(self) -> bool:
            return self.__value & DVgameStatus.SUCCESS
        @is_success.setter
        def is_success(self, other:bool):
            self.__set_bit(DVgameStatus.SUCCESS, other)

        @property
        def is_failed(self) -> bool:
            return self.__value & DVgameStatus.FAILED
        @is_failed.setter
        def is_failed(self, other:bool):
            self.__set_bit(DVgameStatus.FAILED, other)

        @property
        def is_retry(self) -> bool:
            # Retry is a select, current, or success with failed
            # or where retry is forced.
            # If additional things are added to the future,
            # It will need to be updated.
            fail_selected = DVgameStatus.FAILED | DVgameStatus.SELECTED
            return self.__value.value > fail_selected.value
        @is_retry.setter
        def is_retry(self, other:bool):
            self.__set_bit(DVgameStatus.FORCE_FAILED, other)

        @property
        def is_forced(self) -> bool:
            return self.__value & DVgameStatus.FORCE_FAILED
        @is_forced.setter
        def is_forced(self, other: bool):
            self.__set_bit(DVgameStatus.FORCE_FAILED, other)

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

    def __init__(
        self,
        name: dict[str],
        route: str | None = None,
        split_type: str | None = None,
        splits: list[dict | gameSplit] | None = None,
        pb: int = 0,
        path: str | None = None
    ):
        self.status = self.gameStatus()
        self.name = self.gameName(**name)
        self.route = route
        self.splitType = split_type
        self.splits: list[gameSplit] = []
        self.__pb = pb
        self.__path = path

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

    @property
    def accessible_name(self) -> str:
        return "{name} is {status}".format(name=self.name.game, status="")

    @property
    def background_style(self) -> str:
        border_color = self.status
        if self.status.is_selected:
            if self.status.is_success and self.status.is_current:
                border_color = DVgameStatus.CURRENT
            else:
                border_color = DVgameStatus.SELECTED
        style_text = self.__style_text().format(
            bg=DVstatusColors.get_color_from_status(self.status),
            bd=DVstatusColors.get_color_from_status(border_color),
            oc="{",
            cc="}",
            id=self.name.id
        )
        return style_text

    def __style_text(self) -> str:
        return """QStackedWidget {oc}
            background-color: {bg};
            border: 2px solid {bd};
            border-radius: 1px;
            {cc}
        """

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

    def set_forced(self, other: bool | None = None) -> None:
        if other != None:
            self.status.is_forced = other
        else:
            self.status.is_forced = not self.status.is_forced

# Class that contains and controls package contents
class DVmghtPackage():

    class packageRepo():
        def __init__(
            self,
            path: str,
            authors: list[str],
            link: str,
            source: str,
            license: str
        ):
            self.path = path
            self.authors = authors
            self.link = link
            self.source = source
            self.license = license

    def __init__(
        self,
        path: str,
        package: dict[str | bool | list[str]],
        repository: dict[str | list[str]],
        games: list[dict] | None = None
    ):
        self.repository = self.packageRepo(path, **repository)
        self.name: str = package["name"]
        self.version: str = package["version"]
        self.id: str = package["package_id"]
        self._games: list[str] = package["games"]
        self.games: list[DVmghtGame] = []
        self._has_splits: bool = package["has_splits"]

        if games != None:
            self.load_games(games)

    def load_games(self, games_to_load: list[dict]):
        for raw_game in games_to_load:
            self.games.append(DVmghtGame(**raw_game))