
import os
from urllib.parse import quote_plus
from dotenv import load_dotenv


# Load variables from .env file
load_dotenv()


# Encode the password
pwd = quote_plus(os.getenv("DB_PASSWORD"))

# URL_DATABASE = f"postgresql+psycopg2://postgres:{pwd}@localhost:5432/product"

# %40 for @


URL_DATABASE=f"postgresql://postgres:{pwd}@localhost:5432/product"

