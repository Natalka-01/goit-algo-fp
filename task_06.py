items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Розрахунок співвідношення калорій до вартості
    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]['calories'] / x[1]['cost'],
        reverse=True
    )

    total_cost = 0
    chosen_items = []

    for name, data in sorted_items:
        if total_cost + data['cost'] <= budget:
            chosen_items.append(name)
            total_cost += data['cost']

    return chosen_items

def dynamic_programming(items, budget):
    # Перетворення списку елементів для зручності
    names = list(items.keys())
    costs = [items[name]['cost'] for name in names]
    calories = [items[name]['calories'] for name in names]
    n = len(names)

    # Ініціалізація таблиці динамічного програмування
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Заповнення таблиці
    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - costs[i-1]] + calories[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    # Відновлення обраних елементів
    w = budget
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(names[i-1])
            w -= costs[i-1]

    selected_items.reverse()  # Для збереження порядку
    return selected_items


budget = 100

print("Greedy Algorithm result:")
print(greedy_algorithm(items, budget))

print("Dynamic Programming result:")
print(dynamic_programming(items, budget))
