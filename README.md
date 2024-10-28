# Инструкции по установке

## Требования
- Python 3.7+
- Pillow (Python Imaging Library) для работы с изображениями

## Установка

1. Склонируйте репозиторий на локальный компьютер:
   ```bash
   git clone https://github.com/ваш_пользователь/blackjack-game.git
   cd blackjack-game
   ```
2. Установите необходимые зависимости:

  ```bash
  pip install -r requirements.txt
  ```


## Запуск игры
Чтобы запустить игру, выполните следующую команду:

```bash
python main.py
```
## Использование
## Начало игры: При запуске игры игрок и дилер получают по две стартовые карты.

## Действия игрока:

 Взять карту: Добавляет карту игроку. Если сумма очков превышает 21, игрок проигрывает.
 Остановиться: Завершает ход игрока и передает ход дилеру.
 Действия дилера: Дилер (бот) будет брать карты, пока его очки не достигнут или не превысят 17.

## Определение победителя: Победитель определяется по стандартным правилам блэкджека, где выигрывает тот, у кого больше очков, но не превышает 21.
