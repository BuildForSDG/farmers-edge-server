
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e139805eb7724e5c8fb6a54f774803d0)](https://app.codacy.com/gh/BuildForSDG/farmers-edge-server?utm_source=github.com&utm_medium=referral&utm_content=BuildForSDG/farmers-edge-server&utm_campaign=Badge_Grade_Settings)

# Farmers Edge

## About

Farmers Edge enables small scale farmers double their productivity hence doubles their income.
The app enables them to get ready market for their product, access useful info on farming and get funding for their farming activitty.

## Why

This app aims to address hunger problem in the world by focusing on achievemment of Zero Hunger SDG.

## Usage

### Getting started

#### Prerequisites

```
- Python
- Djangorestframework
```

#### Installation

```
git clone https://github.com/BuildForSDG/farmers-edge-server.git
```

```
cd farmers-edge-server/
```

```
poetry install
```

```
Activate Virtual env: source env/bin/activate
```

```
Create .env file and add settings environment variables
```

```
Run pip install -r requirements.txt
```

```
Run poetry run python manage.py runserver
```

```
Open a another terminal and activate virtual env
```

```
Run source .env
```

```
Run Celery: celery -A farmers worker -l info
```

```
Consume endpoints shown in the table below using Postmann/browser
```

#### Further info

- Lint: `poetry run flake8`
- Run tests using the command: `poetry run pytest`
- Install dependencies: `poetry add <dependency>`
- Install dev dependencies: `poetry add --dev <dev-dependency>`

#### Deployed API in Heroku

link to be provided in a shortwhile

## Functionality

1. User can register
2. Registered users can login
3. Retailer can place order
4. Farmer can create product
5. User send query using contact form
6. User can reset password

### Endpoints

|       Endpoint                                        |               FUNCTIONALITY                             |
| ------------------------------------------------------|:-------------------------------------------------------
| POST &emsp;&emsp;/auth/v1/register                    | This will register user                                 |
| POST &emsp;&emsp;/auth/v1/login                       | This will login user                                    |
| POST &emsp;&emsp;/auth/v1/request/                    | This will send password reset                           |
| POST &emsp;&emsp;/api/v1/farmer/product/              | This will create Product                                |
| POST &emsp;&emsp;/api/v1/retailer/order/              | This will create order                                  |
| GET  &emsp;&emsp;/api/v1/farmer/product/list/         | This will return all products                           |
| GET  &emsp;&emsp;/api/v1/retailer/order/list          | This will return all placed order                       |
| POST &emsp;&emsp;/api/v1/contact/                     | This will post a contact info                           |

### Registration

`POST /auth/v1/register`

Example request body:

```source-multipart/form-data
{
  "user":{
    "firstName": "John",
    "surname": "Doe",
    "username": "JD",
    "email":     "jd@gmail.com",
    "password": "pass12"
    "phoneNumber": "0701255789",
    "idNumber": "0120067",
    "location": "location",
    "typeUser": "customer"
  }
}
```

No authentication required, returns a User

Required fields: `firstName`, `surname`, `username`, `email(unique)`, `password`,
`typeUser`, `location`, `phoneNumber(unique)`, `idNumber(unique)`


### Authentication

`POST /auth/v1/login`

Example request body:

```source-json
{
  "user":{
    "email": "levynaibei@gmail.com",
    "password": "pass12"
  }
}
```

No authentication required, returns a User

Required fields: `email`, `password`

### Create Product

`POST api/v1/farmer/product/`

Example request body:

```source-json
     {
        "retailerEmail": "something@gmail.com",
        "product": "Sunflower",
        "totalCost": "Kes 200",
        "quantity": "20 Kg",
        "ready": "True"
    }
```

Authentication required, will return a Product

Required fields: `product`, `totalCost`, `quantity`, `ready`

### Create Order

`POST api/v1/retailer/order/`

Example request body:

```source-json
     {
        "productName": "Sunflower",
        "totalCost": "Kes 200",
        "quantity": "20 Kg",
        "waitTime": "2 months"
    }
```

Authentication required, will return an order

Required fields: `productName`, `totalCost`, `quantity`, `waitTime`

### Contact Us

`POST api/v1/contact/`

Example request body:

```source-json
     {
        "name": "Someone",
        "email": "someone@gmail.com",
        "subject": "premium amount",
        "message": "message here"
    }
```

Required fields: `name`, `email`, `subject`, `message`

### Password Reset Request

`POST auth/v1/request/`

Example request body:

```source-json
     {
        "email": "someone@gmail.com",
    }
```

Required fields: `email`

## Authors

- [Ogunlana Tunbosun](https://github.com/bosunogunlana) - Mentor
- [Levy Naibei](https://github.com/Levy-Naibei) - TTL
- [Ennocent Omondi](https://github.com/innovistar)
- [Emmanuel Langat](https://github.com/manulangat1)

## Contributing

If this project sounds interesting to you and you'd like to contribute, thank you!
First, you can send a mail to buildforsdg@andela.com to indicate your interest, why you'd like to support and what forms of support you can bring to the table, but here are areas we think we'd need the most help in this project :

1. area one (e.g this app is about human trafficking and you need feedback on your roadmap and feature list from the private sector / NGOs)
2. area two (e.g you want people to opt-in and try using your staging app at staging.project-name.com and report any bugs via a form)
3. area three (e.g here is the zoom link to our end-of sprint webinar, join and provide feedback as a stakeholder if you can)

## Acknowledgements

- [Django](https://docs.djangoproject.com/en/3.0/)
- [Django REST framework](https://www.django-rest-framework.org/)

## LICENSE

MIT
