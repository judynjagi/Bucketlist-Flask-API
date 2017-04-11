[![CircleCI](https://circleci.com/gh/judynjagi/Bucket_list/tree/develop.svg?style=svg)](https://circleci.com/gh/judynjagi/Bucket_list/tree/develop)
[![Coverage Status](https://coveralls.io/repos/github/judynjagi/Bucket_list/badge.svg)](https://coveralls.io/github/judynjagi/Bucket_list)
# `BUCKETLIST` 

## `1. Synopsis`
Bucketlist is an API for an online Bucket List service built with Flask.
  
According to Merriam-Webster Dictionary, **a Bucket List is a list of things that one has not done before but wants to do before dying.**

This service implements Token Based Authentication for the Bucket List API such that some methods are not accessible to unauthenticated users. Endpoints listed as `Public` do not require the Authentication token to be accessed. Below is a list of Access control mapping.


| Endpoint                            | Allowed Methods  | Functionality                                            | Public         |
|-------------------------------------|------------------|----------------------------------------------------------|----------------|
| `/auth/login`                       | POST             | Log a user in                                            | Yes            |
| `/auth/register`                    | POST             | Register a user                                          | Yes            |
| `/bucketlists`                      | POST, GET        | Create and Retrieve all bucket lists                     | No             |
| `/bucketlists/<id>`                 | GET, PUT, DELETE | Retrieve, Update and Delete a single bucket list         | No             |
| `/bucketlists/<id>/items`           | GET, POST        | Create and Retrieve a new item in bucket list            | No             |
| `/bucketlists/<id>/items/<item_id>` | GET, PUT, DELETE | Retrieve, Edit, Delete an item in a bucket list          | No             |

## `2. Prerequisites`
Bucketlist API requires `Python 3`to run

## `3. Installation`
#### Clone the github repository
        1. $ git clone https://github.com/judynjagi/Bucket_list.git
       
        2. Change directory into package $ cd bucketlist
        
        3. install virtualenvwrapper
	        	$ pip install virtualenvwrapper
				$ export WORKON_HOME=~/Envs
				$ mkdir -p $WORKON_HOME
				$ source /usr/local/bin/virtualenvwrapper.sh
				$ mkvirtualenv bucketlist
				
        4. Activate the virtual environment using: $ workon bucketlist
        
        5. Install dependencies $ pip install requirements.txt


#### For more instructions on installing virtualenvwrapper use this link: <https://virtualenvwrapper.readthedocs.io/>


#### Configurations
 Creating a `.env` file and set these environment.
  
```
	workon buckeklist
	export APP_SETTINGS="config.DevelopmentConfig"
	export TEST_DATABASE_URI="sqlite:///../bucketlist.db"
	export PRODUCTION_DATABASE_URI="sqlite:///models/bucketlist.db"
	export DEVELOPMENT_DATABASE_URI="sqlite:///../bucketlist.db"
	export SECRET_KEY="privatekey-cannot-be-public"
	export FLASK_APP="bucketlist"
	export FLASK_DEBUG=true
	flask run

```
#### Run Migrations
 Create a database and run migrations by running these commands.

```
        $ python manage.py db init
        $ python manage.py db migrate
        $ python manage.py db upgrade
```

#### Run Bucketlist application
  Finally, after everything is set, run your application by:   

```
        1. Navigating to the project folder
        2. Run python base.py
        3. You can access the app at http://127.0.0.1:5000
```



## `4. Usage`

### Tools
To interact with the Bucketlist API, send it HTTP requests using your favourite tool (cURL, Postman etc).

I prefer ***Postman**, if you would like to try it download it here: <https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en>

Note that all requests ***MUST** be of the `Content-Type application/json`

###Examples

##### User Registration
Make a **POST** request to the route `/auth/register` with the following data: 

![Alt text](http://i.imgur.com/mGkLuWD.png) 
       
#####  User Login
---
Make a **POST** request to the route `/auth/login` with the following data: 
See below how to set the  `Headers` when loggig in
![Alt text](http://i.imgur.com/mkM5sIk.png)

![Alt text](http://i.imgur.com/mIEFAZl.png) 


##### Create a bucket list
---
Make a **POST** request to the route `/bucketlists/` with the 
![Alt text](http://i.imgur.com/3HTE5kq.png)

##### Get all bucket lists
---
Make a **GET** request to the route `/bucketlists/`:    
The request fetchs all user's bucket lists
![Alt text](http://i.imgur.com/3HTE5kq.png)
##### Get a single bucket list
---
Make a **GET** request to the route `/bucketlists/<id>`:    
The request fetches a single bucketlist requested by id          
![Alt text](http://i.imgur.com/QJdErsO.png)

##### Edit a bucket list name
---
Make a **PUT** request to the route `/bucketlists/<id>` to update an existing bucketlist
![Alt text](http://i.imgur.com/jaRKf1H.png)

##### Delete a bucket list
---
Make a **DELETE** request to the route `/bucketlists/<id>` to delete a bucketlist
![Alt text](http://i.imgur.com/hOpttE2.png)

##### Create a new bucket list item
---
Make a **POST** request to the route `/bucketlists/<id>/items/` to create a new bucketlist item
![Alt text](http://i.imgur.com/enJhf1t.png)

##### Get a single bucket list item
---
Make a **GET** request to the following route `/bucketlists/<id>/items/<id>`    

![Alt text](http://i.imgur.com/si0c3Pl.png)

#####  Edit a specific bucket list item
---
Make a **PUT** request to the route `/bucketlists/<id>/items/<id>` with the following payload.
![Alt text](http://i.imgur.com/NCQXIHg.png)

##### Delete a specific bucket list item
---
Make a **DELETE** request to the route `/bucketlist/<id>/<items>/<id>`  
![Alt text](http://i.imgur.com/KG8lbbV.png)

## `5. Testing`
---

```

To run the tests;
```
       1. Naviagate to the project folder and run 
      			 $ python manage.py cov
       
```