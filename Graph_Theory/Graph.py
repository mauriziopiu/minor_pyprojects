import pygame


class Graph(object):

    def __init__(self):
        self.nodes = []
        self.edges = []

    def updateGraph(self):
        pass

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
        new_edge.draw(win)


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

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class Edge(object):

    def __init__(self, start_node, end_node, color=(0, 0, 0), width=3, weight=1):
        self.start_node = start_node
        self.end_node = end_node
        self.color = color
        self.width = width
        self.weight = weight

    def draw(self, win):
        pygame.draw.line(win, self.color, (self.start_node.x, self.start_node.y), (self.end_node.x, self.end_node.y), self.width)


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
    edgePosition1 = []

    while run:
        clock.tick(27)
        win.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if graph.isNodeAt(pos[0], pos[1]) and len(graph.nodes) >= 2:  # Click on Node (-> Add Edge)
                    if len(edgePosition1) == 0:  # No node chosen
                        edgePosition1.append((pos[0], pos[1]))
                    elif len(edgePosition1) == 1:           # First node chosen
                        start_node = graph.getNodeAt(edgePosition1[0][0], edgePosition1[0][1])
                        end_node = graph.getNodeAt(pos[0], pos[1])
                        graph.addEdge(win, start_node, end_node)
                # elif False:                             # Click on Edge (-> Edit Edge)
                #   pass
                else:  # Click into space (-> Add Node)
                    graph.addNode(win, pos[0], pos[1])

        for edge in graph.edges:
            edge.draw(win)

        for node in graph.nodes:
            node.draw(win)

        pygame.display.update()


main()
