from spatial import Point

p = Point("A", 121.0, 14.6)
print(p.id, p.lon, p.lat)
print(p.to_tuple())
print(p.is_poi())

r = Point("B", 123.0, 15.6)
print(r.id, r.lon, r.lat)
print(p.distance_to(r))

q = Point("X", 999, 14)
print(q.id, q.lon, q.lat)