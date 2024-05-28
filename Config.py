import os
import loguru


ENVIRONMENT = os.environ.get('ENVIRONMENT', False)
LOGGER = loguru.logger
if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    OWNER_ID = os.environ.get('OWNER_ID', 6258709129)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = "28611965"
    OWNER_ID = "772384743"
    API_HASH = "d36cfa9250dd3d0d46678b538836ca8b"
    BOT_TOKEN = "7250990840:AAH7hHhSmpb7S7VVP4VXyPYDqz2dsbF4pD0"
    DATABASE_URL = "mongodb+srv://BinaryBandiT69:BinaryBandiT69@db3.vxnexhs.mongodb.net/?retryWrites=true&w=majority&appName=DB3"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "TBots_Father" # must join channel link here
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
