""""module for a class containing location"""


class Location:

    location_id: int
    longitude: float
    latitude: float
    name: str

    def __init__(
            self,
            latitude: float,
            longitude: float,
            name: str,
            location_id: int = None
    ):
        self.longitude = longitude
        self.latitude = latitude
        self.name = name
        self.location_id = location_id

    def __str__(self) -> str:
        return f"x:{self.longitude:.14f} y:{self.latitude:.14f}"

    def to_record(self) -> dict:
        return {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "name": self.name,
        }
