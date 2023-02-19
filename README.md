Для запуска проекта необходимо:

Сделайте клон репозитория

если у вас установлен git, то введите в терминале команду:
если настроен ssh: git clone git@github.com:Ramilsas/My-site.git
если настроен https: git clone https://github.com/Ramilsas/My-site.git
Создайте виртуальное окружение

если у вас установлен python3, то введите в терминале команду:
python3 -m venv venv !!! ВАЖНО !!!
если у вас WINDOWS, уточните создание виртуального окружения
https://docs.python.org/3/library/venv.html
Активируйте виртуальное окружение

если у вас установлен python3, то введите в терминале команду:
source venv/bin/activate !!! ВАЖНО !!!
если в вас WINDOWS, уточните активацию виртуального окружения
https://docs.python.org/3/library/venv.html
Установите зависимости

введите в терминале команду: pip install -r reqirements.txt
Сделайте миграции

введите в терминале команду: python manage.py migrate
Запустите проект

введите в терминале команду: python manage.py runserver
Создайте суперпользователя

введите в терминале команду: python manage.py createsuperuser