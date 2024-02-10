import numpy as np


def classification(pathfile):
    f = open(pathfile, "r")
    x = f.readlines()
    result = []
    choice = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
    true_false = np.zeros(2)
    iris_type = np.zeros(3)

    for i in range(0, len(x)):
        data = x[i].rstrip("\n").split(",")
        if data[2] == "petal_length_L":
            result.append(choice[0])
            iris_type[0] += 1
        elif data[2] == "petal_length_M":
            if data[3] == "petal_width_L":
                result.append(np.random.choice(choice))
            elif data[3] == "petal_width_M":
                if data[0] == "sepal_length_L":
                    result.append(choice[1])
                    iris_type[1] += 1
                elif data[0] == "sepal_length_M":
                    if data[1] == "sepal_width_H":
                        result.append(np.random.choice(choice))
                    else:
                        result.append(choice[1])
                        iris_type[1] += 1
                else:
                    result.append(choice[1])
                    iris_type[1] += 1
            else:
                result.append(choice[2])
                iris_type[2] += 1
        else:
            result.append(choice[2])
            iris_type[2] += 1

        if result[-1] == data[4]:
            true_false[0] += 1
        else:
            print("Line wrong is", i + 1)
            true_false[1] += 1
    print(iris_type)
    print(true_false)
    print(f"Accuracy value = {true_false[0]/sum(true_false)}\n")
