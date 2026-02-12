@echo off
REM Przejdź do folderu projektu
cd /d C:\Users\igorr\Documents\GitHub\awareness

REM Aktywuj wirtualne środowisko
call venv\Scripts\activate.bat

REM Uruchom skrypt Python
python awareness.py

REM Poczekaj na naciśnięcie klawisza, żeby okno nie zniknęło
pause
