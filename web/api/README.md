## Headers

Content-Type: "application/json"

Authorization: "Token {Token}"

***

## api/users/signup
##### POST
Create user and return

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

        200

        {
            "profile": {
                "id": 3,
                "username": "user1",
                "location": "Istanbul",
                "gender": "Male",
                "photo_path": ""
            },
            "user": {
                "email": "user1@gmail.com",
                "username": "user1"
            }
        }
        


        400 Bad Request

        { field: [error] }

***

## api/users/signin
##### POST
authenticate user with email and password, return token

    **Request**

        {
            "username": String, (required)
            "email": String, (required)
            "password": String (required)
        }

    **Response**

        200

        {
            "token": Token
        }



        400 Bad Request

        {}

***

## api/users/signout
##### GET
delete user token from database

    **Response**

        200
        
        
        
        204 NO CONTENT

        { "field": [error] }

***

## api/users
##### GET
retrieve all users

    **Response**

        200

        [
            {
                "email": String,
                "username": String
            }
        ]

***

## api/users/login_req
##### GET, POST
a login required url

    **Response**

        200

        {
            "username": String
        }
        
        
        
        400 BAD REQUEST

***