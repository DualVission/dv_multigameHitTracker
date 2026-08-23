cd ..
@echo off
setlocal ENABLEDELAYEDEXPANSION
set inputDir=./dv_MGHT/gui/ui/*
set outputDir=./dv_MGHT/gui/gen/

cd ./dv_MGHT/gui/ui/

for /r %%f in (*) do (
  set full=%%f
  set inputFile=!full:~48!
  set outputFile=ui_!full:~48,-3!.py
  pyside6-uic "!inputFile!" -o "!outputFile!"
)

for /r %%f in (ui_*.py) do (
    move /y %%f "../gen/"
)

set /p hi=""