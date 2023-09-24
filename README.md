you need 4 terminals to run this program. These are the commands.
in Flask directory:
* python3 app.py
* redis-server
* celery -A celerySQL worker --loglevel=info -P threads

in Mad2Proj directory:
* npm install
* npm run serve