A one-liner phrase describing this project or app

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

Clone the repository

```
git clone https://github.com/BuildForSDG/farmers-edge-server.git
```

Move into the project folder

```
cd farmers-edge-server
```

Install the dependencies of the project

```
poetry install
```

Run the app

```
poetry run python manage.py runserver
```
#### Further info
-  Lint: `poetry run flake8`
-  Run tests using the command: `poetry run pytest`
-  Install dependencies: `poetry add <dependency>`
-  Install dev dependencies: `poetry add --dev <dev-dependency>`

#### Hosted API in Heroku

To be provided soon

## Functionality

### Authentication

1. User can register
2. Registered users can login

### Endpoints

|       Endpoint                                  |               FUNCTIONALITY                             |
| ----------------------------------------        |:-------------------------------------------------------
| POST &emsp;&emsp;/auth/v1/register              | This will register user                                 |
| POST &emsp;&emsp;/auth/v1/login                 | This will login user                                    |
| GET  &emsp;&emsp;/auth/v1/user/                 | This will return user data                              |
| POST &emsp;&emsp;/api/v1/farmer/product/        | This will create Product                                |
| POST &emsp;&emsp;/api/v1/retailer/order/        | This will create Order                                  |
| PUT  &emsp;&emsp;/api/v1/farmer/update/1        | This will update Product                                |
| GET  &emsp;&emsp;/api/v1/product/ready/1        | This will send email to retailers                       |
| GET  &emsp;&emsp;/api/v1/retailer/order/detail/1| This will return order detail                           |

## Authors

*  [Ogunlana Tunbosun](https://github.com/bosunogunlana) - Mentor
*  [Levy Naibei](https://github.com/Levy-Naibei) - TTL
*  [Ennocent Omondi](https://github.com/innovistar)
*  [Emmanuel Langat](https://github.com/manulangat1)cd

## Contributing
If this project sounds interesting to you and you'd like to contribute, thank you!
First, you can send a mail to buildforsdg@andela.com to indicate your interest, why you'd like to support and what forms of support you can bring to the table, but here are areas we think we'd need the most help in this project :
1.  area one (e.g this app is about human trafficking and you need feedback on your roadmap and feature list from the private sector / NGOs)
2.  area two (e.g you want people to opt-in and try using your staging app at staging.project-name.com and report any bugs via a form)
3.  area three (e.g here is the zoom link to our end-of sprint webinar, join and provide feedback as a stakeholder if you can)

## Acknowledgements

* [Django](https://docs.djangoproject.com/en/3.0/)
* [Django REST framework](https://www.django-rest-framework.org/)

## LICENSE
MIT