import random
import matplotlib.pyplot as plt

# Кількість симуляцій
num_simulations = 1_000_000

# Лічильник сум
sum_counts = {i: 0 for i in range(2, 13)}

# Симуляція кидків
for _ in range(num_simulations):
    roll_sum = random.randint(1, 6) + random.randint(1, 6)
    sum_counts[roll_sum] += 1

# Обчислення ймовірностей
monte_carlo_probs = {k: v / num_simulations * 100 for k, v in sum_counts.items()}

# Аналітичні ймовірності
analytical_probs = {
    2: 1/36 * 100,
    3: 2/36 * 100,
    4: 3/36 * 100,
    5: 4/36 * 100,
    6: 5/36 * 100,
    7: 6/36 * 100,
    8: 5/36 * 100,
    9: 4/36 * 100,
    10: 3/36 * 100,
    11: 2/36 * 100,
    12: 1/36 * 100,
}

# Виведення результатів у вигляді таблиці
print(f"{'Сума':<5} {'Монте-Карло':<15} {'Аналітична':<15}")
for s in range(2, 13):
    print(f"{s:<5} {monte_carlo_probs[s]:<15.2f} {analytical_probs[s]:<15.2f}")

# Побудова графіка
sums = list(range(2, 13))
mc_values = [monte_carlo_probs[s] for s in sums]
an_values = [analytical_probs[s] for s in sums]

plt.figure(figsize=(10, 6))
plt.plot(sums, mc_values, marker='o', label='Монте-Карло')
plt.plot(sums, an_values, marker='x', label='Аналітична')
plt.title("Ймовірність сум при киданні двох кубиків")
plt.xlabel("Сума")
plt.ylabel("Ймовірність (%)")
plt.legend()
plt.grid(True)
plt.show()
