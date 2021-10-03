# Документация к API Yatube (v1)

## Как запустить проект:

Если вы собираетесь работать из командной строки в **windows**, вам может
 потребоваться Bash. скачать его можно по ссылке:
 [GitBash](https://gitforwindows.org/) ([Git-2.33.0.2-64-bit.exe](https://github.com/git-for-windows/git/releases/download/v2.33.0.windows.2/Git-2.33.0.2-64-bit.exe)).

Так же при работе в **windows** необходимо использовать **python** вместо
 **python3**

Последнюю версию **python** ищите на официальном сайте
 [https://www.python.org/](https://www.python.org/downloads/)

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/zhss1983/api_final_yatube
```

```
cd api_final_yatube
```

Создать и активировать виртуальное окружение:

```
python -m venv env
```

- linux
>```
>source env/bin/activate
>```
- windows
>```
>source env/Scripts/activate
>```

Установить зависимости из файла **requirements.txt**:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Работа с эндпоинтами:

### Работа с публикациями:

**Чтение** доступно *всем пользователям* без исключения, **добавлять** новые 
 записи смогут только *зарегистрированные пользователи*, а **изменять** или
 **удалять** записи смогут только *авторы* этих записей. 

#### Получение публикаций

Получить список всех публикаций. При указании параметров **limit** и **offset**
 результаты будут переданы постранично.

GET: [/api/v1/posts/](http://127.0.0.1:8000/api/v1/posts/)

Ответ, статус код 200:

```JSON
[
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2019-08-24T14:15:22Z",
      "image": "string",
      "group": 0
    }
]
```


Параметры передаваемые в запрос:
>**limit**: тип integer, целое положительное число. Соответствует количеству 
> публикаций, выводимых на одну страницу.
>
>**offset**: тип integer, целое положительное число. Номер страницы после
> которой начинать выдачу.

GET: [/api/v1/posts/?offset=400&limit=100](http://127.0.0.1:8000/api/v1/posts/?offset=300&limit=100)

Ответ, статус код 200:

```JSON
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2019-08-24T14:15:22Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

#### Получение одной конкретной публикации

Получить конкретную публикацию возможно используя её **id**.

Параметр пути, передаваемый в GET запросе:
>**id**: тип integer, целое положительное число. Соответствует уникальному 
> идентификатору публикации.

GET: api/v1/posts/{id}/

GET: [api/v1/posts/0/](http://127.0.0.1:8000/api/v1/posts/0/)

Ответ, статус код 200:

```JSON
[
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2019-08-24T14:15:22Z",
      "image": "string",
      "group": 0
    }
]
```

Ответ, статус код 404:

```JSON
{
  "detail": "Страница не найдена."
}
```