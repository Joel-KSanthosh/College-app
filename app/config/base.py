from os.path import dirname, join

from dotenv import load_dotenv

BASE_DIR = dirname(dirname(dirname(__file__)))

APP_DIR = join(BASE_DIR, 'app')

load_dotenv(dotenv_path=join(BASE_DIR, 'dev.env'))

DEBUG = True



