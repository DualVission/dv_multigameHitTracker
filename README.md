# DualVission's Multigame Hit Tracker 
> dv_MGHT `[diː viː ˈmaɪt]` 

This tool is as described on the tin, a hit tracker for multiple games and their segments. 
 
## Installation 
To use, install the [latest release](https://github.com/DualVission/dv_multigameHitTracker/releases/latest) or 
1. Clone this repository using `git clone https://github.com/DualVission/dv_multigameHitTracker.git`. 
2. Open a terminal in the root of the directory `C:/{path/to}/dv_multigameHitTracker/`. 
   1. Do not open in the subdirectory `./dv_MGHT` as this will not work. 
3. In terminal, run `py -m runMe`. 
 
## Dependencies 
My goal is out of the box usable on [releases](https://github.com/DualVission/dv_multigameHitTracker/releases/latest), but certain features are limited if dependencies are not installed. 
### NDI<sup>®</sup> 
Install [NDI® tools](https://ndi.video/tools). 
 
## Other Packages 
To install additional packages, 
1. Download the package. 
2. Navigate to your Local App Data folder. 
   1. The default on Windows is locatable as `%appdata%` in the address bar on File Explorer. It is located at `C:/Users/{username}/AppData/Roaming/`. 
   2. The default on Linux is locatable as `$HOME`. It is located at `/home/{username}/.local/share/`. 
   3. The default on MacOS is located at `/users/{username}/Library/Application Support/`. 
3. Navigate down to `./DV/dv_mght/packages/`. 
4. Drag the package into the folder. 
5. At this time, only flat folders are supported, but ZIP Archive support as well as subfolder support is planned. 
 
## User Customization 
User customization can be broken into two subcategories: 
 
### Options 
- To access, 
  1. In the content window's ribbon, hover over the `Options` menu. 
  2. Select the option you wish to change. 
  3. Further dialog will appear if it is followed by an ecllipsis `...`. 
- Current Options include: 
  - Dark Mode [On]: As described on the tin 
  - Randomize Order Open on Startup [Off]: When a package is loaded, sets whether the game order randomization panel should be open. 
- Options not implemented: 
  - Status Colors: Sets the colors of status when displayed in the UI 
    - Upcoming [Silver]: Background color of games or splits not yet interacted. 
    - Selected [Cyan]: Background and highlight color of games or splits currently selected within content window. 
    - Current [White]: Background and highlight color of games or splits currently set as current. 
    - Success [Green]: Background color of games or splits completed without a hit. 
    - Failed [Red]: Background color of games or splits where hits are greater than 0. 
  - Enable NDI: When a package is loaded, sets whether to broadcast over NDI LAN. 
### Package Options 
- To access, 
  1. Load a package. 
  2. In the content window's ribbon, hover over the `Options` menu. 
  3. Hover over the `Package Options` submenu to change quick options. 
  4. Click `Package Options...` to open a package options dialog window. 
- Current Options include: 
  - Display Counter [Off]: Only selectable if packages enable display counters. Enables the user to turn display counters on or off. 
- Options not fully implemented: 
  - Display Background Images on Game Tiles [Off]: Only selectable if packages enable display background images on game tiles. Enables the user to turn displaying background images on game tiles on or off. 
  - NDI Game Board Size [default not set, from package?]: When NDI is enabled, this enables the user to set the output resolutions and aspect ratio. 
- Options not implemented: 
  - Display Background Images on Split Tiles [Off]: Only selectable if packages enable display background images on split tiles. Enables the user to turn displaying background images on split tiles on or off. 
  - NDI Game Board Scale [2.0]: When NDI is enabled, this enables the user to choose the size elements should be scaled in the NDI output. 


# Terminology 
## What is a hit? 
Much harder to define than what you would think. For the purposes of my creation, a hit and/or damage is as described by [Team Hitless](https://teamhitless.com/). 
> Team Hitless 
> 
> A **Hit** is classified as a loss of health or a stagger caused by an enemy or trap[...] attacks from enemies that deal no damage and also status effects, such as poison [...] as a result of an enemy attack. 
> 
> **Damage** is classified as any loss of health, including environment damage, fall damage, [...] attacks from enemies that deal damage and also status effects, such as poison [...] as a result of an enemy attack. 
> 
> Don't get confused[...] 

But a hit tracker is just that, a tracker, something that counts a value across multiple games and/or segments. 

## What is a game? 
A game is as defined by [Wiktionary](https://en.wiktionary.org/wiki/game), but more specifically a video game. 
> Wiktionary 
> 
> game `[geɪm]` 
> 
> 1. A playful or competitive activity. 
> 
>    2. [...] An activity described by a set of rules, especially for the purpose of entertainment, often competitive or having an explicit goal. 
> 
>    4. [...] A particular instance of playing a game. 
> 
>    10. [...] One's manner, style, or performance in playing a game. 
> 
> video game `[ˈvɪdiːəʊ ɡeɪm]` 
> 
> 1. A type of game, existing as and controlled by software, usually run by a video game console or a computer[...]. 

But a game should be considered in a more abstract sense. In actuality, a game itself, in the context of dv_MGHT, can be thought of as an explicitly declared large split or segment as part of a larger run. 
 
## What is a split? 
I was genuinely shocked by the number of websites that were not blocked by my employer in relation to speedrunning, but I was also shocked by the lack of semiformal definition of a split and/or segment despite the popularity of the terminology within the community. So that leaves me to use [Wiktionary](https://en.wiktionary.org/wiki/split) again and further providing my own definition in this context. 
> Wiktionary 
> 
> split `[splɪt]` 
> 
> Noun 
> 
> 4. A piece that is split off [...]; a splinter; a fragment 
> 
> Verb 
> 
> 1. [...] To divide [...] 
> 
> segment `[sɛɡ mɛnt]` 
> 
> Noun 
> 
> 2. One of the parts into which any body [...] is divided; a part divided or cut off; a section; a portion. 
> 
> 3. [...] A portion 
It can then be extrapolated that the following definition would apply in speedruns. 
> 
> <a name="split">split `[splɪt]` or segment `[sɛɡ mɛnt]`</a> 
> 
> A portion of a run or another split, explicitly or implicitly declared, to maintain trackable progress through that portion for comparison between individual runs from a singular runners or trends between multiple runners. 

A distinction can be made further between that delineation is made by a game itself explicitly – such as individual levels in the Super Mario franchise – or implicitly – such as item collection in The Legend of Zelda franchise. 

# Disclaimers 
Yes, I did copy my code, modifications to flow layout, from @Randovania [Randovania](https://github.com/randovania/randovania/). 
Throughout development, I referred back to [Randovania](https://github.com/randovania/randovania/) and @LagoLunatic [Wind Waker Randomizer](https://github.com/lagolunatic/wwrando). Both are projects that I was familiar with the codebase and how users interact with them. I wanted my code to reflect how I felt a software like this should be handled while still being accessible. There are definitely a number of coding conventions that I will be honest and say I wouldn't think of needing, but recognize it will provide flexibility and scalability in the future. 
The code relating to local data is very much inspired by Randovania with heavy modification to support a more flexible package system. 
 

# Legal Disclosures and Disclaimers 
## Application License 
> [!IMPORTANT] 
> DualVission's Multigame Hit Tracker  is a tracker for hits taken in multiple games in segmented runs. 
> 
> Copyright (C) 2026  Zach the DualVission 
> 
> This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. 
> 
> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. 
> 
> You should have received a copy of the GNU General Public License along with this program.  If not, see http://www.gnu.org/licenses/. 
 
## Dependencies and their Licenses 
> [!IMPORTANT] 
> ndi-python: MIT License 
> 
> JSONC-parser: MIT License 
> 
> PyQtDarkTheme: MIT License 
> 
> [NDI®](https://docs.ndi.video/all/developing-with-ndi/sdk/licensing) 
> 
> [Python](https://docs.python.org/3/license.html) 
> 
> [Qt](https://doc.qt.io/qt-6/licensing.html) 
 
## Copyright and Rights Notices 
All copyrights are held by their respective owners. 
Zach the DualVission does not hold any rights to these owners’ contents. 
> [!IMPORTANT] 
> NDI<sup>®</sup> is a registered trademark of Vizrt NDI AB. 
> 
> JSON is maintained as a standard defined by the Internet Engineering Task Force (IETF) as STD 90, Ecma International as ECMA-404, and the joint technical committee of the International Organization for Standardization and the International Electrotechnical Commission as ISO/IEC 21778:2017. 
> 
> Qt is a platform maintained by the Qt Company. 
> 
> The Legend of Zelda, the franchise, its games, and its characters are trademarks of Nintendo Co., Ltd. 

Zach the DualVission is in no way related to or endorsed by these companies – or creators – or their brands. The actions of said persons are not in any way connected to or encouraged by other mentioned parties. 
