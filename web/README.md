***

### Start the project
* `git clone https://github.com/bounswe/bounswe2017group1.git`
* `cd bounswe2017group1/web`
* `pip install -r requirements.txt` (Install necessary python modules)
* `python manage.py migrate` (Create or update the database structure)
* `python manage.py runserver` (Start server)

***

Go to http://127.0.0.1:8000 and see if it works

Use API on http://127.0.0.1:8000/api base.

***
### Heritage Item Get Post Functions:

	Post Function:
		GET: 	"http://127.0.0.1:8000/api/items/ID"
			* There is no slash at the end of the url.
			* ID is numerical, ex:1,2,3,...
			
			Example Result of GET:
				url: http://127.0.0.1:8000/api/items/2
				result: 200 OK,
				JSON Result:
					{
 					   "id": 2,
					    "title": "tac mahal",
					    "description": "hindistanda efso mekan",
					    "creation_date": "2017-10-25T14:26:56Z",
					    "event_date": "2017-10-25T14:26:57Z",
					    "location": "ez",
					    "creator": 4
					}
		POST:	"http://127.0.0.1:8000/api/items"
			* There is no slash at the end of the url.
			* ID is assigned by database, you should not add ID into your JSON that you post.
			
			Example Result of GET:
				url: http://127.0.0.1:8000/api/items
				result: 201 CREATED,
				JSON format that will be POSTed:
					{
					    "title": "tac mahal",				//title of heritage item
					    "description": "hindistanda efso mekan",	        //description of heritage item
					    "creation_date": "2017-10-25T14:26:56Z",		//creation date
					    "event_date": "2017-10-25T14:26:57Z",		//event date
					    "location": "ez",					//location
					    "creator": 4					//ID of PROFILE model(profile includes USER model)
					}
  NOTs:  You can add one Heritage Item and you can retrieve one Heritage item.
  
  ***
