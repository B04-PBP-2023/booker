release: django-admin migrate --noinput && rm db.sqlite3 && django-admin migrate
web: gunicorn booker.wsgi