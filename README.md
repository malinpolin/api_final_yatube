## Описание

Финальный проект 9-го спринта "API".

Предоставляет доступ к API проекта Yatube.

Выполнила [Полина Стрельникова](https://github.com/malinpolin).

_____________________________________________________________________________________________________________________________________
## Установка:

### 1. Клонировать репозиторий в рабочую директорию на компьютере:

##### Linux или MacOS
```bash
git clone git@github.com:malinpolin/api_final_yatube.git
```
##### Windows
```bash
git clone https://github.com/malinpolin/api_final_yatube.git
```

### 2. Перейти в директорию /api_final_yatube: 

```bash
cd api_final_yatube/
```

### 3. Cоздать и активировать виртуальное окружение: 

##### Linux или MacOS
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
##### Windows
```bash
python -m venv venv
```
```bash
source venv/Scripts/activate
```

### 4. Обновить pip:
##### Linux или MacOS
```bash
python3 -m pip install --upgrade pip
```
##### Windows
```bash
python -m pip install --upgrade pip
```

### 5. Установить зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

### 6. Выполнить миграции:
##### Linux или MacOS
```bash
python3 manage.py migrate
```
##### Windows
```bash
python manage.py migrate
```

### 7. Запустить проект:
##### Linux или MacOS
```bash
python3 manage.py runserver
```
##### Windows
```bash
python manage.py runserver
```

_____________________________________________________________________________________________________________________________________
## Примеры

### 1. Получение списка постов:
:green_heart:GET-запрос /api/v1/posts/

> Ответ:
>```json
>[
>  {
>    "id": 0,
>    "author": "string",
>    "text": "string",
>    "pub_date": "2021-10-14T20:41:29.648Z",
>    "image": "string",
>    "group": 0
>  }
>]
>```


### 2. Получение списка постов с параметрами limit и offset:
:green_heart:GET-запрос /api/v1/posts/?offset=300&limit=100/

> Ответ:
>```json
>{
>  "count": 123,
>  "next": "http://127.0.0.1:8000/api/v1/posts/?offset=400&limit=100",
>  "previous": "http://127.0.0.1:8000/api/v1/posts/?offset=200&limit=100",
>  "results": [
>    {
>      "id": 0,
>      "author": "string",
>      "text": "string",
>      "pub_date": "2021-10-14T20:41:29.648Z",
>      "image": "string",
>      "group": 0
>    }
>  ]
>}
>```

### 3. Создание публикации:
:blue_heart:POST-запрос /api/v1/posts/

*Обязательные поля*: **text**

> Тело запроса:
>```json
>{
>  "text": "string",
>  "image": "string",
>  "group": 0
>}
>```

> Ответ:
>```json
>{
>  "id": 0,
>  "author": "string",
>  "text": "string",
>  "pub_date": "2019-08-24T14:15:22Z",
>  "image": "string",
>  "group": 0
>}

### 4. Получение публикации:
:green_heart:GET-запрос /api/v1/posts/{post_id}/

> Ответ:
>```json
>{
>  "id": 0,
>  "author": "string",
>  "text": "string",
>  "pub_date": "2019-08-24T14:15:22Z",
>  "image": "string",
>  "group": 0
>}

### 5. Обновление публикации:
:purple_heart:PUT-запрос /api/v1/posts/{post_id}/

*Обязательные поля*: **text**

> Тело запроса:
>```json
>{
>  "text": "string",
>  "image": "string",
>  "group": 0
>}
>```

> Ответ:
>```json
>{
>  "id": 0,
>  "author": "string",
>  "text": "string",
>  "pub_date": "2019-08-24T14:15:22Z",
>  "image": "string",
>  "group": 0
>}

### 6. Частичное обновление публикации:
:orange_heart:PATCH-запрос /api/v1/posts/{post_id}/

*Обязательные поля*: **text**

> Тело запроса:
>```json
>{
>  "text": "string",
>  "image": "string",
>  "group": 0
>}
>```

> Ответ:
>```json
>{
>  "id": 0,
>  "author": "string",
>  "text": "string",
>  "pub_date": "2019-08-24T14:15:22Z",
>  "image": "string",
>  "group": 0
>}

### 7. Удаление публикации:
:heart:DELETE-запрос /api/v1/posts/{post_id}/

> Ответ:
>```json
>{
>  "id": 0,
>  "author": "string",
>  "text": "string",
>  "pub_date": "2019-08-24T14:15:22Z",
>  "image": "string",
>  "group": 0
>}

### 8. Получение списка комментариев к публикации:
:green_heart:GET-запрос /api/v1/posts/{post_id}/comments/

> Ответ:
>```json
>[
>  {
>    "id": 0,
>    "author": "string",
>    "text": "string",
>    "created": "2021-10-14T20:41:29.648Z",
>    "post": 0
>  }
>]
>```

### 9. Добавление комментария:
:blue_heart:POST-запрос /api/v1/posts/{post_id}/comments/

*Обязательные поля*: **text**

> Тело запроса:
>```json
>{
>  "text": "string",
>}
>```

> Ответ:
>```json
>{
>  "id": 0,
>  "author": "string",
>  "text": "string",
>  "created": "2021-10-14T20:41:29.648Z",
>  "post": 0
>}
>```

### 10. Получение комментария:
:green_heart:GET-запрос /api/v1/posts/{post_id}/comments/{comment_id}/

> Ответ:
>```json
>{
>  "id": 0,
>  "author": "string",
>  "text": "string",
>  "created": "2021-10-14T20:41:29.648Z",
>  "post": 0
>}

### 11. Обновление комментария:
:purple_heart:PUT-запрос /api/v1/posts/{post_id}/comments/{comment_id}/

*Обязательные поля*: **text**

> Тело запроса:
>```json
>{
>  "text": "string",
>}
>```

> Ответ:
>```json
>{
>  "id": 0,
>  "author": "string",
>  "text": "string",
>  "created": "2021-10-14T20:41:29.648Z",
>  "post": 0
>}

### 12. Частичное обновление комментария:
:orange_heart:PATCH-запрос /api/v1/posts/{post_id}/comments/{comment_id}/

*Обязательные поля*: **text**

> Тело запроса:
>```json
>{
>  "text": "string",
>}
>```

> Ответ:
>```json
>{
>  "id": 0,
>  "author": "string",
>  "text": "string",
>  "created": "2021-10-14T20:41:29.648Z",
>  "post": 0
>}

### 13. Удаление комментария:
:heart:DELETE-запрос /api/v1/posts/{post_id}/comments/{comment_id}/

### 14. Получение списка сообществ:
:green_heart:GET-запрос /api/v1/groups/

> Ответ:
>```json
>[
>  {
>    "id": 0,
>    "title": "string",
>    "slug": "string",
>    "description": "string",
>  }
>]
>```

### 15. Информация о сообществе:
:green_heart:GET-запрос /api/v1/groups/{group_id}/

> Ответ:
>```json
>{
>  "id": 0,
>  "title": "string",
>  "slug": "string",
>  "description": "string"
>}
>```

### 16. Получение списка подписок пользователя:
:green_heart:GET-запрос /api/v1/follow/

> Ответ:
>```json
>[
>  {
>    "user": "string",
>    "following": "string"
>  }
>]
>```

### 17. Добавление подписки пользователя:
:blue_heart:POST-запрос /api/v1/follow/

*Обязательные поля*: **following**

> Тело запроса:
> ```json
>{
>  "following": "string"
>}
>```

> Ответ:
>```json
>{
>  "user": "string",
>  "following": "string"
>}
>```

### 18. Получение JWT-токена:
:blue_heart:POST-запрос /api/v1/jwt/create/

*Обязательные поля*: **username, password**

> Тело запроса:
>```json
>{
>  "username": "string",
>  "password": "string"
>}
>```

> Ответ:
>```json
>{
>  "refresh": "string",
>  "access": "string"
>}
>```

### 19. Обновление JWT-токена:
:blue_heart:POST-запрос /api/v1/jwt/refresh/

*Обязательные поля*: **refresh**

> Тело запроса:
>```json
>{
>  "refresh": "string"
>}
>```

> Ответ:
>```json
>{
>  "access": "string"
>}
>```

### 20. Проверка JWT-токена:
:blue_heart:POST-запрос /api/v1/jwt/verify/

*Обязательные поля*: **token**

> Тело запроса:
>```json
>{
>  "token": "string"
>}
>```
>
