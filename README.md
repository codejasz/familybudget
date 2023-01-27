# Family budget
App which allows you and your family to control your common incomes and expenses

### Run project
1. Clone project directory to your local machine
2. Go to the root project directory and run script which will build docker image and start the app:
`./rebuild_and_start_container.sh`
3. Go to [localhost](http://127.0.0.1:8000). You should be able to see welcome page
4. During first run you need to run all migrations for DB
`python manage.py migrate`

### Example data

You can also populate example data

`python manage.py loaddata example_data/example_data.json  `

Admin (SuperUser) - `admin`:`adminadmin`

User 1 - `user`:`useruser`

User 2 - `user2`:`useruser`

### Debug

If you are in debug mode then you can use `/admin/` panel.

Only super user have access to admin panel. To create super user, please use command:

`python manage.py createsuperuser`

# API

`/users/` - users endpoint

`/budgets/` - budgets endpoint

`/transactions/` - transactions endpoint

For clients to authenticate, the token key should be included in the Authorization HTTP header. The key should be prefixed by the string literal "Token", with whitespace separating the two strings. For example:

```
Authorization: Token bd3310b8681237572fc44a9c099c77486a00ed06
```

## Login

Login (obtaining authorization token)

Request:

```bash
curl -X POST \
  http://127.0.0.1:8000/auth/ \
  -H 'content-type: application/json' \
  -d '{
	"username": "user",
	"password": "useruser"
}'
```

Response:

```json
{
    "token": "b1199ee92738ede753e523f530a0440076a4d41a"
}
```

## New budget

Create new budget

Request:

```bash
curl -X POST \
  http://127.0.0.1:8000/budgets/ \
  -H 'Authorization: Token b1199ee92738ede753e523f530a0440076a4d41a' \
  -H 'content-type: application/json' \
  --data-raw $'{\n    "name": "Budget example",\n    "owner": 2,    \n"description": "budget",\n    "transactions": [],\n    "shared_with": []\n}'
```

Response

```json
{
    "description": "budget",
    "name": "Budget example",
    "owner": 2,
    "shared_with":
        [],
    "transactions":
        []
}
```

## List budgets

List users budgets together with budgets to which the user is entitled

Request

```bash
curl -X GET \
  http://127.0.0.1:8000/budgets/ \
  -H 'Authorization: Token b1199ee92738ede753e523f530a0440076a4d41a' \
  -H 'content-type: application/json'
```

Response

```json
[
    {
        "description": null,
        "name": "Savings",
        "owner": 2,
        "shared_with":
        	[],
        "transactions":
        	[8]
    }
]
```


## Add expense

Create new expense

Request:

```bash
curl -X POST \
  http://127.0.0.1:8000/transactions/ \
  -H 'Authorization: Token b1199ee92738ede753e523f530a0440076a4d41a' \
  -H 'content-type: application/json' \
  -d '
      {
        "description": "Expense example",
        "amount": 100,
        "transaction_type": "EX",
        "created_at": "2023-01-24",
        "category": 1,
        "budget": 76
    }
'
```

Response:

```json
{
    "description": "Expense example",
    "amount": 100,
    "transaction_type": "EX",
    "created_at": "2023-01-24",
    "category": 1,
    "budget": 76
}
```

## Try to get budget without permission

Request:

```bash
curl -X GET \
  http://127.0.0.1:8000/budgets/76 \
  -H 'Authorization: Token b1199ee92738ede753e523f530a0440076a4d41a' \
  -H 'content-type: application/json'
```

Response

```json
{
    "detail": "Not found."
}
```

### Tech stack
* Django 4.1
* Postgres
