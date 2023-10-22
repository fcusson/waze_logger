"""module containing the route object"""

from waze_logger.location import Location


class Route:

    route_id: int
    origin: Location
    destination: Location

    def __init__(
            self,
            origin: Location,
            destination: Location,
            route_id: int = None,
    ):

        self.origin = origin
        self.destination = destination
        self.route_id = route_id

    def to_record(self) -> dict:
        return {
            "origin": self.origin.location_id,
            "destination": self.destination.location_id,
        }
