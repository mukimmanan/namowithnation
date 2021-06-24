release python manage.py makemigrations core
release: python manage.py migrate core
web: run-program waitress-serve --port=$PORT settings.wsgi:application