# Workflow App

> [!INFO] Workflow App system
> [AI workflow system](http://localhost:8000/docs)
> version: 0.0.1

---

## Authorizations

**`CustomHTTPBearer`** _(http, bearer)_

---

> health-check

> [!tip] Health Check

- Authorizations: **`None`**

**Endpoint:** **`GET`** [localhost:8000/v1/health_check/]()

**200** _'Successful Response'_

**Content-Type**: `application/json`

```json
null
```

> user

> [!tip] Register User Endpoint

- Authorizations: **`None`**

**Endpoint:** **`POST`** [localhost:8000/v1/user/register/]()

**200** _'Successful Response'_

**Content-Type**: `application/json`

```json
{
  "email": "richardmorgan@example.net",
  "is_staff": false,
  "id": 7623
}
```

**422** _'Validation Error'_

**Content-Type**: `application/json`

```json
{
  "detail": [
    {
      "loc": [
        "enim ipsum, odit culpa! sit ipsum dui modi dui nec",
        ""
      ],
      "msg": "sit odit a",
      "type": "adipisicing elit. arcu illum congue. arcu"
    },
    {
      "loc": [
        "reprehenderit molestias, veniam dui dolor a",
        3963,
        "Enim"
      ],
      "msg": "vitae esse ipsum amet nunc cursus congue. dui quas",
      "type": "possimus Lorem magnam, Lorem possimus mattis enim"
    },
    {
      "loc": [
        4498,
        5445,
        "odit",
        "reprehenderit accusantium ipsum adipisicing ipsum,",
        6119
      ],
      "msg": "libero illum possimus arcu vitae congue. sit nec a",
      "type": "Nullam dui Enim ut dui"
    },
    {
      "loc": [
        1517,
        940
      ],
      "msg": "quas possimus exercitationem esse repellendus",
      "type": "reprehenderit Hic vehicula odit esse"
    },
    {
      "loc": [
        "arcu accusantium enim nec",
        "accusantium dui elit. reprehenderit esse"
      ],
      "msg": "possimus Lorem",
      "type": "dolor nec arcu nunc molestias, molestias, quas sit"
    }
  ]
}
```


> [!tip] Login

- Authorizations: **`None`**

**Endpoint:** **`POST`** [localhost:8000/v1/user/login/]()

**200** _'Successful Response'_

**Content-Type**: `application/json`

```json
{
  "access": "repellendus tellus. officiis",
  "refresh": "ipsum exercitationem nobis Hic repellendus odit ut",
  "expired_at": "1977-05-24T21:26:20.972066+00:00"
}
```

**422** _'Validation Error'_

**Content-Type**: `application/json`

```json
{
  "detail": []
}
```


> [!tip] Me

- Authorizations: **`CustomHTTPBearer`** _(http, bearer)_

**Endpoint:** **`GET`** [localhost:8000/v1/user/me/]()

**200** _'Successful Response'_

**Content-Type**: `application/json`

```json
{
  "email": "christopher53@example.com",
  "id": 2407
}
```


> [!tip] Partial Update

- Authorizations: **`CustomHTTPBearer`** _(http, bearer)_

**Endpoint:** **`PATCH`** [localhost:8000/v1/user/me/]()

**200** _'Successful Response'_

**Content-Type**: `application/json`

```json
{
  "email": "qroman@example.com",
  "is_staff": true,
  "last_login": "2006-09-27T23:14:28.455242+00:00",
  "id": 8558
}
```

**422** _'Validation Error'_

**Content-Type**: `application/json`

```json
{
  "detail": [
    {
      "loc": [
        7219
      ],
      "msg": "a ipsum placeat magnam, dolor",
      "type": "cursus"
    },
    {
      "loc": [
        2689,
        3251,
        "elit. vehicula ipsum congue. arcu reiciendis esse",
        7472,
        "a"
      ],
      "msg": "illum esse reiciendis veniam placeat",
      "type": "congue. consectetur veniam elit. Hic congue. dolor"
    },
    {
      "loc": [
        7252,
        4072,
        "sit",
        1217,
        4653
      ],
      "msg": "reprehenderit ipsum",
      "type": "Enim veniam"
    },
    {
      "loc": [
        "Nullam",
        9909
      ],
      "msg": "nunc arcu reprehenderit amet ipsum, mattis veniam",
      "type": "placeat modi exercitationem congue. mattis modi ut"
    },
    {
      "loc": [
        2652,
        "vehicula adipisicing tellus. mattis ipsum esse"
      ],
      "msg": "",
      "type": "Nullam reiciendis magnam, esse"
    }
  ]
}
```

---
