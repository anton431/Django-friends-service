# Django friends service


## Stack

>Language: __Python 3__<br>
Web framework: __Django__<br>
Database: __SQLite__<br>



## Description

>The service provides the following features:
>- register a new user;
>- send one user a friend request to another;
>- accept/reject a friend request from another user;
>- view the user's list of their outgoing and incoming friend requests;
>- view the user's list of their friends;
>- get the user the status of friendship with some other user;
>- remove the user of another user from their friends


## Private information

>Private information is in the .env:<br>
>- SECRET_KEY — django key;<br>


## Launch

>- Clone a repository<br>
>- Go to the working directory in the terminal <br>
>- Execute commands in the terminal:<br>
>>pip install -r requirements.txt<br>
python -m venv venv<br>
source venv/Scripts/activate<br>
pip install -r requirements.txt<br>
cd src<br>
python manage.py makemigrations<br>
python manage.py migrate<br>
python manage.py createsuperuser<br>
python manage.py runserver<br>