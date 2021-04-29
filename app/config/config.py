from dotenv import load_dotenv
from os.path import join, dirname

# Path to .env file
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)
