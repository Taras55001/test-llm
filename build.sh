#!/bin/bash

# Оновлення системи та встановлення необхідних пакетів
sudo pacman -Syu --noconfirm
sudo pacman -S --needed --noconfirm gcc python3 portaudio

# Створити віртуальне оточення
python3 -m venv venv
source venv/bin/activate

# Оновити pip
pip install --upgrade pip

# Встановити залежності
pip install -r requirements.txt

# Запустити основний скрипт
python main.py

# Деактивувати віртуальне оточення
deactivate

