@echo off

REM Створити віртуальне оточення
python -m venv venv
call venv\Scripts\activate

REM Оновити pip
pip install --upgrade pip

REM Встановити залежності
pip install -r requirements.txt

REM Запустити основний скрипт
python test_micro.py

REM Деактивувати віртуальне оточення
call venv\Scripts\deactivate