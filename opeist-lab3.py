from pulp import LpProblem, LpMaximize, LpVariable, LpContinuous, lpSum
import numpy as np

def construct_LP_equivalent():

    prob = LpProblem("Robusni", LpMaximize)
		
    x1 = LpVariable("x1", lowBound=0, upBound=4, cat=LpContinuous)
    x2 = LpVariable("x2", lowBound=0, upBound=6, cat=LpContinuous)
		
    U1 = 4
		
    p1 = LpVariable.dicts(name="p1", indices=range(U1), lowBound=0, cat=LpContinuous)   #u edgaru obavezno indexs, ovdje indices
		
    D1 = np.array([[-1,1], [1,-1], [-1,-1], [1,1]])
		
    d1 = np.array([0,2,-4,6]).T
	
    prob += 3*x1 + 5*x2
    prob += x1 <= 4
    prob += x2 <= 6
	
    prob += lpSum([ p1[i] * d1[i] for i in range(U1)]) <= 18
    
    prob += lpSum([ p1[i] * D1[i, 0] for i in range(U1)]) == x1
    prob += lpSum([ p1[i] * D1[i, 1] for i in range(U1)]) == x2
	
    dictionary = {"x1" : x1, "x2" : x2}
    return prob, dictionary
		


prob, dictionary = construct_LP_equivalent()
prob.solve()

for v in prob.variables():
    print(f"{v.name} = {v.varValue}")

print(f"Ciljna funkcija: {prob.objective.value()}")









