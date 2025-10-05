# Workflow App

> [!INFO] Workflow App system
> [AI workflow system](http://localhost:8000/docs)
> version: 0.0.1

---

## Authorizations

**`CustomHTTPBearer`** _(http, bearer)_

---

> health-check

## Health Check

- Authorizations: **`None`**

**Endpoint:** **`GET`** [localhost:8000/v1/health_check/]()

**Request:** 

**`None`**

**Responses:** 

**200** _'Successful Response'_

**Content-Type**: `application/json`

```json
null
```

> user

## Register User Endpoint

- Authorizations: **`None`**

**Endpoint:** **`POST`** [localhost:8000/v1/user/register/]()

**Request:** 

**Content-Type**: `application/json`

```json
{
  "email": "omartaylor@example.org",
  "raw_password": "adipisicing congue. mattis"
}
```


**Responses:** 

**200** _'Successful Response'_

**Content-Type**: `application/json`

```json
{
  "email": "justin39@example.com",
  "is_staff": false,
  "id": 247
}
```

**422** _'Validation Error'_

**Content-Type**: `application/json`

```json
{
  "detail": []
}
```


## Login

- Authorizations: **`None`**

**Endpoint:** **`POST`** [localhost:8000/v1/user/login/]()

**Request:** 

**Content-Type**: `application/json`

```json
{
  "email": "callahanchristopher@example.org",
  "raw_password": "exercitationem"
}
```


**Responses:** 

**200** _'Successful Response'_

**Content-Type**: `application/json`

```json
{
  "access": "reiciendis modi quas sit dolor a nec libero a a ut",
  "refresh": "accusantium vitae consectetur",
  "expired_at": "1993-01-22T19:19:41.849646+00:00"
}
```

**422** _'Validation Error'_

**Content-Type**: `application/json`

```json
{
  "detail": [
    {
      "loc": [
        6568,
        "cursus",
        8901,
        "dui modi exercitationem libero congue. molestias,"
      ],
      "msg": "exercitationem exercitationem Lorem enim congue.",
      "type": "vitae mattis tellus. reprehenderit placeat esse a"
    },
    {
      "loc": [
        "cursus reprehenderit nunc dui",
        7518,
        8106
      ],
      "msg": "enim",
      "type": "repellendus nunc Nullam amet Lorem sit Nullam sit"
    },
    {
      "loc": [
        384,
        "repellendus nec architecto molestias, mattis elit."
      ],
      "msg": "",
      "type": "cursus architecto mattis mattis dolor nobis Lorem"
    }
  ]
}
```


## Me

- Authorizations: **`CustomHTTPBearer`** _(http, bearer)_

**Endpoint:** **`GET`** [localhost:8000/v1/user/me/]()

**Request:** 

**`None`**

**Responses:** 

**200** _'Successful Response'_

**Content-Type**: `application/json`

```json
{
  "email": "nathan44@example.org",
  "is_staff": true,
  "id": 8918
}
```


## Partial Update

- Authorizations: **`CustomHTTPBearer`** _(http, bearer)_

**Endpoint:** **`PATCH`** [localhost:8000/v1/user/me/]()

**Request:** 

**Content-Type**: `application/json`

```json
{
  "raw_password": "dolor nobis quas mattis repellendus reprehenderit ut Lorem illum ipsum, Lorem ipsum dui culpa! a molestias, Nullam libero architecto reiciendis nunc",
  "is_staff": true
}
```


**Responses:** 

**200** _'Successful Response'_

**Content-Type**: `application/json`

```json
{
  "email": "kevin87@example.org",
  "is_staff": false,
  "id": 1145
}
```

**422** _'Validation Error'_

**Content-Type**: `application/json`

```json
{}
```

---
