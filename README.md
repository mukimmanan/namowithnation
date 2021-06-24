# Edit Settings.py File

# Change the user, password, database-name

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoRestDatabse',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

Create the database with same name as you mentioned over in the Database Dictionary

# Running the App
1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py runserver 127.0.0.1:8000

# Registering a User
POST Request

url = https://127.0.0.1/core/register/

body = {
    "name": "name",
    "email": "email",
    "password": "password"
}

# Authenticating a User
POST Request

url = https://127.0.0.1/core/login/

body = {
    "username": "the email you entered while registering",
    "password": "password"
}

You will get a token in response response = {
 "token": TOKEN
}

# Fetching Tweets
GET Request

url = https://127.0.0.1/core/tweets/?page_num=1 

for changing the page size from 5 to any other size

url = https://127.0.0.1/core/tweets/?page_num=1&page_size=6 (max page size = 10)

Response Array of tweets

# Creating Tweets
POST Request

url = https://127.0.0.1/core/tweets/

body = {
    tweet_text: "Text"
}

For clients to authenticate, the token key should be included in the Authorization HTTP header. 

For example:

Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

# Fetching and Searching Own Tweets
GET Request

For clients to authenticate, the token key should be included in the Authorization HTTP header.

For example:

Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

url = https://127.0.0.1/core/owntweets/

for searching a specific tweet with the text in the tweet

url = https://127.0.0.1/core/owntweets/?search=text