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

You will get a token in response
response = {
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
Attach the token you got after logging in, the token will be attached
to the Authorization Header as (Token <TOKEN>)


# Fetching and Searching Own Tweets
GET Request
Attach the token you got after logging in, the token will be attached
to the Authorization Header as (Token <TOKEN>)

url = https://127.0.0.1/core/owntweets/

for searching a specific tweet with its text
url = https://127.0.0.1/core/owntweets/?search=text