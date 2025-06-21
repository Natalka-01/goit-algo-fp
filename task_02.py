import matplotlib.pyplot as plt
import numpy as np

def draw_tree(x, y, angle, depth, length):
    if depth == 0:
        return

    # Обчислення кінцевої точки гілки
    x1 = x + length * np.cos(angle)
    y1 = y + length * np.sin(angle)

    # Малювання лінії (гілки)
    plt.plot([x, x1], [y, y1], color='brown', linewidth=1)

    # Рекурсивно малюємо дві нові гілки під кутами
    new_length = length * 0.7
    draw_tree(x1, y1, angle + np.pi/4, depth - 1, new_length)
    draw_tree(x1, y1, angle - np.pi/4, depth - 1, new_length)

def main():
    depth = int(input("Введіть рівень рекурсії (наприклад, 10): "))
    plt.figure(figsize=(8, 8))
    draw_tree(0, 0, np.pi/2, depth, 100)
    plt.axis('equal')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
