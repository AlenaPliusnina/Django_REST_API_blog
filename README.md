# Django_REST_API_blog /

     Django, Django REST framework, Sqlite3 (локально), PostgreSQL (на Heroku)

Описание проекта:

     Проект созданный на основе Django REST framework представляет собой API для сайта-блога.

Созданый API размещен на Heroku и доступен по ссылке: https://shielded-reaches-49083.herokuapp.com/

Разворачиваем проект локально:

1. Скачайте репозиторий

2. Создайт виртуальное окружение: 
    
       python -m venv env
    
3. Активируйте виртуальное окружение:

       source env/bin/activate
    
4. Чтобы установить все требуемые библиотеки python в новом окружении выполните команду:
     
       pip install -r requirements.txt
    
  Если у вас macOS до выполнения команды pip install -r requirements.txt выполните команду:

    env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install psycopg2==2.8.4
    
  Для предотвращения появления ошибки (error: command 'gcc' failed with exit status 1.) при установке зависимостей.

5. Создайте файл переменных окржения (.env) и добавьте в него значение SECRET_KEY (которое используется в settings.py) для работы приложения.

6. Чтбы запустить сервер введите команду:

       python manage.py runserver
    
7. Для входа в администравтивную панель проекта создайте суперпользователя при помощи команды:

       python manage.py createsuperuser


Описание функционала:

1. / - список всех постов, создание нового поста

   ![Список всех постов](/screenshots/screen_1.png)
   ![Список всех постов](/screenshots/screen_2.png)
   ![Список всех постов](/screenshots/screen_3.png)
   
2. /<int:pk> - детали по конкретному посту

   ![Детали по конкретному посту](/screenshots/screen_4.png)

3. /categories - список категорий и входящих в них постов, создание новой категории

   ![Список категорий](/screenshots/screen_5.png)
   ![Список категорий](/screenshots/screen_6.png)
   ![Список категорий](/screenshots/screen_7.png)

4. /categories/<int:pk> - детали по конкретной категории

   ![Детали по категории](/screenshots/screen_8.png)

5. /admin - вход в административную панель, через которую можно создать пользователей и обновить авторов для уже существующих постов.

   ![Административная панель](/screenshots/screen_9.png)
   ![Административная панель](/screenshots/screen_10.png)
   ![Административная панель](/screenshots/screen_11.png)
   ![Административная панель](/screenshots/screen_12.png)
