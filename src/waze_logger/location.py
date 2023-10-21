""""module for a class containing location"""


class Location:

    longitude: float
    latitude: float

    def __init__(self, lat: float, long: float):
        self.longitude = long
        self.latitude = lat

    def __str__(self) -> str:
        return f"x:{self.longitude:.14f} y:{self.latitude:.14f}"
