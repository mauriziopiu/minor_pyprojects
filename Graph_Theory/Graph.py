import pygame
import math


class Graph(object):

    def __init__(self, isDirected=False):
        self.isDirected = isDirected
        self.nodes = []
        self.edges = []

    def addNode(self, win, x, y):
        new_node = Node(x, y)
        self.nodes.append(new_node)
        new_node.draw(win)

    def isNodeAt(self, x, y):
        for node in self.nodes:
            if node.x_left <= x <= node.x_right:
                if node.y_upper <= y <= node.y_lower:
                    return True
        return False

    def getNodeAt(self, x, y):
        # Assert that (x, y) contains a node
        for node in self.nodes:
            if node.x_left <= x <= node.x_right:
                if node.y_upper <= y <= node.y_lower:
                    return node

    def addEdge(self, win, start_node, end_node, weight=1):
        new_edge = Edge(start_node, end_node)
        self.edges.append(new_edge)
        start_node.addEdge(new_edge)
        end_node.addEdge(new_edge)
        new_edge.draw(win)

    def isEdgeAt(self, x, y):
        pass

    def getEdgeAt(self, x, y):
        pass


class Node(object):

    def __init__(self, x, y, color=(255, 0, 0), radius=10):
        self.x = x
        self.x_left = x - radius
        self.x_right = x + radius

        self.y = y
        self.y_upper = y - radius
        self.y_lower = y + radius

        self.color = color
        self.radius = radius
        self.edges = []

    def addEdge(self, edge):
        self.edges.append(edge)

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class Edge(object):

    def __init__(self, start_node, end_node, color=(0, 0, 0), width=3, weight=1):
        self.start_node = start_node
        self.start_node.x = start_node.x
        self.start_node.y = start_node.y

        self.end_node = end_node
        self.end_node_x = end_node.x
        self.end_node_y = end_node.y

        self.delta_x = self.end_node.x - self.start_node.x
        self.delta_y = self.end_node.y - self.start_node.y
        self.hyp = math.sqrt(self.delta_x**2 + self.delta_y**2)
        self.normalized_dir_vx = self.delta_x // self.hyp
        self.normalized_dir_vy = self.delta_y // self.hyp
        self.direction = math.acos(self.delta_y // self.hyp)        # not sure

        self.color = color
        self.width = width
        self.weight = weight

    def draw(self, win):
        pygame.draw.line(win, self.color, (self.start_node.x, self.start_node.y), (self.end_node.x, self.end_node.y),
                         self.width)

    def drawDirection(self, win):
        tip_x = self.end_node.x + math.sin(self.end_node.radius)
        tip_y = self.end_node.y - math.cos(self.end_node.radius)
        tip = tip_x, tip_y
        pygame.draw.polygon()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def main():
    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Graph")
    clock = pygame.time.Clock()
    run = True

    graph = Graph()
    nodeStorage = []

    while run:
        clock.tick(27)
        win.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if graph.isNodeAt(pos[0], pos[1]) and len(graph.nodes) >= 2:  # Click on Node (-> Add Edge)
                    if len(nodeStorage) == 0:  # No node chosen
                        nodeStorage.append((pos[0], pos[1]))
                    elif len(nodeStorage) == 1:  # First node chosen
                        start_node = graph.getNodeAt(nodeStorage[0][0], nodeStorage[0][1])
                        end_node = graph.getNodeAt(pos[0], pos[1])
                        graph.addEdge(win, start_node, end_node)
                        nodeStorage.clear()
                if graph.isEdgeAt(pos[0], pos[1]):
                    pass
                else:  # Click into space (-> Add Node)
                    graph.addNode(win, pos[0], pos[1])

        for edge in graph.edges:
            edge.draw(win)

        for node in graph.nodes:
            node.draw(win)

        pygame.display.update()


main()
