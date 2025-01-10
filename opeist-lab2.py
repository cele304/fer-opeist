import numpy as np
from pulp import LpProblem, LpMinimize, LpVariable, lpSum
from pulp import PULP_CBC_CMD, PULP_CHOCO_CMD


np.random.seed(3652960821)

mali_costs = np.random.randint(1, 21, size=(8,8))
veliki_costs = np.random.randint(1, 21, size=(16,16))


def construct_problem(costs):
    problem = LpProblem("Opeist-lab2", LpMinimize)

    matrix_range = np.arange(costs.shape[0]).tolist()

    x = LpVariable.dicts(name="x", indices=(matrix_range, matrix_range), lowBound=0, upBound=1, cat=LpBinary)   #u edgaru indexs, a ne indices

    polje = []
    for i in matrix_range:
        for j in matrix_range:
            polje.append(costs[i][j] * x[i][j])

    problem += lpSum(polje)

    for i in matrix_range:
        problem += lpSum([x[i][j] for j in matrix_range]) == 1

    for j in matrix_range:
        problem += lpSum([x[i][j] for i in matrix_range]) == 1

    return problem


def solve_LP(model):
    model.solve(PULP_CBC_CMD(msg=0))   

def solve_CP(model):
    model.solve(PULP_CHOCO_CMD(msg=0))




                            












