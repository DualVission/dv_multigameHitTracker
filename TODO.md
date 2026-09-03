README.md:
  - [ ] End User explanation
  - [ ] Package Creator (own document?)

Classes:
- Package Classes:
  - DVmghtSplit:
    - [ ] Update PB to reflect multiple hit types
    - [ ] TODO
  - DVmghtGame:
    - [ ] Update PB to reflect multiple hit types
  - ZIP Tools
    - [ ] Pseudo Glob ZIP items
    - [ ] Package from ZIP
    - [ ] Graphics from ZIP (PIL?)
    - [ ] TODO

Interface:
- State Loading:
  - [ ] User PB loading
  - [ ] Save recover status
  - [ ] TODO
- Options:
  - [ ] Per Package Options:
    - [ ] Custom Captions
    - [ ] Disable Game Tile Background Images
    - [ ] TODO
- Image Handling:
  - [ ] TODO

Asset:
- Images:
  - Hit Type Icons:
    - These are default icons creators can use without needing to make assets.
    - [x] Heart
    - [x] Shield
    - [ ] Bomb/Explosion
    - [ ] Sunshine/Storm Clouds
    - [ ] Balloon Pop

Interface:
- Options:
  - [ ] NDI GUI scaling
  - [ ]

GUI:
- Content Window:
  - [ ] TODO
- Lib:
  - Qt MGHT:
    - Game Tile:
      - [ ] Custom Background (how?)
      - [ ] User Caption (from Content Window)
    - Split Tile <= Qt Split Widget:
      - Data:
        - [ ] Split ID
        - [ ] Caption
        - [ ] Selectable (whether to enable cursor interaction)
        - [ ] Hit Counters
      - Qt Stuff (For Selectable):
        - On Hover
        - Unhide child splits on activate
        - Hide child splits on unactivate
        - Talk to Clock
        - Hit Displays
    - Qt Dynamic Split Viewer:
      - This is for Content Window (User scrollable)
      - [ ] TODO
    - Qt Split Status Display:
      - This is for NDI (Displays current split, prior split, and as many upcoming splits as possible)
      - [ ] TODO 
  - Clock:
    - [ ] TODO
- NDI Options:
  - Generic Window:
    - [ ] self.resizeEvent() => If user resizes window geo => Options.game_board_size?
    - [ ] self.closeEvent()  => If user clicks x           => self.hide()
    - [ ] self. hide()       => Should overload closeEvent instead if possible
    - [ ] Report to Content Window
    - [ ] Receive update commands from Content Window
  - Game Status Display:
    - [ ] Would sandwiching it in layouts with spacers prevent the size from over expanding?
  - Split Status Display:
    - This will need to be more explicit with sizing
    - [ ] Prerequisite! DVmghtSplit
    - [ ] Prerequisite! SplitTile