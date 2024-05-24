import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)

# Оголошення змінних, які відображають кількість вироблених напоїв
# x1 - кількість одиниць "Лимонаду", x2 - кількість одиниць "Фруктового соку"
x1 = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
x2 = pulp.LpVariable('Fruit Juice', lowBound=0, cat='Integer')

# Додавання обмежень на кількість ресурсів
# Води: 2x1 + x2 <= 100
model += 2 * x1 + x2 <= 100, "Water"
# Цукру: x1 <= 50
model += x1 <= 50, "Sugar"
# Лимонного соку: x1 <= 30
model += x1 <= 30, "Lemon Juice"
# Фруктового пюре: 2x2 <= 40
model += 2 * x2 <= 40, "Fruit Puree"

# Визначення цільової функції для максимізації загальної кількості продуктів
model += x1 + x2, "Total Production"

model.solve()

print("Результати виробництва:")
for var in model.variables():
    print(f"{var.name} = {var.varValue}")

print("Загальна кількість продукції:", pulp.value(model.objective))
