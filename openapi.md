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
  "email": "kaitlyncunningham@example.net",
  "raw_password": "nobis reprehenderit adipisicing odit nobis elit. veniam culpa! ipsum arcu"
}
```


**Responses:** 

**200** _'Successful Response'_

**Content-Type**: `application/json`

```json
{
  "email": "espinozabrian@example.net",
  "id": 2144
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
  "email": "juarezdeborah@example.org",
  "raw_password": "repellendus nec Hic ipsum accusantium repellendus vehicula cursus ut"
}
```


**Responses:** 

**200** _'Successful Response'_

**Content-Type**: `application/json`

```json
{
  "access": "mattis ut veniam veniam adipisicing arcu amet nec",
  "refresh": "",
  "expired_at": "1970-07-08T09:23:01.811030+00:00"
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
  "email": "gary73@example.net",
  "last_login": "1977-09-22T23:15:31.580836+00:00",
  "id": 9896
}
```


## Partial Update

- Authorizations: **`CustomHTTPBearer`** _(http, bearer)_

**Endpoint:** **`PATCH`** [localhost:8000/v1/user/me/]()

**Request:** 

**Content-Type**: `application/json`

```json
{
  "email": null,
  "raw_password": "culpa! reprehenderit nunc libero illum consectetur quas a arcu repellendus odit dui",
  "is_staff": true
}
```


**Responses:** 

**200** _'Successful Response'_

**Content-Type**: `application/json`

```json
{
  "email": "nathanielhardin@example.com",
  "last_login": null,
  "id": 269
}
```

**422** _'Validation Error'_

**Content-Type**: `application/json`

```json
{}
```

---
