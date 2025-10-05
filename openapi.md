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
"quas culpa! accusantium nunc"
```

> user

## Register User Endpoint

- Authorizations: **`None`**

**Endpoint:** **`POST`** [localhost:8000/v1/user/register/]()

**Request:** 

**Content-Type**: `application/json`

```json
{
  "email": "melissasweeney@example.net",
  "raw_password": "officiis vitae exercitationem Nullam odit a mattis libero repellendus Nullam possimus"
}
```


**Responses:** 

**200** _'Successful Response'_

**Content-Type**: `application/json`

```json
{
  "email": "danieldustin@example.com",
  "id": 2047
}
```

**422** _'Validation Error'_

**Content-Type**: `application/json`

```json
{}
```


## Login

- Authorizations: **`None`**

**Endpoint:** **`POST`** [localhost:8000/v1/user/login/]()

**Request:** 

**Content-Type**: `application/json`

```json
{
  "email": "katherine87@example.net",
  "raw_password": "Enim congue. cursus tellus. enim Lorem libero Nullam libero elit. Hic tellus. congue. cursus exercitationem dui"
}
```


**Responses:** 

**200** _'Successful Response'_

**Content-Type**: `application/json`

```json
{
  "access": "amet sit accusantium dolor magnam, vehicula nobis",
  "refresh": "Lorem nec molestias, Hic dolor vitae",
  "expired_at": "1988-01-14T01:39:31.511464+00:00"
}
```

**422** _'Validation Error'_

**Content-Type**: `application/json`

```json
{}
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
  "email": "kaylamills@example.org",
  "last_login": "1989-05-29T04:08:09.591019+00:00",
  "id": 2284
}
```


## Partial Update

- Authorizations: **`CustomHTTPBearer`** _(http, bearer)_

**Endpoint:** **`PATCH`** [localhost:8000/v1/user/me/]()

**Request:** 

**Content-Type**: `application/json`

```json
{
  "raw_password": "officiis ipsum, enim amet ut odit consectetur adipisicing nunc vehicula Lorem dui",
  "last_login": "1998-01-11T11:05:54.234770+00:00"
}
```


**Responses:** 

**200** _'Successful Response'_

**Content-Type**: `application/json`

```json
{
  "email": "jjones@example.com",
  "last_login": null,
  "id": 6650
}
```

**422** _'Validation Error'_

**Content-Type**: `application/json`

```json
{
  "detail": []
}
```

---
