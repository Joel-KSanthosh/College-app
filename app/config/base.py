import os

from dotenv import load_dotenv

BASE_DIR = os.path.abspath('C:\\Users\\285148\\Desktop\\FastApi')
APP_DIR = os.path.abspath('C:\\Users\\285148\\Desktop\\FastApi\\app')

load_dotenv(dotenv_path=os.path.join(BASE_DIR, 'dev.env'))

DEBUG = True



