import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#CCCCCC"  # Базовий сірий
        self.id = str(uuid.uuid4())


def build_sample_tree():
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    return root


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title="Tree Traversal"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [tree.nodes[n]["color"] for n in tree.nodes()]
    labels = {n: tree.nodes[n]["label"] for n in tree.nodes()}

    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors, with_labels=True,
            font_color='black', font_size=10)
    plt.title(title)
    plt.axis('off')
    plt.show()


def generate_purple_gradient(n, start_color=(75, 0, 130), end_color=(230, 204, 255)):
    colors = []
    for i in range(n):
        ratio = i / max(n - 1, 1)
        r = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * ratio)
        colors.append(f"#{r:02X}{g:02X}{b:02X}")
    return colors


def bfs(root):
    queue = deque([root])
    visited = []
    while queue:
        node = queue.popleft()
        if node:
            visited.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return visited


def dfs(root):
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        if node:
            visited.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return visited


def visualize_traversal(traversal_func, root, title):
    nodes_in_order = traversal_func(root)
    colors = generate_purple_gradient(len(nodes_in_order))

    for step, node in enumerate(nodes_in_order):
        node.color = colors[step]
        draw_tree(root, title=f"{title} - Step {step + 1}")


# Побудова дерева
tree_root = build_sample_tree()

# Візуалізація DFS
visualize_traversal(dfs, tree_root, title="DFS Traversal")

# Скидання кольорів
tree_root = build_sample_tree()

# Візуалізація BFS
visualize_traversal(bfs, tree_root, title="BFS Traversal")
