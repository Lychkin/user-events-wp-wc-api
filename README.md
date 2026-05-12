# User Events API

Простое REST API на FastAPI для хранения и получения пользовательских событий WordPress WooCommerce.

Сервис использует FastAPI, SQLite, SQLAlchemy, Pydantic

Данные с сервиса можно использовать для аналитики или ML

# Возможности

- Создание пользовательских событий
- Получение списка событий
- Пагинация результатов
- SQLite в качестве базы данных
- Автоматическая Swagger-документация

---

# Структура события

Каждое событие содержит:

| Поле | Тип | Описание |
|---|---|---|
| item_id | integer | ID товара |
| user_id | integer | ID пользователя |
| timestamp | datetime | Время события |
| event | string | Тип события (`view` или `add_to_cart`) |

---

# Требования

- Python 3.10+
- pip

---

# Установка

## 1. Клонирование проекта

```bash
git clone https://github.com/Lychkin/user-events-wp-wc-api.git
cd project
```

## 2. Установка зависимостей

```bash
pip install -r requirements.txt
```

---

# Запуск сервиса

```bash
py main.py
```

После запуска сервис будет доступен по адресу:

```text
http://localhost:8001
```

Swagger документация:
```text
http://localhost/docs
```


# API Documentation

## 1. Получить список событий

### Endpoint

```http
GET /events
```

### Query Parameters

| Параметр | Тип     | Обязательный | Описание                         |
| -------- | ------- | ------------ | -------------------------------- |
| page     | integer | Нет          | Номер страницы                   |
| per_page | integer | Нет          | Количество элементов на страницу |

### Пример запроса

```http
GET /events?page=1&per_page=10
```

### Пример ответа

```json
{
  "page": 1,
  "per_page": 10,
  "total": 2,
  "data": [
    {
      "user_id": 1,
      "item_id": 100,
      "event": "view",
      "id": 0,
      "timestamp": "2025-10-10T12:00:00",
    },
    {
      "user_id": 2,
      "item_id": 101,
      "event": "add_to_cart",
      "id": 1,
      "timestamp": "2025-10-10T12:05:00",
    }
  ]
}
```

## 2. Создать событие

### Endpoint

```http
POST /events
```

### Request Body

```json
{
  "item_id": 100,
  "user_id": 1,
  "event": "view"
}
```

### Допустимые значения event

* `view`
* `add_to_cart`

### Пример ответа

```json
{
  "event": "view",
  "item_id": 100,
  "user_id": 1,
  "timestamp": "2025-10-10T12:00:00",
  "id": 1,
}
```