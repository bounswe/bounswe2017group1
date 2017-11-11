## Headers

Content-Type: "application/json"

Authorization: "Token {Token}"

***

## User Routes

### /users/signup
##### POST
Create new user

    **Request**

        {
            "username": String, (required)
            "email": String, (required)
            "password": String, (required)
            "location": String, (optional)
            "gender": String, (optional)
            "photo_path": String (optional)
        }

    **Response**

        201 Created

        {
            "profile": {
                "id": Integer,
                "username": String,
                "location": String,
                "gender": String,
                "photo_path": String,
                "user": Integer
            },
            "user": {
                "email": String,
                "username": String
            }
        }
        


        400 Bad Request

        { field: [error] }

***

### /users/signin
##### POST
authenticate user with email and password, return token

    **Request**

        {
            "username": String, (required)
            "email": String, (optional)
            "password": String (required)
        }

    **Response**

        200 OK

        {
            "token": Token
        }



        400 Bad Request

        {}

***

## /users/signout
##### POST
delete user token from database

    **Response**

        200 OK
        
        
        
        204 NO CONTENT

        { "field": [error] }

***

### /users/
##### GET
get all users

    **Response**

        200 OK

        [
            {
                "email": String,
                "username": String
            },
        ]

***