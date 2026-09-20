from __future__ import annotations

from enum import Enum, Flag, auto

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

    CLEAR        = UPCOMING

    @classmethod
    def get_color_from_status(cls, check_status: DVgameStatus):
        if check_status.name in cls.__members__:
            return cls.__members__[check_status.name].value

class DVsplitTypes(Enum):
    LINEAR = "linear"
    OPEN   = "open"

# Class that contains split information, needs to be separate from games
class DVmghtSplit():
    def __init__(
        self,
        parent: DVmghtGame | DVmghtSplit,
        split_id: str,
        caption: str | None = None,
        splits: list[ dict ] = [],
        pb: list[ int | None ] = [],
        path: str | None = None,
        selectable: bool | None = True,
        split_type: str | None = None,
        **kwargs
    ):
        self.__parent: DVmghtGame | DVmghtSplit = parent
        self.id = split_id
        self.__caption = caption
        # TODO
        converted_split_type = None
        if split_type == None:
            converted_split_type = self.__parent.split_type
        else:
            converted_split_type = DVsplitTypes(split_type)
        self.split_type = converted_split_type
        self.selectable = selectable
        self.__pb: list[int|None, ...] = [ None ] * self.__parent.number_of_hits
        if isinstance(pb, list):
            if len(pb) <= self.__parent.number_of_hits:
                for i in range(len(pb)):
                    self.__pb[i] = pb[i]
            else:
                raise TypeError(
                    "DVmghtGame.__init__() required argument, 'pb', malformed:\n"
                    + str(pb)
                )
        self.__path = path
        self.__future_proof: dict = {**kwargs}

        self.split_from_id: dict[str, DVmghtSplit] = {}

        for split in splits:
            self.add_split(split)

    @property
    def caption(self) -> str:
        if self.__caption == "" or self.__caption == None:
            return self.id
        return self.__caption

    @property
    def parent(self) -> DVmghtGame | DVmghtSplit | None:
        return self.__parent
    @parent.setter
    def parent(self, other: DVmghtGame | DVmghtSplit) -> None:
        self.__parent = other

    @property
    def number_of_hits(self) -> int:
        return len(self.__pb)

    @property
    def personal_best(self) -> list[int]:
        resultSums: list[int] = [
            max(item or 0, 0) for item in self.__pb 
        ]
        for split in self.splits:
            splitPb = split.personal_best
            for i in range(len(self.__pb)):
                resultSums[i] += max(splitPb[i], 0)
        return resultSums

    @property
    def personal_best_text(self) -> str:
        return str(self.personal_best[0])

    @property
    def splits(self) -> list[DVmghtSplit]:
        return [ *self.split_from_id.values() ]

    def add_split(self, other: dict) -> None:
        if other["split_id"] == "":
            return
        other = { "parent": self, **other }
        new_split = DVmghtSplit(**other)
        self.split_from_id[new_split.id] = new_split

# Class that contains and controls game contents
class DVmghtGame():
    class gameStatus():
        def __init__(self):
            self.__value: DVgameStatus = DVgameStatus.UPCOMING

        def __str__(self) -> str:
            return str(self.__value)

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
        def accessible_name(self):
            outputS = []
            if self.is_current:
                outputS.append("current")
            if self.is_selected:
                outputS.append("selected")
            if self.is_retry:
                outputS.append("being retried")
            if self.is_success:
                outputS.append("successful")
            if self.is_failed and not self.is_retry:
                outputS.append("successful")
            if len(outputS) >= 0:
                outputS.append("upcoming")
            if len(outputS) == 1:
                return  outputS[0]
            elif len(outputS) == 2:
                return " and ".join(outputS)
            return ", ".join(outputS[:-1]) + ", and " + outputS[-1]

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
        def __init__(
            self,
            game_id: str,
            caption: str | None = None,
            game: str | None = None
        ):
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
        parent: DVmghtPackage,
        name: dict[ str ] = {},
        route: str | None = None,
        split_type: str | None = None,
        splits: list[ dict ] = [],
        pb: list[ int | None ] = [],
        path: str | None = None,
        **kwargs
    ):
        self.__parent: DVmghtPackage  = parent
        self.status = self.gameStatus()
        if len(name) <= 0:
            raise TypeError("DVmghtGame.__init__() missing 1 required argument: 'name'")
        elif "game_id" not in name:
            raise TypeError(
                "DVmghtGame.__init__() required argument, 'name', malformed:\n"
                + name
            )
        self.name = self.gameName(**name)
        self.route = route
        if split_type == None:
            converted_split_type = self.__parent.settings.default_split_type
        else:
            converted_split_type = DVsplitTypes(split_type)
        self.split_type = converted_split_type
        self.__pb: list[int|None, ...] = [ None ] * self.__parent.settings.number_of_hits
        if isinstance(pb, list):
            if len(pb) <= self.__parent.settings.number_of_hits:
                for i in range(len(pb)):
                    self.__pb[i] = pb[i]
            else:
                raise TypeError(
                    "DVmghtGame.__init__() argument, 'pb', malformed:\n"
                    + str(pb)
                )
            
        self.__path = path
        self.__future_proof = {**kwargs}

        self.split_from_id: dict[str, DVmghtSplit] = {}

        for new_split in splits:
            self.add_split(new_split)

    def __str__(self):
        return self.name.game

    @property
    def parent(self) -> DVmghtPackage:
        return self.__parent
    @parent.setter
    def parent(self, other: DVmghtPackage) -> None:
        self.__parent = other

    @property
    def number_of_hits(self) -> int:
        return len(self.__pb)

    @property
    def personal_best(self) -> list[int]:
        resultSums: list[int] = [
            max(item or 0, 0) for item in self.__pb 
        ]
        for split in self.splits:
            splitPb = split.personal_best
            for i in range(len(self.__pb)):
                resultSums[i] += max(splitPb[i], 0)
        return resultSums

    @property
    def personal_best_text(self) -> str:
        return str(self.personal_best[0])

    @property
    def accessible_name(self) -> str:
        return "{name} is {status}".format(
            name=self.name.game,
            status=self.status.accessible_name
        )

    @property
    def splits(self) -> list[DVmghtSplit]:
        return [ *self.split_from_id.values() ]

    def caption_style(self, size_mult: float) -> str:
        style_text = self.__style_caption_text().format(
            oc="{",
            cc="}",
            fs=int(24 * size_mult)
        )
        return style_text

    def __style_caption_text(self) -> str:
        return """QLabel {oc}
            background: #00ffffff;
            font: {fs}px bold;
            color: #000;
            border: 0px hidden;
            text-align: center;
        {cc}"""

    def background_style(self, size_mult: float) -> str:
        border_color = self.status
        if self.status.is_selected:
            if self.status.is_success and self.status.is_current:
                border_color = DVgameStatus.CURRENT
            else:
                border_color = DVgameStatus.SELECTED
        style_text = self.__style_background_text().format(
            bg=DVstatusColors.get_color_from_status(self.status),
            bd=DVstatusColors.get_color_from_status(border_color),
            oc="{",
            cc="}",
            bw=int(2 * size_mult),
            br=int(size_mult),
            id=self.name.id
        )
        return style_text

    def __style_background_text(self) -> str:
        return """QWidget QLabel {oc}
            background: {bg};
            border: {bw}px solid {bd};
            border-radius: {br}px;
            {cc}
        """

    def add_split(self, other: dict) -> None:
        if other["split_id"] == "":
            return
        other = { "parent": self, **other }
        new_split = DVmghtSplit(**other)
        self.split_from_id[new_split.id] = new_split

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

    class packageSettings():
        def __init__(
            self,
            display_counter: bool = False,
            game_bg_img: bool = False,
            split_bg_img: bool = False,
            default_split_type: str = "linear",
            number_of_hits: int = 1,
            hit_captions: list[str] = None,
            **kwargs
        ):
            self.display_counter = display_counter
            self.game_bg_img = game_bg_img
            self.split_bg_img = split_bg_img
            self.default_split_type = DVsplitTypes(default_split_type)
            self.number_of_hits = number_of_hits
            self.hit_captions: list[str] = [ "Hit" * self.number_of_hits ]
            if len(hit_captions) <= self.number_of_hits:
                self.hit_captions[:len(hit_captions)] = [
                    item or "Hit" for item in hit_captions
                ]
            else:
                raise TypeError(
                    "DVmghtPackage.settings.__init__() argument, 'hit_captions', malformed:\n"
                    + str(hit_captions)
                )
            self.__future_proof = {**kwargs}

    def __init__(
        self,
        path: str,
        package: dict[str | bool | list[str]],
        repository: dict[str | list[str]],
        games: list[dict] | None = None,
        settings: list[dict] | None = None,
        **kwargs
    ):
        self.repository = self.packageRepo(path=path, **repository)
        self.settings = self.packageSettings(**settings)
        self.name: str = package["name"]
        self.version: str = package["version"]
        self.id: str = package["package_id"]
        self._games: list[str] = package["games"]
        self.games: list[DVmghtGame] = []
        self.game_from_id: dict[str, DVmghtGame] = {}
        self._has_splits: bool = package["has_splits"]
        self.__future_proof = {**kwargs}

        if games != None:
            self.load_games(games)

    def load_games(self, games_to_load: list[dict]):
        for raw_game in games_to_load:
            raw_game = {"parent": self, **raw_game}
            self.games.append(DVmghtGame(**raw_game))
            self.game_from_id[self.games[-1].name.id] = self.games[-1]
