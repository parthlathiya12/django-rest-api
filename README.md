# Django Boilerplate

This repo contains sample django application which has 2 APIs. one to create an user and another to get user.
Foe easy setup, we hvae added docker setup also docke

## Getting Started

### Prerequisites

Install Docker. see the [install instructions.](https://www.docker.com/get-started)

Below instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing

Clone repo in local 

```
git clone https://github.com/roverer/django-boilerplate.git
```

Build services using docker-compose. Go to project's root dir where docker-compose.yml located and run below cmd

```
docker-compose build
```

Create and start containers.

```
docker-compose up
```

This will create container for django app and mysql db.

### Usage
Swagger-ui: http://localhost:8090/swagger-ui

Create User API
```
curl --location --request POST 'http://localhost:8090/user' --header 'Content-Type: application/json' --data-raw '{
    "email": "test@gmail.com",
    "first_name": "test_first_name",
    "last_name": "test_last_name"
}'
```
Get User API
```
curl --location --request GET 'http://localhost:8090/user?email=test@gmail.com' --header 'Content-Type: application/json' 
```
