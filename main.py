import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import datetime

from core import pso, topologies, fitness_functions


def run_experiments_and_plot_graphs(fitness_function_name, fitness_function, topology):
    mpl.style.use('seaborn')

    list_global_best_values, runs = main(1, topology, fitness_function)
    description = f"Constant Inertia - {fitness_function_name} - {topology}"
    plot_boxplot(runs, fitness_function_name, description)

    list_global_best_values, runs = main(2, topology, fitness_function)
    description = f"Linear Inertia - {fitness_function_name} - {topology}"
    plot_boxplot(runs, fitness_function_name, description)

    list_global_best_values, runs = main(3, topology, fitness_function)
    description = f"Clerc - {fitness_function_name} - {topology}"
    plot_boxplot(runs, fitness_function_name, description)

    plot_covergence_graphs(fitness_function_name, fitness_function, topology)


def plot_covergence_graphs(fitness_function_name, fitness_function, topology):
    mpl.style.use('seaborn')
    fig, ax = plt.subplots()
    list_global_best_values, runs = main(1, topology, fitness_function)
    ax.plot(list(range(0, 10000)), list_global_best_values, 'b', label=f"Constant - Best: {list_global_best_values[-1]:.2f}")
    ax.set_title("PSO Local Topology")
    ax.set_ylabel("Best Fitness")
    ax.set_xlabel("Iterations")

    list_global_best_values, runs = main(2, topology, fitness_function)
    ax.plot(list(range(0, 10000)), list_global_best_values, 'r', label=f"Linear - Best: {list_global_best_values[-1]:.2f}")

    list_global_best_values, runs = main(3, topology, fitness_function)
    ax.plot(list(range(0, 10000)), list_global_best_values, 'g', label=f"Clerc - Best: {list_global_best_values[-1]:.2f}")
    ax.legend()
    plt.savefig(f'PSO Convergence {fitness_function_name} {topology} Average 30 runs_2.png')


def plot_boxplot(best_fitness, function_name, description):
    fig1, ax1 = plt.subplots()
    ax1.set_title(f'BoxPlot Best Fitness for {function_name}: {description}')
    ax1.boxplot(best_fitness, patch_artist=True, showfliers=False)
    ax1.legend()
    plt.savefig(f'PSO {description} Boxplot {function_name}_2.png')


def save_global_best_values(inertia_type, pso_algorithm):
    now = datetime.now().strftime("%d-%m-%Y%H:%M:%S")
    filepath = f"results/{inertia_type}-{now}.txt"
    with open(filepath, "w") as f:
        f.write(f"[\n")
        for i in pso_algorithm.list_global_best_values:
            f.write(f"{str(i)},\n")
        f.write(f"]")


def main(inertia_type, topology, fitness_function):
    runs = []
    for _ in range(30):
        pso_algorithm = pso.PSOAlgorithm(
            topology=topology,
            bound= [-32,32],
            dimensions=30,
            num_particles=30,
            num_iterations=10000,
            max_speed=[-1, 1],
            fitness_function=fitness_function,
        )
        pso_algorithm.search(inertia_type)
        runs.append(pso_algorithm.list_global_best_values)

    return np.average(runs, axis=0), runs


topology_l = topologies.Local(max_speed=[-1, 1])
topology_g = topologies.Global(max_speed=[-1, 1])

# run_experiments_and_plot_graphs("Rastrigin", fitness_functions.rastrigin_function, topology_l)
# run_experiments_and_plot_graphs("Rastrigin", fitness_functions.rastrigin_function, topology_g)
# run_experiments_and_plot_graphs("Rosenbrocks", fitness_functions.rosenbrocks_function, topology_l)
run_experiments_and_plot_graphs("Rosenbrocks", fitness_functions.rosenbrocks_function, topology_g)
