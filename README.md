### Описание

Финальный проект 9-го спринта "API"
Предоставляет доступ к API проекта Yatube

Выполнил [Полина Стрельникова](https://https://github.com/malinpolin)

### Установка:

#### 1. Клонировать репозиторий в рабочую директорию на компьютере:

##### Linux или MacOS:
```bash
git clone git@github.com:malinpolin/api_final_yatube.git
```
##### Windows:
```bash
git clone https://github.com/malinpolin/api_final_yatube.git
```

#### 2. Перейти в директорию /api_final_yatube:

```bash
cd api_final_yatube/
```

#### 3. Cоздать и активировать виртуальное окружение:

##### Linux или MacOS:
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
##### Windows:
```bash
python -m venv venv
```
```bash
source venv/Scripts/activate
```

#### 4. Обновить pip:
##### Linux или MacOS
```bash
python3 -m pip install --upgrade pip
```
##### Windows:
```bash
python3 -m pip install --upgrade pip
```

#### 5. Установить зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

#### 6. Выполнить миграции:
##### Linux или MacOS
```bash
python3 manage.py migrate
```
##### Windows:
```bash
python manage.py migrate
```

#### 7. Запустить проект:
##### Linux или MacOS
```bash
python3 manage.py runserver
```
##### Linux или MacOS
```bash
python manage.py runserver
```

### Примеры

#### 1. Запрос к корневому эндпоинту:
GET-запрос http://127.0.0.1:8000/api/v1/

> Ответ:
```json
{
    "posts": "http://127.0.0.1:8000/api/v1/posts/",
    "groups": "http://127.0.0.1:8000/api/v1/groups/",
    "follow": "http://127.0.0.1:8000/api/v1/follow/"
}
```

#### 2. Получение токена:
POST-запрос http://127.0.0.1:8000/api/v1/jwt/create/

```json
{
    "username": "string",
    "password": "string"
}
```
#### 3. Получение списка постов:
GET-запрос http://127.0.0.1:8000/api/v1/posts/

> Ответ:
```json
{
  "count": 123,
  "next": "http://127.0.0.1:8000/api/v1/posts/?offset=400&limit=100",
  "previous": "http://127.0.0.1:8000/api/v1/posts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

#### 4. Добавление комментария к посту:
POST-запрос http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/

```json
{
    "text": "string"
}
```

### 5. Получение информации о группе:
GET-запрос http://127.0.0.1:8000/api/v1/groups/{id}/

> Ответ:
```json
{
  "id": 0,
  "title": "string",
  "slug": "string",
  "description": "string"
}
```