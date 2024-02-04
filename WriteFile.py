def write_text_seconds_node():
    f1 = open("Iris/iris.data.ver_preprocess.txt", "r")
    f2 = open("Iris/petal_length_middle/middle.txt", "w")

    x = f1.readlines()

    for i in range(0, len(x)):
        data = x[i].split(",")

        if data[2] == 'petal_length_M':
            del data[2]
            result = ",".join(data[:2] + data[2:])
            f2.write(result)


def write_text_third_node():
    f1 = open("Iris/petal_length_middle/middle.txt", "r")
    f2 = open("Iris/petal_length_middle/petal_width_middle/middle.txt", "w")

    x = f1.readlines()

    for i in range(0, len(x)):
        data = x[i].split(",")

        if data[2] == 'petal_width_M':
            del data[2]
            result = ",".join(data[:2] + data[2:])
            f2.write(result)


def write_text_fourth_node_left():
    f1 = open("Iris/petal_length_middle/petal_width_middle/middle.txt", "r")
    f2 = open("Iris/petal_length_middle/petal_width_middle/sepal_length_left/left.txt", "w")

    x = f1.readlines()

    for i in range(0, len(x)):
        data = x[i].split(",")

        if data[0] == 'sepal_length_L':
            del data[0]
            result = ",".join(data)
            f2.write(result)


def write_text_fourth_node_middle():
    f1 = open("Iris/petal_length_middle/petal_width_middle/middle.txt", "r")
    f2 = open("Iris/petal_length_middle/petal_width_middle/sepal_length_middle/middle.txt", "w")

    x = f1.readlines()

    for i in range(0, len(x)):
        data = x[i].split(",")

        if data[0] == 'sepal_length_M':
            del data[0]
            result = ",".join(data)
            f2.write(result)
