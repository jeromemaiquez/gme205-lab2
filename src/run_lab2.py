import os
import json
import matplotlib.pyplot as plt
from spatial import Point, PointSet

# ---------------------
# Paths
# ---------------------
DATA_PATH = "data/points.csv"
OUTPUT_DIR = "output"
SUMMARY_PATH = os.path.join(OUTPUT_DIR, "lab2_report.json")
PLOT_PATH = os.path.join(OUTPUT_DIR, "lab2_preview.png")

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

# ----------------------------
# Visualization and Reporting
# ----------------------------
point_set = PointSet.from_csv(DATA_PATH)
poi_set = point_set.filter_by_tag("poi")
bbox = point_set.bbox()
count = point_set.count()

point_lons = [point.lon for point in point_set.points]
point_lats = [point.lat for point in point_set.points]
poi_lons = [poi.lon for poi in poi_set.points]
poi_lats = [poi.lat for poi in poi_set.points]

plt.figure()
if count == 0:
    plt.title("Preview Plot (No valid coordinates to plot)")
else:
    plt.scatter(point_lons, point_lats, c="blue")
    plt.scatter(poi_lons, poi_lats, c="red")
    plt.title("PointSet Preview (blue = all points; red = POIs)")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")

plt.savefig(PLOT_PATH, dpi=150, bbox_inches="tight")
plt.close()

print(f"Saved scatter plot to: {PLOT_PATH}")
