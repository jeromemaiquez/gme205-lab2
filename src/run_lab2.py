from spatial import Point, PointSet

# ---------------------
# Paths
# ---------------------
DATA_PATH = "data/points.csv"

# ---------------------
# Tests for Point class
# ---------------------

print("Tests for Point Class")

# Test for Point, to_tuple(), is_poi()
p = Point("A", 121.0, 14.6)
print(p.id, p.lon, p.lat)
print(p.to_tuple())
print(p.is_poi())

# Test for distance_to() and haversine_m()
r = Point("B", 123.0, 15.6)
print(r.id, r.lon, r.lat)
print(p.distance_to(r))

# Test for Point.from_row()
s = {
    "id": "C",
    "lon": 124.0,
    "lat": 16.6,
    "name": "C",
    "tag": "poi"
}
t = Point.from_row(s)
print(t.id, t.lon, t.lat, t.name, t.tag)

# Test for validity check
# Commented out to allow script to run
# q = Point("X", 999, 14)
# print(q.id, q.lon, q.lat)

# --------------------------
# Tests for PointSet class
# --------------------------

# Test for PointSet instantiation
u = PointSet([p, r, t])
for point in u.points:
    print(point.id, point.lon, point.lat)

# Test for PointSet.from_csv()
point_set = PointSet.from_csv(DATA_PATH)
print(type(point_set))

print("\nPoints inside PointSet")
for point in point_set.points:
    print(point.id, point.lon, point.lat, point.name, point.tag)

print("\nTest for PointSet instance methods")
print(point_set.count())
print(point_set.bbox())

new_point_set = point_set.filter_by_tag("poi")
for point in new_point_set.points:
    print(point.id, point.lon, point.lat, point.name, point.tag)