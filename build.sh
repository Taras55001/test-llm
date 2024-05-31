#!/bin/bash

# Створити віртуальне оточення
python3 -m venv venv
source venv/bin/activate

# Оновити pip
pip install --upgrade pip

# Встановити залежності
pip install -r requirements.txt

# Запустити основний скрипт
python test_micro.py

# Деактивувати віртуальне оточення
deactivate

