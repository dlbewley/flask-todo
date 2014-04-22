Follow me
=========

Make sure you have virtualenv setup before continuing. Here's how on OSX.
* http://hackercodex.com/guide/mac-osx-mavericks-10.9-configuration/
* http://hackercodex.com/guide/python-development-environment-on-mac-osx/

Make a flask app with virtualenv goodness. I substituted python-2.7 for the python-2.6 references.
* https://www.openshift.com/blogs/how-to-install-and-configure-a-python-flask-dev-environment-deploy-to-openshift

Readers' Digest Summary
-----------------------
 # using our ~/src/openshift/ dir to house it, create an app called 'flask'
 cd ~/src/openshift
 rhc app create flask python-2.7
 cd ~/src/openshift/flask
 git remote add upstream -m master git://github.com/openshift/flask-example.git
 git pull -s recursive -X theirs upstream master
 cd ~/src/openshift/flask/wsgi
 virtualenv venv --python=python2.7
 . venv/bin/activate
 pip install flask flask-wtf flask-babel markdown flup 
 vim ~/src/openshift/flask/setup.py
 # update install_requires to include flask-wtf flask-babel markdown flup
 #  install_requires=['Flask>=0.7.2', 'MarkupSafe', 'flask-wtf', 'flask-babel', 'markdown', 'flup'],
 echo 'venv/' >> ~/src/flask/.gitignore
 mkdir -p ~/src/openshift/flask/wsgi/app/{static,templates}
 mkdir -p ~/src/openshift/flask/wsgi/tmp

Now create hello world app in app/.
* Create flask
 cat <<EOF >  ~/src/openshift/flask/wsgi/app/__init__.py
from flask import Flask  
app = Flask(__name__)  
from app import views
EOF

* Create view
 cat <<EOF >  ~/src/openshift/flask/wsgi/app/views.py
from app import app
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
EOF

* Create run.py to spawn hello world app
 cat <<EOF >  ~/src/openshift/flask/wsgi/run.py
from app import app
if __name__ == "__main__":
    app.run(debug = True) #We will set debug false in production 
EOF

* Update  ~/src/openshift/flask/wsgi/application


Test It
-------
 python run.py
 curl http://localhost:5000

Push It
-------
 cd ~/src/openshift/flask
 git add .


Phase Two
=========

 cd ~/src/openshift/flask
 #update wsgi/run.py
 #ceate templates/base.html
 #ceate templates/index.html




Flask on OpenShift
==================

This git repository helps you get up and running quickly w/ a Flask installation
on OpenShift.


Running on OpenShift
----------------------------

Create an account at https://www.openshift.com

Create a python application

    rhc app create flask python-2.6

Add this upstream flask repo

    cd flask
    git remote add upstream -m master https://github.com/openshift/flask-example.git
    git pull -s recursive -X theirs upstream master
    
Then push the repo upstream

    git push

That's it, you can now checkout your application at:

    http://flask-$yournamespace.rhcloud.com

------------------------------

To get more log messages in your OpenShift logs please add the following line to your code

app.config['PROPAGATE_EXCEPTIONS'] = True  

To read more about logging in Flask please see this email

http://flask.pocoo.org/mailinglist/archive/2012/1/27/catching-exceptions-from-flask/

