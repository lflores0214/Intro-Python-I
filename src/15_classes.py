# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
# YOUR CODE HERE:


class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# =============================================
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
# YOUR CODE HERE:


class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name

    def __str__(self):
        return str(vars(self))
# =============================================
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
# it inherits lat and lon and name from Waypoint and Waypoint inherits lat and lon from LatLon

# YOUR CODE HERE


class Geocache(Waypoint):
    def __init__(self, lat, lon, name, difficulty, size):
        super().__init__(lat, lon, name)
        self.difficulty = difficulty
        self.size = size

    def __str__(self):
        return str(vars(self))
    # the above ^ way is better
    # def __str__(self):
    #     s = f"Name: {self.name}, Difficulty: {self.difficulty}, Size: {self.size}, Latitude: {self.lat}, Longitude: {self.lon}"
    #     return s
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521


# YOUR CODE HERE
waypoint = Waypoint(41.70505, -121.51521, "catacombs")


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print("Waypoint: ", waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache(44.052137, -121.41556, "Newberry Views", 1.5, 2)
# Print it--also make this print more nicely
print("Geocache: ", geocache)
