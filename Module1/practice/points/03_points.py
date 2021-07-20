class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y



def distance(p1, p2):
    return ((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**(1/2)


def max_dlina():
    points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
    start = Point(0, 0)
    k = [] #список всех расстояний от каждой точки до начала координат
    dlina = 0
    for point in points:
        dlina = distance(point, start)
        k.append(dlina)
    return max(k)


print("Координаты наиболее удаленной точки = ", max_dlina())
