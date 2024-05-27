# Курсовая работа №3
___
### Описание работы
#### Функция, которая выводит на экран список из 5 последних выполненных клиентом операций
```text
# Пример вывода для одной операции:
14.10.2018 Перевод организации
Visa Platinum 7000 79** **** 6361 -> Счет **9638
82771.72 руб.
```
#### Виртуальное окружение
* poetry
#### Используемые библиотеки
* json
* datetime
* os.path
#### Тестирование
* pytest / pytest-cov
___
## Начало работы
### Клонирование репозитория
```bash
git clone git@github.com:RomanPecheritsa/coursework3.git
```

### Настройка зависимостей poetry
#### Установка poetry <https://python-poetry.org/docs/>
```bash
cd coursework3/
poetry install
```
### Запуск функции
```bash
poetry run go
```
### Запуск тестирования и показ процента покрытия
```bash
cd tests
pytest --cov coursework3 --cov-report term-missing
```