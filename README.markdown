# HeadRoom
## Browser-based psych testing

# THIS IS A DEVELOPMENT RELEASE
Please don't use it for production. We are releasing this software to github
so that it may be further developed upon.

## Features:
* JSON-based configuration
* JSON-based database
* [bottle.py](https://github.com/defnull/bottle) for minimal, one-file implementations

## Goals
* To incorporate [greenlets](http://bottlepy.org/docs/dev/async.html#greenlets-to-the-rescue) into the application: This gives us an opportunity to do real-time testing.
* To incorporate a python server / view module system. This would allow for
	user-extensible programming ranging from networked economics experiments to
	Event-Related Potential (ERP) testing with an EEG device. 
* To foster a community of scientists and hackers to help shape future
	psychological research.
* Incorporation of a key-value database such as Redis or Postgresql.

# TODOs
This software is pre-alpha, but should give the apt programmer an idea of the
intended result. It is **untested** as of this point, but I'm working on that.
If the code doesn't show it: I'm really not a great programmer, but I can
usually hack things together
* Testing (I'm not a TDD type, but I really should be `:(`). 
* Probably a re-factor of 

# Installation &amp; Deployment
If you really want to give this a go, you'll need git, python2.6 or higher, and
virtualenv on your system. Activate the virtualenv, `pip install -r
requirements.txt` and `python headroom/app.py` should set you on your way. 


## Licensing
Released under an MIT License. You can do pretty much anything you want with
this code, so long as others can do the same (see the `LICENSE.markdown` file
for more information).

