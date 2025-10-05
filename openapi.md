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

**Responses:** 

**200** _'Successful Response'_

**Content-Type**: `application/json`

```json
{
  "email": "sarapayne@example.com",
  "is_staff": false,
  "last_login": null,
  "id": 1235
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

**Responses:** 

**200** _'Successful Response'_

**Content-Type**: `application/json`

```json
{
  "access": "ipsum illum reiciendis",
  "refresh": "Hic veniam repellendus libero tellus. Lorem",
  "expired_at": "1975-04-27T14:00:50.180380+00:00"
}
```

**422** _'Validation Error'_

**Content-Type**: `application/json`

```json
{
  "detail": [
    {
      "loc": [],
      "msg": "architecto officiis placeat officiis",
      "type": "ut accusantium a exercitationem nobis vitae"
    },
    {
      "loc": [],
      "msg": "dolor reiciendis",
      "type": "sit Lorem ipsum nunc culpa! a possimus illum dolor"
    },
    {
      "loc": [
        "Hic quas accusantium odit elit. ipsum mattis"
      ],
      "msg": "esse libero nunc vehicula dolor quas",
      "type": ""
    },
    {
      "loc": [
        "mattis odit enim molestias, Hic a cursus culpa! ut",
        "ipsum, ipsum, cursus Nullam elit.",
        8481
      ],
      "msg": "veniam Hic Nullam adipisicing",
      "type": ""
    }
  ]
}
```


## Me

- Authorizations: **`CustomHTTPBearer`** _(http, bearer)_

**Endpoint:** **`GET`** [localhost:8000/v1/user/me/]()

**Responses:** 

**200** _'Successful Response'_

**Content-Type**: `application/json`

```json
{
  "email": "nfranklin@example.com",
  "is_staff": true,
  "id": 6130
}
```


## Partial Update

- Authorizations: **`CustomHTTPBearer`** _(http, bearer)_

**Endpoint:** **`PATCH`** [localhost:8000/v1/user/me/]()

**Responses:** 

**200** _'Successful Response'_

**Content-Type**: `application/json`

```json
{
  "email": "kimberlystephens@example.org",
  "is_staff": true,
  "last_login": "1999-05-05T01:00:00.856810+00:00",
  "id": 8006
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
