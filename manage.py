# Importing the create_app (application factory) from app/__init__.py

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()