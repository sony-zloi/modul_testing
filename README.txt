Памятка как делать проект
Директория fraction - корень проекта.
Все команды выполняются из нее.

Чтобы проверить, в какой директории вы находитесь в коммандой строке/терминале
 - Для Windows выполните cd
 - Для Linux/Mac выполните pwd

Чтобы перейти в нужную директорию, используйте команду cd DIRECTORY

Чтобы не было проблем с импортами локальных модулей, установите переменную окружения PYTHONPATH
 - Для Windows выполните set PYTHONPATH=.
 - Для Linux/Mac выполните export PYTHONPATH=.


[Выберете python или python3 в зависимости от того, какой у вас исполняемый файл]

Команды запуска тестов:
> python -m unittest discover -s tests -v

Чтобы запустить тест-метод, в названии которого содержаится строка abc:
> python -m unittest discover -s tests -v -k "abc"


Для проверки покрытия нужен модуль coverage
Установим, если он отстуствует:
> pip (или pip3) install coverage


Запустим тесты и посчитаем покрытие
> python -m coverage run --source . -m unittest discover -s tests -v -k "abc"
Выведем отчет о покрытии
> python -m coverage report
Отчистим существующие подсчеты
> python -m coverage erase

