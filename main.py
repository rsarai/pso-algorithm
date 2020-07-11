from datetime import datetime

from core import pso, topologies, fitness_functions


def main(inertia_type):
    topology = topologies.Global(max_speed=[-6, 6])
    pso_algorithm = pso.PSOAlgorithm(
        topology=topology,
        bound= [-100,100],
        dimensions=30,
        num_particles=30,
        num_iterations=10000,
        max_speed=[-6, 6],
        fitness_function=fitness_functions.ackley_function,
    )

    inertia_options = {
        1: "Constant: 0.8",
        2: "Linear: 0.4 < w < 0.9",
        3: "Clerc",
    }
    pso_algorithm.search(inertia_type)

    specs = (
        f"Topology: {str(topology)}\n"
        f"Inertia: {inertia_options[inertia_type]}\n"
    )
    now = datetime.now().strftime("%d-%m-%Y%H:%M:%S")
    filepath = f"results/{inertia_type}-{now}.txt"
    with open(filepath, "w") as f:
        f.write(specs)
        f.write(f"[\n")
        for i in pso_algorithm.list_global_best_values:
            f.write(f"{str(i)},\n")
        f.write(f"]")
    return pso_algorithm.list_global_best_values, specs

graph_info = []


import matplotlib as mpl
import matplotlib.pyplot as plt


mpl.style.use('seaborn')
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)
list_global_best_values, specs = main(1)
ax1.plot(list(range(0, 40)), list_global_best_values[:40])
ax1.set_xlabel("Iterations")
ax1.set_ylabel("Best Fitness")
ax1.text(20, 200, specs)

list_global_best_values, specs = main(2)
ax2.plot(list(range(0, 40)), list_global_best_values[:40])
ax2.set_xlabel("Iterations")
ax2.set_ylabel("Best Fitness")
ax2.text(20, 200, specs)

list_global_best_values, specs = main(3)
ax3.plot(list(range(0, 40)), list_global_best_values[:40])
ax3.set_xlabel("Iterations")
ax3.set_ylabel("Best Fitness")
ax3.text(20, 200, specs)

plt.show()
