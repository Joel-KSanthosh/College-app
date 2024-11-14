import os

print("\n------------ DEVELOPMENT ENVIRONMENT STARTED ----------------\n")

user = os.environ.get('POSTGRES_USER')
password = os.environ.get('POSTGRES_PASSWORD')
server = os.environ.get('POSTGRES_SERVER')
port = os.environ.get('POSTGRES_PORT')


def db_uri():
    return f'postgresql://{user}:{password}@{server}:{port}'
