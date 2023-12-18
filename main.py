import heapq

class City:
    def __init__(self, name):
        self.name = name
        self.edges = []

class Edge:
    def __init__(self, dest, weight):
        self.dest = dest
        self.weight = weight

class NavigationSystem:
    def __init__(self):
        self.cities = {}

    def addCity(self, name):
        if name not in self.cities:
            self.cities[name] = City(name)

    def addConnection(self, city1, city2, weight):
        if city1 in self.cities and city2 in self.cities:
            edge1 = Edge(self.cities[city2], weight)
            edge2 = Edge(self.cities[city1], weight)
            self.cities[city1].edges.append(edge1)
            self.cities[city2].edges.append(edge2)

    def shortestPath(self, start, end):
        if start not in self.cities or end not in self.cities:
            return None

        distance = {city: float('inf') for city in self.cities}
        previous = {city: None for city in self.cities}
        visited = set()

        distance[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_city = heapq.heappop(priority_queue)

            if current_city in visited:
                continue

            visited.add(current_city)

            for edge in self.cities[current_city].edges:
                new_distance = distance[current_city] + edge.weight

                if new_distance < distance[edge.dest.name]:
                    distance[edge.dest.name] = new_distance
                    previous[edge.dest.name] = current_city
                    heapq.heappush(priority_queue, (new_distance, edge.dest.name))

        if distance[end] == float('inf'):
            return None  

        path = []
        current = end
        while current is not None:
            path.insert(0, current)
            current = previous[current]

        return path, distance[end]

# Example:
navigation_system = NavigationSystem()

navigation_system.addCity("A")
navigation_system.addCity("B")
navigation_system.addCity("C")

navigation_system.addConnection("A", "B", 1)
navigation_system.addConnection("B", "C", 2)
navigation_system.addConnection("A", "C", 4)

path, shortest_distance = navigation_system.shortestPath("A", "C")

print("Shortest Path:", path)
print("Shortest Distance:", shortest_distance)

