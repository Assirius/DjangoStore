# DjangoStore
## Интернет магазин одежды

Данный проект представляет интернет магазин одежды. В нем реализованы каталог товаров и личный кабинет пользователя с корзиной товаров,
подтверждение пользователя по почте с использованием Celery, подключена система оплаты через Stripe.

## Требования

Для запуска проекта Django убедитесь, что у вас есть:

- Установленный Python 3 на вашей системе
- Установщик пакетов Pip
- Виртуальная среда (необязательно, но рекомендуется)


## Настройка проекта

1. Клонируйте репозиторий проекта на ваш компьютер.
2. Перейдите в директорию проекта.
3. Создайте виртуальную среду (необязательно):

### Установка venv
1. Если у вас еще не установлен модуль venv, выполните следующую команду в командной строке, чтобы установить его:
pip install venv


### Установка зависимостей
1. Перейдите в корневую папку проекта.

2. Активируйте виртуальное окружение venv следующей командой:
# **source venv/bin/activate**
 
  или для Windows:
# **venv\Scripts\activate**

3. Установите зависимости, указанные в файле requirements.txt, выполнив следующую команду:
**pip install -r requirements.txt**


4. Примените миграции, чтобы создать необходимые таблицы в базе данных:
**python manage.py migrate**

5. Загрузите фикстуры:
 # **python manage.py loaddata products/fixtures/categories.json**
 # **python manage.py loaddata products/fixtures/goods.json**

6. Создайте файл .env на основе файла env.template и обновите необходимые переменные окружения.
   **python manage.py runserver**


## Запуск сервера

  После настройки проекта вы можете запустить сервер разработки:
  **python manage.py runserver**

---

  Сервер будет запущен по адресу http://localhost:8000/. Вы можете открыть этот URL в веб-браузере, чтобы получить доступ к проекту.










