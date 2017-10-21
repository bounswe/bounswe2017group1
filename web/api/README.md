## Headers

Content-Type: "application/json"

Authorization: "Token {Token}"

***

## api/users/signup
##### POST
Create user and return

  **Request**

    {
      "email": String,
      "password": String,
      "first_name"(optional): String,
      "last_name"(optional): String
    }

  **Response**

    200

      {
        "email": String,
        "password": String,
        "first_name"(optional): String,
        "last_name"(optional): String
      }


    400 Bad Request

    { field: [error] }

***

## api/users/signin
##### POST
authenticate user with email and password, return token

  **Request**

    {
      "email": String,
      "password": String
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
          "password": String,
          "first_name" (optional): String,
          "last_name" (optional): String
        }
      ]

***
