
import json
import csv

from waze_logger.database.create import create_database
from waze_logger.database.engine import create_engine
from waze_logger.location import Location

if __name__ == '__main__':

    with open('./config/waze_logger.json', 'r', encoding="utf8") as file:
        config = json.load(file)

    with open('./config/location.csv', 'r', encoding="utf8") as file:
        location_file = csv.reader(file)

        headers = next(location_file)
        locations = []

        for row in location_file:
            location = dict(zip(headers, row))
            locations.append(Location(**location))

    credentials = config["database"]

    engine = create_engine(credentials)

    create_database(engine, locations)
