##Class Project for NAU CS399
### How to install Requirements
- pip install -r requirements.txt
###Urls
- If user isn's logged in redirect to '/login'
- "/": splash page, if the user is logged in redirect to '/dashboard'
- "/feed": gallery display of posts from followed users
- "/explore": grid of random posts (that fit a tag the user provides?)
- "/dashboard": User dashboard, think facebook newsfeed, allows user to view followed posts and post new content
- "/login": login form, must validate
- "/logout": logout user, clear whatever, redirect to '/'

###Models
- User
- Post

###ToDo
- Login
	- Authenticate
	- Ensure that only authenticated users have access:
		-  to the dashboard
		-  Make posts
- Splash page
	- Add content
- Django Restful framework
	- Edit views.py implement
- Post status to main feed
- Add feature for other users to comment on status
- Thumbs up / Thumbs Down
- Profile Picture Upload