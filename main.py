import numpy as np

from datetime import datetime

from core import pso, topologies, fitness_functions



def run_experiments_and_plot_graphs():
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    mpl.style.use('seaborn')

    list_global_best_values = main(1)
    fig, ax = plt.subplots()
    ax.plot(list(range(0, 10000)), list_global_best_values[:10000], 'b', label=f"Constant - Best: {list_global_best_values[-1]:.2f}")
    ax.set_title("PSO Local Topology")
    ax.set_xlabel("Iterations")
    ax.set_ylabel("Best Fitness")

    list_global_best_values = main(2)
    ax.plot(list(range(0, 10000)), list_global_best_values[:10000], 'r', label=f"Linear - Best: {list_global_best_values[-1]:.2f}")

    list_global_best_values = main(3)
    ax.plot(list(range(0, 10000)), list_global_best_values[:10000], 'g', label=f"Clerc - Best: {list_global_best_values[-1]:.2f}")
    ax.legend()

    plt.show()


def save_global_best_values(inertia_type, pso_algorithm):
    now = datetime.now().strftime("%d-%m-%Y%H:%M:%S")
    filepath = f"results/{inertia_type}-{now}.txt"
    with open(filepath, "w") as f:
        f.write(f"[\n")
        for i in pso_algorithm.list_global_best_values:
            f.write(f"{str(i)},\n")
        f.write(f"]")


def main(inertia_type):
    runs = []
    topology = topologies.Local(max_speed=[-6, 6])

    for _ in range(10):
        pso_algorithm = pso.PSOAlgorithm(
            topology=topology,
            bound= [-100,100],
            dimensions=30,
            num_particles=30,
            num_iterations=10000,
            max_speed=[-6, 6],
            fitness_function=fitness_functions.ackley_function,
        )
        pso_algorithm.search(inertia_type)
        runs.append(pso_algorithm.list_global_best_values)

    return np.average(runs, axis=0)


run_experiments_and_plot_graphs()
