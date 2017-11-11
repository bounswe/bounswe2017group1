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

      { field: [error] }

***

### /users/signout
##### POST
delete user token from database

  **Response**

    200 OK
        
        
        
    204 No Content

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

## Heritage Item Routes

### /items/
##### POST
Create new heritage item

  **Request**

    {
        "title": String, (required)
        "description": String, (optional)
        "event_date": String, (optional)
        "location": String, (required)
        "tags": [
            {
                "name": String,
                "category": String
            },
        ] (optional)
    }


  **Response**

    201 Created

      {
          "id": Integer,
          "upvote_count": Integer,
          "downvote_count": Integer,
          "tags": [
              {
                  "id": Integer,
                  "name": String,
                  "category": String
              },
          ] (optional)
      }
        


    400 Bad Request

      { field: [error] }

***

### /items/{id}
##### GET
get heritage item by id

  **Response**

    200 OK

      {
          "id": Integer,
          "upvote_count": Integer,
          "downvote_count": Integer,
          "tags": [
              {
                  "id": Integer,
                  "name": String,
                  "category": String
              },
          ],
          "title": String,
          "description": String,
          "creation_date": DateTime,
          "event_date": DateTime,
          "location": String,
          "creator": Integer
      }



    404 Not Found

***

### /items/all
##### POST
get all heritage items

  **Response**

    200 OK
        
      [
        {
            "id": Integer,
            "upvote_count": Integer,
            "downvote_count": Integer,
            "tags": [
                {
                    "id": Integer,
                    "name": String,
                    "category": String
                },
            ],
            "title": String,
            "description": String,
            "creation_date": DateTime,
            "event_date": DateTime,
            "location": String,
            "creator": Integer
        },
      ]



    404 Not Found
        
***

## Comment Routes

### /comments/
##### POST
Create new comment

  **Request**

    {
        "text": String, (required)
        "heritage": Integer, (required)
        "parent_comment": Integer (optional)
    }
    

  **Response**

    201 Created

      {
          "id": Integer,
          "text": String,
          "creation_date": DateTime,
          "update_date": DateTime,
          "heritage": Integer,
          "creator": Integer,
          "parent_comment": Integer
      }
        


    400 Bad Request

      { field: [error] }

***

### /comments/{id}
##### GET, PUT, DELETE
get, update or delete a comment by id

  **Request**

    {
        "text": String, (required)
        "heritage": Integer, (required)
        "parent_comment": Integer (optional)
    }
    

  **Response**

    200 OK

      {
          "id": Integer,
          "text": String,
          "creation_date": DateTime,
          "update_date": DateTime,
          "heritage": Integer,
          "creator": Integer,
          "parent_comment": Integer
      }

        
        
    400 Bad Request

      { field: [error] }
        


    404 Not Found

***

### /heritagecomments/{id}
##### GET
get all comments of the heritage item by id

  **Response**

    200 OK
        
      [
        {
            "id": Integer,
            "text": String,
            "creation_date": DateTime,
            "update_date": DateTime,
            "heritage": Integer,
            "creator": Integer,
            "parent_comment": Integer
        },
      ]



    404 Not Found
        
***

## Vote Routes

### /votes/
##### POST
Create new vote

  **Request**

    {
        "value": Boolean, (required)
        "heritage": Integer (required)
    }
    

  **Response**

    201 Created

      {
          "id": Integer,
          "value": Boolean,
          "creation_date": DateTime,
          "update_date": DateTime,
          "voter": Integer,
          "heritage": Integer
      }
        


    400 Bad Request

      { field: [error] }

***

## Profile Routes

### /profiles/{id}
##### GET
get user profile by id

  **Response**

    200 OK

      {
          "id": Integer,
          "username": String,
          "location": String,
          "gender": String,
          "photo_path": String,
          "user": Integer
      }



    404 Not Found

***

### /profiles/all
##### GET
get all user profiles

  **Response**

    200 OK
        
      [
        {
            "id": Integer,
            "username": String,
            "location": String,
            "gender": String,
            "photo_path": String,
            "user": Integer
        },
      ]



    404 Not Found
        
***

## Tag Routes

### /tags/all
##### GET
get all tags

  **Response**

    200 OK
        
      [
        {
            "id": Integer,
            "name": String,
            "category": String
        },
      ]



    404 Not Found
    
***