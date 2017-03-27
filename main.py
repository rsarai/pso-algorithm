from pso import PSO
from problems import Sphere
from topologies import Global


def main():
    sphere = Sphere(30)
    topology = Global()
    pso = PSO(sphere, topology)
    result = []
    result = pso.search(1)

    file = open("testfile.txt", "w")

    file.write("\n")
    for item in result:
        file.write("{}, ".format(item))
        file.write("\n")
    file.close()

main()
