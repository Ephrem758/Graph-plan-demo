from planning import *
from datetime import datetime

from search import astar_search, breadth_first_tree_search


start = datetime.now()



# Define problem
problem = PlanningProblem(initial='At(kuka, rest) & At(cabin, printer) & ~At(cabin, k_base)& ~At(kuka, duAro) & ~At(cabin, duAro)',
                           goals='At(kuka, duAro) & At(cabin, duAro)',
                           actions=[Action('pick_place(cabin, printer, k_base)',
                                           precond='At(kuka, printer) & At(cabin, printer)',
                                           effect='In(kuka, printer) & ~At(cabin, printer)& At(cabin, k_base)',
                                           domain='kuka & cabin & k_base & printer'),
                                    Action('move(kuka, rest, printer)',
                                           precond='At(kuka, rest)',
                                           effect='At(kuka,printer)',
                                           domain='kuka & printer'),
                                    Action('move_cabin(cabin, k_base, duAro)',
                                           precond='At(cabin, k_base) & At(kuka,printer)',
                                           effect='At(cabin, duAro) & ~At(cabin, k_base) & At(kuka, duAro)',
                                           domain='kuka & cabin & k_base & duAro')],
                           domain='kuka & cabin & k_base & duAro & printer')

# Planner
graphplan = GraphPlan(problem)

# Solve
solution = graphplan.execute()

# Linearize
lin_sol = linearize(solution)

# Print
print(lin_sol)

end = datetime.now()

#calculates the time of excution
td = (end - start).total_seconds() * 10**3
print(f"The time of execution: {td:.03f}ms")

