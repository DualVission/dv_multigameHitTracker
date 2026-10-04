from __future__ import annotations

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QUrl, Signal, QCoreApplication, QKeyCombination
from pyqthotkey import HotkeyPicker

class QHotkeyPicker(HotkeyPicker):
    hotkeyChanged = Signal(object, object)

    __key_code_map = {}
    for name in [name for name in dir(Qt.Key) if "Key_" in name]:
        key = getattr(Qt, name)
        __key_code_map[key] = name.partition('_')[-1]

    # Manually change name for some keys
    __key_code_map[Qt.Key.Key_Space]      = 'Space'
    __key_code_map[Qt.Key.Key_Adiaeresis] = 'Ä'
    __key_code_map[Qt.Key.Key_Odiaeresis] = 'Ö'
    __key_code_map[Qt.Key.Key_Udiaeresis] = 'Ü'
    __key_code_map[Qt.Key.Key_Equal]      = 'Plus'
    __key_code_map[Qt.Key.Key_Minus]      = 'Minus'

    __in_selection: bool = False
    __selected_key: QKeyCombination | None = None
    def __init__( 
        self, 
        parent=None,
        default_text: str = 'None',
        selection_text: str = '..',
        cancel_key: Qt.Key = Qt.Key.Key_Escape,
        key_filter_enabled: bool = True,
        whitelisted_keys: list[Qt.Key] = [],
        blacklisted_keys: list[Qt.Key] = [
            Qt.Key.Key_Shift,
            Qt.Key.Key_Control,
            Qt.Key.Key_Alt
        ]
    ):
        super(QHotkeyPicker, self).__init__(
            parent,
            default_text,
            selection_text,
            cancel_key,
            key_filter_enabled,
            whitelisted_keys, 
            blacklisted_keys
        )

    def getHotkey(self) -> QKeyCombination | None:
        return self.__selected_key

    def getHotkeyName(self) -> str:
        if self.__selected_key == None:
            return self.getDefaultText()
        return QHotkeyPicker.getKeyName(self.getHotkey())

    def keyPressEvent(self, event):
        return

    def keyReleaseEvent(self, event):
        keys = event.keyCombination()
        self.setHotkey(keys)

    def setHotkey(self, keys: QKeyCombination) -> None:
        if keys.key() == self.getCancelKey():
            self.setText(self.getDefaultText())
            self.__selected_key = None
        elif (
            self.isKeyFilterEnabled()
            and self.getWhitelistedKeys()
            and keys.key() not in self.getWhitelistedKeys()
        ) or (
            self.isKeyFilterEnabled()
            and self.getBlacklistedKeys()
            and keys.key() in self.getBlacklistedKeys()
       ):
            return
        else:
            self.__selected_key = keys
            self.setText(self.getHotkeyName())

        self.__in_selection = False
        self.clearFocus()

        self.hotkeyChanged.emit(
            self.getHotkeyName(),
            self.text()
        )

    @staticmethod
    def getKeyName(keys: QKeyCombination) -> str:
        name_list: list[str] = []
        if keys.keyboardModifiers() & Qt.ShiftModifier:
            name_list.append(QHotkeyPicker.__key_code_map[Qt.Key.Key_Shift])
        if keys.keyboardModifiers() & Qt.ControlModifier:
            name_list.append(QHotkeyPicker.__key_code_map[Qt.Key.Key_Control])
        if keys.keyboardModifiers() & Qt.AltModifier:
            name_list.append(QHotkeyPicker.__key_code_map[Qt.Key.Key_Alt])
        name_list.append(QHotkeyPicker.__key_code_map[keys.key()])

        return "+".join(name_list)

    @staticmethod
    def setKeyName(keys: QKeyCombination | Qt.Key, name: str) -> None:
        if isinstance(keys, QKeyCombination):
            keys = keys.key()
        QHotkeyPicker.__key_code_map[keys] = name
