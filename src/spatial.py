class Point:
    def __init__(self, id, lon, lat, name=None, tag=None):
        # Validation must happen INSIDE the object, not outside
        if not (-180 <= lon <= 180):
            raise ValueError("Longitude must be between -180 and 180")
        if not (-90 <= lat <= 90):
            raise ValueError("Latitude must be between -90 and 90")

        self.id = id
        self.lon = lon
        self.lat = lat
        
        # Allows the point geometry to represent a POI
        self.name = name
        self.tag = tag

    # ---------------------------------------------------
    # Instance methods (behavior belonging to the object)
    # ---------------------------------------------------

    def to_tuple(self) -> tuple[float, float]:
        """
        Return the coordinate as a (lon, lat) tuple.
        """
        return (self.lon, self.lat)