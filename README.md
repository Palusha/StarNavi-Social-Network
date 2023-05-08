# StarNavi Social-network

## Dependencies

- [docker](https://docs.docker.com/get-docker/)

## Api envinronment

- ### create `.env` file in `SocialNetwork` folder

#### `.env` example

```dosini
DEBUG=1
SECRET_KEY="django-insecure-44^#9_ar$$hy(\*#+n@9fl-9cn+\_4g=#7h)ak#%nk88vts(fdp0"
ALLOWED_HOSTS=api localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=mydb
SQL_USER=admin
SQL_PASSWORD=admin
SQL_HOST=api_db
SQL_PORT=5432
```

- ### create `.db.env` file in `SocialNetwork` folder

#### `.db.env` example

```dosini
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
POSTGRES_DB=mydb
```

## Bot envinronment

- ### create `.bot.env` file in `SocialNetwork` folder

#### `.bot.env` example

```dosini
SCHEME=http
HOST=api
PORT=8000
```

## Build

```shell
docker-compose build
```

## Start

```shell
docker-compose up -d
```

## Note

### After starting the containers it will create superuser with credentials:

- username: `admin`
- password: `password`
