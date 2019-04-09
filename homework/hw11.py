import pulp

# define problem
model_A = pulp.LpProblem("Zero-Sum Battle for Trainer A", pulp.LpMaximize)

# define variables
payoff = pulp.LpVariable('payoff')
x1 = pulp.LpVariable('x1', lowBound=0)
x2 = pulp.LpVariable('x2', lowBound=0)
x3 = pulp.LpVariable('x3', lowBound=0)

# objective function
model_A += payoff

# constraints
model_A += payoff <= -10 * x1 + 4 * x2 + 6 * x3
model_A += payoff <= 3 * x1 - 1 * x2 - 9 * x3
model_A += payoff <= 3 * x1 - 3 * x2 + 2 * x3
model_A += x1 + x2 + x3 == 1

# solve problem
model_A.solve()
pulp.LpStatus[model_A.status]

print(model_A.name)
print("x1:", x1.varValue)
print("x2:", x2.varValue)
print("x3:", x3.varValue)
print("payoff:", payoff.varValue)

# define problem
model_B = pulp.LpProblem("Zero-Sum Battle for Trainer B", pulp.LpMinimize)

# define variables
payoff = pulp.LpVariable('payoff')
y1 = pulp.LpVariable('y1', lowBound=0)
y2 = pulp.LpVariable('y2', lowBound=0)
y3 = pulp.LpVariable('y3', lowBound=0)

# objective function
model_B += payoff

# constraints
model_B += payoff >= -10 * y1 + 3 * y2 + 3 * y3
model_B += payoff >= 4 * y1 - 1 * y2 - 3 * y3
model_B += payoff >= 6 * y1 - 9 * y2 + 2 * y3
model_B += y1 + y2 + y3 == 1

# solve problem
model_B.solve()
pulp.LpStatus[model_B.status]

print(model_B.name)
print("y1:", y1.varValue)
print("y2:", y2.varValue)
print("y3:", y3.varValue)
print("payoff:", payoff.varValue)

# define problem
model_C = pulp.LpProblem("Domination for Raw Player", pulp.LpMaximize)

# define variables
payoff = pulp.LpVariable('payoff')
x1 = pulp.LpVariable('x1', lowBound=0)
x2 = pulp.LpVariable('x2', lowBound=0)
x3 = pulp.LpVariable('x3', lowBound=0)

# objective function
model_C += payoff

# constraints
model_C += payoff <= 1 * x1 + 3 * x2 - 1 * x3
model_C += payoff <= 2 * x1 + 2 * x2 - 2 * x3
model_C += payoff <= -3 * x1 - 2 * x2 + 2 * x3
model_C += x1 + x2 + x3 == 1

# solve problem
model_C.solve()
pulp.LpStatus[model_C.status]

print(model_C.name)
print("x1:", x1.varValue)
print("x2:", x2.varValue)
print("x3:", x3.varValue)
print("payoff:", payoff.varValue)

# define problem
model_D = pulp.LpProblem("Domination for Column Player", pulp.LpMinimize)

# define variables
payoff = pulp.LpVariable('payoff')
y1 = pulp.LpVariable('y1', lowBound=0)
y2 = pulp.LpVariable('y2', lowBound=0)
y3 = pulp.LpVariable('y3', lowBound=0)

# objective function
model_D += payoff

# constraints
model_D += payoff >= 1 * y1 + 2 * y2 - 3 * y3
model_D += payoff >= 3 * y1 + 2 * y2 - 2 * y3
model_D += payoff >= -1 * y1 - 2 * y2 + 2 * y3
model_D += y1 + y2 + y3 == 1

# solve problem
model_D.solve()
pulp.LpStatus[model_D.status]

print(model_D.name)
print("y1:", y1.varValue)
print("y2:", y2.varValue)
print("y3:", y3.varValue)
print("payoff:", payoff.varValue)
