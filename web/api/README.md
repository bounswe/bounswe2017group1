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
        
        
        
    401 Unauthorized
    
      {
        "detail": "Invalid token."
      }

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
      
      
      
    404 Not Found

***

## Heritage Item Routes

### /items/
##### POST
Create new heritage item

  **Request**

    {
        "title": String, (required)
        "description": String, (required)
        "event_date": String, (optional)
        "location": String, (optional)
        "tags": [
            {
                "name": String,
            },
        ] (required, send empty list if there are no tags)
    }


  **Response**

    201 Created

      {
          "id": Integer,
          "upvote_count": Integer,
          "downvote_count": Integer,
          "is_upvoted": Boolean,
          "is_downvoted": Boolean,
          "is_owner": Boolean,
          "tags": [
              {
                  "id": Integer,
                  "name": String
              },
          ],
          "media":[
              {
                   "id": Integer,
                   "heritage": Integer,
                   "image": URL,
                   "creation_date": Datetime,
                   "update_date": Datetime
              
              },
          ],
          "creator_username": String,  
          "creator_image_path": URL,
          "title": String,
          "description": String,
          "creation_date": Datetime,
          "event_date": Datetime,
          "location": String,
          "creator": Integer
          
      }
        


    400 Bad Request

      { field: [error] }
      
      
      
    401 Unauthorized
    
      { "detail": [error] }  

***

### /items/
##### GET
get all heritage items

  **Response**

    200 OK
        
      [
        {
          "id": Integer,
          "upvote_count": Integer,
          "downvote_count": Integer,
          "is_upvoted": Boolean,
          "is_downvoted": Boolean,
          "is_owner": Boolean,
          "tags": [
              {
                  "id": Integer,
                  "name": String
              },
          ],
          "media":[
              {
                   "id": Integer,
                   "heritage": Integer,
                   "image": URL,
                   "creation_date": Datetime,
                   "update_date": Datetime
              
              },
          ],
          "creator_username": String,  
          "creator_image_path": URL,
          "title": String,
          "description": String,
          "creation_date": Datetime,
          "event_date": Datetime,
          "location": String,
          "creator": Integer
          
         },
      ]



    404 Not Found
        
***

### /items/top
##### GET
Get heritage items sorted by their votes

Response is the same as GET /items/

### /items/trending
##### GET
Get heritage items sorted by the increase in their votes in the last week

Response is the same as GET /items/

### /items/new
##### GET
Get heritage items sorted by their creation dates.

Response is the same as GET /items/

### /items/{id}
##### GET
get heritage item by id

  **Response**

    200 OK

      {
          "id": Integer,
          "upvote_count": Integer,
          "downvote_count": Integer,
          "is_upvoted": Boolean,
          "is_downvoted": Boolean,
          "is_owner": Boolean,
          "tags": [
              {
                  "id": Integer,
                  "name": String
              },
          ],
          "media":[
              {
                   "id": Integer,
                   "heritage": Integer,
                   "image": URL,
                   "creation_date": Datetime,
                   "update_date": Datetime
              
              },
          ],
          "creator_username": String,  
          "creator_image_path": URL,
          "title": String,
          "description": String,
          "creation_date": Datetime,
          "event_date": Datetime,
          "location": String,
          "creator": Integer
          
      }



    404 Not Found

***

### /items/{id}
##### PUT
update the heritage item which is indicated by id

  **Response**

    200 OK

      {
          "id": Integer,
          "upvote_count": Integer,
          "downvote_count": Integer,
          "is_upvoted": Boolean,
          "is_downvoted": Boolean,
          "is_owner": Boolean,
          "tags": [
              {
                  "id": Integer,
                  "name": String
              },
          ],
          "media":[
              {
                   "id": Integer,
                   "heritage": Integer,
                   "image": URL,
                   "creation_date": Datetime,
                   "update_date": Datetime
              
              },
          ],
          "creator_username": String,  
          "creator_image_path": URL,
          "title": String,
          "description": String,
          "creation_date": Datetime,
          "event_date": Datetime,
          "location": String,
          "creator": Integer
          
      }

    
    
    400 Bad Request
    
      { field: [error] }
    
    

    404 Not Found
    
    
    
    412 Precondition Failed

***

### /items/{id}
##### DELETE
delete the heritage item which is indicated by id

  **Response**

    200 OK



    204 No Content
    
    
    
    404 Not Found

***

### /items/{id}/comments/
##### GET
get all comments of the heritage item indicated by id

  **Response**

    200 OK
        
      [
        {
            "id": Integer,
            "is_owner": Boolean,
            "creator_image_path": URL,
            "creator_username": string,
            "text": string,
            "creation_date": Datetime,
            "update_date": Datetime,
            "heritage": Integer,
            "creator": Integer,
            "parent_comment": Integer (can be null)
        },
      ]



    404 Not Found
        
***

### /items/{id}/tags/
##### GET
get all tags of the heritage item indicated by id

  **Response**

    200 OK
        
      [
        {
            "id": Integer,
            "name": String,
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
        "is_owner": Boolean,
        "creator_image_path": URL,
        "creator_username": string,
        "text": string,
        "creation_date": Datetime,
        "update_date": Datetime,
        "heritage": Integer,
        "creator": Integer,
        "parent_comment": Integer (can be null)
      }
        


    400 Bad Request

      { field: [error] }
      
      
      
    401 Unauthorized
    
      { "detail": [error] } 

***

### /comments/{id}
##### GET
get the comment by id


  **Response**

    200 OK

      {
        "id": Integer,
        "is_owner": Boolean,
        "creator_image_path": URL,
        "creator_username": string,
        "text": string,
        "creation_date": Datetime,
        "update_date": Datetime,
        "heritage": Integer,
        "creator": Integer,
        "parent_comment": Integer (can be null)
      }

        


    404 Not Found

***

### /comments/{id}
##### DELETE
delete the comment that is indicated by id

  **Response**

    200 OK



    204 No Content
    
    
    
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
          "heritage": Integer,
          "upvote_count": Integer,
          "downvote_count": Integer
      }
        


    400 Bad Request

      { field: [error] }
      
      
    
    401 Unauthorized
    
      { "detail": [error] } 

***

##### DELETE
Deletes the existing vote of the requester

  **Request**

    {
        "heritage": Integer (required)
    }
    

  **Response**

    200 Ok
    action successfully done

      {
          "upvote_count": Integer,
          "downvote_count": Integer
      }
        


    404 Not Found
    Means there is no old vote in the DB to specified heritage item ID or it is already deleted.

    
    HTTP_412_PRECONDITION_FAILED    
    Probably there is no heritage field in the request or something else is wrong about the request.
    
***

## Profile Routes

### /profiles/
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

## Tag Routes

### /tags/
##### GET
get all tags

  **Response**

    200 OK
        
      [
        {
            "id": Integer,
            "name": String,
        },
      ]



    404 Not Found
    
***

### /tags/{id}/heritages/
##### GET
get all heritage items own the tag indicated by id

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



## Search

### /search/
##### POST
searches heritage items

  **Request**
  
      [
         {
            "query": String, (Required)
            "filters":{
                 "location": String, (optional)
                 "creator": String, (optional)
                 "creation_start": datetime, (optional)
                 "creation_end": datetime, (optional)
                 "event_start": datetime, (optional)
                 "event_end": datetime, (optional)
             } (optional)
          }
      ]

  **Response**
  
      [
        {
          "id": Integer,
          "upvote_count": Integer,
          "downvote_count": Integer,
          "is_upvoted": Boolean,
          "is_downvoted": Boolean,
          "is_owner": Boolean,
          "tags": [
              {
                  "id": Integer,
                  "name": String
              },
          ],
          "media":[
              {
                   "id": Integer,
                   "heritage": Integer,
                   "image": URL,
                   "creation_date": Datetime,
                   "update_date": Datetime
              
              },
          ],
          "creator_username": String,  
          "creator_image_path": URL,
          "title": String,
          "description": String,
          "creation_date": Datetime,
          "event_date": Datetime,
          "location": String,
          "creator": Integer
          
         },
      ]
***



## Annotation

### /annotation/heritage/{item_id}/
##### POST
create annotation on the description of the heritage item

  **Request**
  
      {
	    "text": String, (Required),
	    "coordinates": [ Integer, Integer ]
      }


  **Response**
    
    201 Created
    
    
    
    400 Bad Request
      
***


### /annotation/heritage/{item_id}/
##### GET
get annotations of a heritage item indicated by id

  **Response**
    
    200 OK
      [
        {
          "annotatedAt": DateTimeString,
          "body": String,
          "@id": String,
          "serializedAt": DateTimeString,
          "target": String
        },
      ]
      
***


## Annotation

### /annotation/heritage/{item_id}/media/{media_id}
##### POST
create annotation on the media file of the heritage item

  **Request**
  
      {
	    "text": String, (Required),
	    "coordinates": [ Integer, Integer, Integer, Integer ]
      }


  **Response**
    
    201 Created
    
    
    
    400 Bad Request
      
***



## Annotation

### /annotation/heritage/{item_id}/comment/{comment_id}
##### POST
create annotation on the comment of the heritage item

  **Request**
  
      {
	    "text": String, (Required),
	    "coordinates": [ Integer, Integer ]
      }


  **Response**
    
    201 Created
    
    
    
    400 Bad Request
      
***


### /annotation/
##### GET
get all annotations

  **Response**
    
    200 OK
      [
        {
          "annotatedAt": DateTimeString,
          "body": String,
          "@id": String,
          "serializedAt": DateTimeString,
          "target": String
        },
      ]
      
***


## Video

### /videos/
##### POST
create a video or change an old video of the heritage item

  **Request**
  
      {
        "video_url": String,
        "heritage" : Int(heritage id)
      }


  **Response**
    
    201 Created
    
    
    
    400 Bad Request
      
***


### /videos/<video id>
##### GET
get the video with the given id 

ps: there should be no need to use this GET function since video object is also returned in the heritage serializer in the "video" field

  **Response**
    
    200 OK
      
      {
          "id" : Int,
          "video_url": String,
          "creation_date": DateTimeString,
          "update_date": DateTimeString,
          "heritage": Int(Heritage id)
      }
      
***
##### DELETE
delete the video with the given id

  **Response**
    
    204 NO CONTENT (Successfully Deleted)
    
    412 Precondition Failed
