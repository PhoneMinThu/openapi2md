# Workflow App

> [!INFO] Workflow App system
> [AI workflow system](http://localhost:8000/docs)
> version: 0.0.1

---

## Authorizations

**`CustomHTTPBearer`** _(http, bearer)_

---

> [!ABSTRACT] health-check

> [!hint] Health Check

- Authorizations: **`None`**

**Endpoint:** **`GET`** [localhost:8000/v1/health_check/]()

> [!ABSTRACT] user

> [!hint] Register User Endpoint

- Authorizations: **`None`**

**Endpoint:** **`POST`** [localhost:8000/v1/user/register/]()

> [!hint] Login

- Authorizations: **`None`**

**Endpoint:** **`POST`** [localhost:8000/v1/user/login/]()

> [!hint] Me

- Authorizations: **`CustomHTTPBearer`** _(http, bearer)_

**Endpoint:** **`GET`** [localhost:8000/v1/user/me/]()

> [!hint] Partial Update

- Authorizations: **`CustomHTTPBearer`** _(http, bearer)_

**Endpoint:** **`PATCH`** [localhost:8000/v1/user/me/]()

---
