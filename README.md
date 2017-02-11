# back
swipeat back-end prototype

# crash course on heroku

We use [heroku](http://heroku.com) to sport our back-end, refer to their [introduction](https://devcenter.heroku.com/articles/getting-started-with-python#introduction) ot get started.

But here is the a shortcut...

## prerequisites
- you will need an account on [heroku](heroku.com)
- install [virtualenv](https://github.com/kennethreitz/python-guide/blob/master/docs/dev/virtualenvs.rst): `pip install virtualenv`
- follow the [heroku set-up](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)

## create and deploy
- get the code, commited to github
- push the code to heroku: `git push heroku master`
- start the web service: `heroku ps:scale web=1`
