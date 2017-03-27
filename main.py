from pso import PSO
from problems import Rastrigin
from topologies import Global


def main():
    sphere = Rastrigin(30)
    topology = Global()
    pso = PSO(sphere, topology)
    result = []
    result = pso.search(2)

    file = open("testfile.txt", "w")

    file.write("\n")
    for item in result:
        for i in item:
            file.write("{}, ".format(i))
        file.write("\n")

    file.write("\n")
    file.close()

main()
