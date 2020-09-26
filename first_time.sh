# rm -r migrations/ app.db
export FLASK_APP=app.py
flask db init
flask db migrate -m 'init'
flask db upgrade
export FLASK_DEBUG=1
flask run
