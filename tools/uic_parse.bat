cd ..
@echo off
setlocal ENABLEDELAYEDEXPANSION
set inputDir=./dv_MGHT/gui/ui/*
set outputDir=./dv_MGHT/gui/gen/

cd ./dv_MGHT/gui/ui/
echo %cd%

set length = 0

for /l %%a in (0,1,1000) DO (
  if "!cd:~%%a,1!"=="" (
    set /a length = %%a + 1
    goto EXIT
  )
)

:EXIT
echo %length%

for /r %%f in (*) do (
  set full=%%f
  set inputFile=!full:~%length%!
  set outputFile=ui_!full:~%length%,-3!.py
  pyside6-uic "!inputFile!" -o "!outputFile!"
)

for /r %%f in (ui_*.py) do (
    move /y %%f "../gen/"
)

set /p hi=""