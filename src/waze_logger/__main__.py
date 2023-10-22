
import json

from waze_logger.database.create import create_database
from waze_logger.database.engine import create_engine

if __name__ == '__main__':

    with open('./config/waze_logger.json', 'r', encoding="utf8") as file:
        config = json.load(file)

    credentials = config["database"]

    engine = create_engine(credentials)

    create_database(engine)
