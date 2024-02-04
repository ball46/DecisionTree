from Dtreefunc import *

md_sepal_length = [5.84 - 0.83, 5.84 + 0.83]
md_sepal_width = [3.05 - 0.43, 3.05 + 0.43]
md_petal_length = [3.76 - 1.76, 3.76 + 1.76]
md_petal_width = [1.20 - 0.76, 1.20 + 0.76]

sl_mapping = {'sepal_length_L': 0, 'sepal_length_M': 1, 'sepal_length_H': 2}
sw_mapping = {'sepal_width_L': 0, 'sepal_width_M': 1, 'sepal_width_H': 2}
pl_mapping = {'petal_length_L': 0, 'petal_length_M': 1, 'petal_length_H': 2}
pw_mapping = {'petal_width_L': 0, 'petal_width_M': 1, 'petal_width_H': 2}


def preprocessing_data():
    f1 = open("Iris/iris.data", "r")
    f2 = open("Iris/iris.data.ver_preprocess.txt", "w")

    x = f1.readlines()

    for i in range(0, len(x)):
        data = x[i].split(",")

        num = float(data[0])
        sepal_length_type = "sepal_length_L" if num < md_sepal_length[0] \
            else ("sepal_length_M" if md_sepal_length[0] <= num <= md_sepal_length[1] else "sepal_length_H")

        num = float(data[1])
        sepal_width_type = "sepal_width_L" if num < md_sepal_width[0] \
            else ("sepal_width_M" if md_sepal_width[0] <= num <= md_sepal_width[1] else "sepal_width_H")

        num = float(data[2])
        petal_length_type = "petal_length_L" if num < md_petal_length[0] \
            else ("petal_length_M" if md_petal_length[0] <= num <= md_petal_length[1] else "petal_length_H")

        num = float(data[3])
        petal_width_type = "petal_width_L" if num < md_petal_width[0] \
            else ("petal_width_M" if md_petal_width[0] <= num <= md_petal_width[1] else "petal_width_H")

        f2.write(f"{sepal_length_type},{sepal_width_type},{petal_length_type},{petal_width_type},{data[4]}")


def calculate_information_gain_for_iris():
    f = open("Iris/iris.data.ver_preprocess.txt", "r")
    x = f.readlines()

    n = 3  # col(3 class)
    m = 4  # row

    sepal_length = np.zeros(3)
    sepal_length_ci = [[0 for _ in range(m)] for _ in range(n)]

    sepal_width = np.zeros(3)
    sepal_width_ci = [[0 for _ in range(m)] for _ in range(n)]

    petal_length = np.zeros(3)
    petal_length_ci = [[0 for _ in range(m)] for _ in range(n)]

    petal_width = np.zeros(3)
    petal_width_ci = [[0 for _ in range(m)] for _ in range(n)]

    iris = np.zeros(3)

    for i in range(0, len(x)):
        data = x[i].split(",")

        sepal_length_type = sl_mapping.get(data[0])
        sepal_length[sepal_length_type] += 1

        sepal_width_type = sw_mapping.get(data[1])
        sepal_width[sepal_width_type] += 1

        petal_length_type = pl_mapping.get(data[2])
        petal_length[petal_length_type] += 1

        petal_width_type = pw_mapping.get(data[3])
        petal_width[petal_width_type] += 1

        iris_mapping = {'Iris-setosa\n': 0, 'Iris-versicolor\n': 1, 'Iris-virginica\n': 2}
        iris_type = iris_mapping.get(data[4])
        iris[iris_type] += 1

        sepal_length_ci[sepal_length_type][iris_type] += 1
        sepal_width_ci[sepal_width_type][iris_type] += 1
        petal_length_ci[petal_length_type][iris_type] += 1
        petal_width_ci[petal_width_type][iris_type] += 1

    info_d = entropy_new_version(iris)

    for i in range(3):
        sepal_length_ci[i][3] = entropy_new_version(
            [sepal_length_ci[i][0], sepal_length_ci[i][1], sepal_length_ci[i][2]])
        sepal_width_ci[i][3] = entropy_new_version(
            [sepal_width_ci[i][0], sepal_width_ci[i][1], sepal_width_ci[i][2]])
        petal_length_ci[i][3] = entropy_new_version(
            [petal_length_ci[i][0], petal_length_ci[i][1], petal_length_ci[i][2]])
        petal_width_ci[i][3] = entropy_new_version(
            [petal_width_ci[i][0], petal_width_ci[i][1], petal_width_ci[i][2]])

    info_sepal_length_d = inforD(sepal_length, [sepal_length_ci[0][3],
                                                sepal_length_ci[1][3], sepal_length_ci[2][3]])
    info_sepal_width_d = inforD(sepal_width, [sepal_width_ci[0][3], sepal_width_ci[1][3], sepal_width_ci[2][3]])
    info_petal_length_d = inforD(petal_length, [petal_length_ci[0][3], petal_length_ci[1][3], petal_length_ci[2][3]])
    info_petal_width_d = inforD(petal_width, [petal_width_ci[0][3], petal_width_ci[1][3], petal_width_ci[2][3]])

    print("Sepal length count is", sepal_length)
    print("Sepal width count is", sepal_width)
    print("Petal length count is", petal_length)
    print("Petal width count is", petal_width)
    print("Iris computer count is", iris)

    print("\nSepal length Info relate to class", sepal_length_ci)
    print("Sepal width Info relate to class", sepal_width_ci)
    print("Petal length Info relate to class", petal_length_ci)
    print("Petal width rating Info relate to class", petal_width_ci)

    print("\nInfo(D) is %5.3f" % info_d)
    print("Info(Sepal length (< mean - SD) is %5.3f" % sepal_length_ci[0][3])
    print("Info(Sepal length ([mean - SD, mean + SD]) is %5.3f" % sepal_length_ci[1][3])
    print("Info(Sepal length (> mean + SD) is %5.3f" % sepal_length_ci[2][3])

    print("\nInfo(Sepal width (< mean - SD) is %5.3f" % sepal_width_ci[0][3])
    print("Info(Sepal width ([mean - SD, mean + SD]) is %5.3f" % sepal_width_ci[1][3])
    print("Info(Sepal width (> mean + SD) is %5.3f" % sepal_width_ci[2][3])

    print("\nInfo(Petal length (< mean - SD) is %5.3f" % petal_length_ci[0][3])
    print("Info(Petal length ([mean - SD, mean + SD]) is %5.3f" % petal_length_ci[1][3])
    print("Info(Petal length (> mean + SD) is %5.3f" % petal_length_ci[2][3])

    print("\nInfo(Petal width (< mean - SD) is %5.3f" % petal_width_ci[0][3])
    print("Info(Petal width ([mean - SD, mean + SD]) is %5.3f" % petal_width_ci[1][3])
    print("Info(Petal width (> mean + SD) is %5.3f" % petal_width_ci[2][3])

    print("\nInfo Sepal length (D) is %5.3f" % info_sepal_length_d)
    print("Info Sepal width (D) is %5.3f" % info_sepal_width_d)
    print("Info Petal length (D) is %5.3f" % info_petal_length_d)
    print("Info Petal width (D) is %5.3f" % info_petal_width_d)

    print("\n***Gain results of all dataset***")
    gain_sepal_length = info_d - info_sepal_length_d
    print("Gain (sepal_length) is %5.3f" % gain_sepal_length)
    gain_sepal_width = info_d - info_sepal_width_d
    print("Gain (sepal_width) is %5.3f" % gain_sepal_width)
    gain_petal_length = info_d - info_petal_length_d
    print("Gain (petal_length) is %5.3f" % gain_petal_length)
    gain_petal_width = info_d - info_petal_width_d
    print("Gain (petal_width) is %5.3f" % gain_petal_width)

    result_all = [gain_sepal_length, gain_sepal_width, gain_petal_length, gain_petal_width]
    max_gain = max(result_all)
    pos = np.argmax(result_all)
    print("\nmax gain of attb is %5.3f" % max_gain, "position is", pos)


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


def secondary_information_gain():
    f = open("Iris/petal_length_middle/middle.txt", "r")
    x = f.readlines()

    n = 3  # col(3 class)
    m = 3  # row

    sepal_length = np.zeros(3)
    sepal_length_ci = [[0 for _ in range(m)] for _ in range(n)]

    sepal_width = np.zeros(3)
    sepal_width_ci = [[0 for _ in range(m)] for _ in range(n)]

    petal_width = np.zeros(3)
    petal_width_ci = [[0 for _ in range(m)] for _ in range(n)]

    iris = np.zeros(2)

    for i in range(0, len(x)):
        data = x[i].split(",")

        sepal_length_type = sl_mapping.get(data[0])
        sepal_length[sepal_length_type] += 1

        sepal_width_type = sw_mapping.get(data[1])
        sepal_width[sepal_width_type] += 1

        petal_width_type = pw_mapping.get(data[2])
        petal_width[petal_width_type] += 1

        iris_mapping = {'Iris-versicolor\n': 0, 'Iris-virginica\n': 1}
        iris_type = iris_mapping.get(data[3])
        iris[iris_type] += 1

        sepal_length_ci[sepal_length_type][iris_type] += 1
        sepal_width_ci[sepal_width_type][iris_type] += 1
        petal_width_ci[petal_width_type][iris_type] += 1

    info_d = entropy_new_version(iris)

    for i in range(3):
        sepal_length_ci[i][2] = entropy_new_version([sepal_length_ci[i][0], sepal_length_ci[i][1]])
        sepal_width_ci[i][2] = entropy_new_version([sepal_width_ci[i][0], sepal_width_ci[i][1]])
        petal_width_ci[i][2] = entropy_new_version([petal_width_ci[i][0], petal_width_ci[i][1]])

    info_sepal_length_d = inforD(sepal_length, [sepal_length_ci[0][2],
                                                sepal_length_ci[1][2], sepal_length_ci[2][2]])
    info_sepal_width_d = inforD(sepal_width, [sepal_width_ci[0][2], sepal_width_ci[1][2], sepal_width_ci[2][2]])
    info_petal_width_d = inforD(petal_width, [petal_width_ci[0][2], petal_width_ci[1][2], petal_width_ci[2][2]])

    print("Sepal length count is", sepal_length)
    print("Sepal width count is", sepal_width)
    print("Petal width count is", petal_width)
    print("Iris computer count is", iris)

    print("\nSepal length Info relate to class", sepal_length_ci)
    print("Sepal width Info relate to class", sepal_width_ci)
    print("Petal width rating Info relate to class", petal_width_ci)

    print("\nInfo(D) is %5.3f" % info_d)
    print("Info(Sepal length (< mean - SD) is %5.3f" % sepal_length_ci[0][2])
    print("Info(Sepal length ([mean - SD, mean + SD]) is %5.3f" % sepal_length_ci[1][2])
    print("Info(Sepal length (> mean + SD) is %5.3f" % sepal_length_ci[2][2])

    print("\nInfo(Sepal width (< mean - SD) is %5.3f" % sepal_width_ci[0][2])
    print("Info(Sepal width ([mean - SD, mean + SD]) is %5.3f" % sepal_width_ci[1][2])
    print("Info(Sepal width (> mean + SD) is %5.3f" % sepal_width_ci[2][2])

    print("\nInfo(Petal width (< mean - SD) is %5.3f" % petal_width_ci[0][2])
    print("Info(Petal width ([mean - SD, mean + SD]) is %5.3f" % petal_width_ci[1][2])
    print("Info(Petal width (> mean + SD) is %5.3f" % petal_width_ci[2][2])

    print("\nInfo Sepal length (D) is %5.3f" % info_sepal_length_d)
    print("Info Sepal width (D) is %5.3f" % info_sepal_width_d)
    print("Info Petal width (D) is %5.3f" % info_petal_width_d)

    print("\n***Gain results of all dataset***")
    gain_sepal_length = info_d - info_sepal_length_d
    print("Gain (sepal_length) is %5.3f" % gain_sepal_length)
    gain_sepal_width = info_d - info_sepal_width_d
    print("Gain (sepal_width) is %5.3f" % gain_sepal_width)
    gain_petal_width = info_d - info_petal_width_d
    print("Gain (petal_width) is %5.3f" % gain_petal_width)

    result_all = [gain_sepal_length, gain_sepal_width, gain_petal_width]
    max_gain = max(result_all)
    pos = np.argmax(result_all)
    print("\nmax gain of attb is %5.3f" % max_gain, "position is", pos)


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


def third_information_gain():
    f = open("Iris/petal_length_middle/petal_width_middle/middle.txt", "r")
    x = f.readlines()

    n = 3  # col(3 class)
    m = 3  # row

    sepal_length = np.zeros(3)
    sepal_length_ci = [[0 for _ in range(m)] for _ in range(n)]

    sepal_width = np.zeros(3)
    sepal_width_ci = [[0 for _ in range(m)] for _ in range(n)]

    iris = np.zeros(2)

    for i in range(0, len(x)):
        data = x[i].split(",")

        sepal_length_type = sl_mapping.get(data[0])
        sepal_length[sepal_length_type] += 1

        sepal_width_type = sw_mapping.get(data[1])
        sepal_width[sepal_width_type] += 1

        iris_mapping = {'Iris-versicolor\n': 0, 'Iris-virginica\n': 1}
        iris_type = iris_mapping.get(data[2])
        iris[iris_type] += 1

        sepal_length_ci[sepal_length_type][iris_type] += 1
        sepal_width_ci[sepal_width_type][iris_type] += 1

    info_d = entropy_new_version(iris)

    for i in range(3):
        sepal_length_ci[i][2] = entropy_new_version([sepal_length_ci[i][0], sepal_length_ci[i][1]])
        sepal_width_ci[i][2] = entropy_new_version([sepal_width_ci[i][0], sepal_width_ci[i][1]])

    info_sepal_length_d = inforD(sepal_length, [sepal_length_ci[0][2],
                                                sepal_length_ci[1][2], sepal_length_ci[2][2]])
    info_sepal_width_d = inforD(sepal_width, [sepal_width_ci[0][2], sepal_width_ci[1][2], sepal_width_ci[2][2]])

    print("Sepal length count is", sepal_length)
    print("Sepal width count is", sepal_width)
    print("Iris computer count is", iris)

    print("\nSepal length Info relate to class", sepal_length_ci)
    print("Sepal width Info relate to class", sepal_width_ci)

    print("\nInfo(D) is %5.3f" % info_d)
    print("Info(Sepal length (< mean - SD) is %5.3f" % sepal_length_ci[0][2])
    print("Info(Sepal length ([mean - SD, mean + SD]) is %5.3f" % sepal_length_ci[1][2])
    print("Info(Sepal length (> mean + SD) is %5.3f" % sepal_length_ci[2][2])

    print("\nInfo(Sepal width (< mean - SD) is %5.3f" % sepal_width_ci[0][2])
    print("Info(Sepal width ([mean - SD, mean + SD]) is %5.3f" % sepal_width_ci[1][2])
    print("Info(Sepal width (> mean + SD) is %5.3f" % sepal_width_ci[2][2])

    print("\nInfo Sepal length (D) is %5.3f" % info_sepal_length_d)
    print("Info Sepal width (D) is %5.3f" % info_sepal_width_d)

    print("\n***Gain results of all dataset***")
    gain_sepal_length = info_d - info_sepal_length_d
    print("Gain (sepal_length) is %5.3f" % gain_sepal_length)
    gain_sepal_width = info_d - info_sepal_width_d
    print("Gain (sepal_width) is %5.3f" % gain_sepal_width)

    result_all = [gain_sepal_length, gain_sepal_width]
    max_gain = max(result_all)
    pos = np.argmax(result_all)
    print("\nmax gain of attb is %5.3f" % max_gain, "position is", pos)


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


def fourth_left_information_gain():
    f = open("Iris/petal_length_middle/petal_width_middle/sepal_length_left/left.txt", "r")
    x = f.readlines()

    n = 3  # col(3 class)
    m = 3  # row

    sepal_width = np.zeros(3)
    sepal_width_ci = [[0 for _ in range(m)] for _ in range(n)]

    iris = np.zeros(2)

    for i in range(0, len(x)):
        data = x[i].split(",")

        sepal_width_type = sw_mapping.get(data[0])
        sepal_width[sepal_width_type] += 1

        iris_mapping = {'Iris-versicolor\n': 0, 'Iris-virginica\n': 1}
        iris_type = iris_mapping.get(data[1])
        iris[iris_type] += 1

        sepal_width_ci[sepal_width_type][iris_type] += 1

    info_d = entropy_new_version(iris)

    for i in range(3):
        sepal_width_ci[i][2] = entropy_new_version([sepal_width_ci[i][0], sepal_width_ci[i][1]])

    info_sepal_width_d = inforD(sepal_width, [sepal_width_ci[0][2], sepal_width_ci[1][2], sepal_width_ci[2][2]])

    print("Sepal width count is", sepal_width)
    print("Iris computer count is", iris)

    print("Sepal width Info relate to class", sepal_width_ci)

    print("\nInfo(D) is %5.3f" % info_d)
    print("Info(Sepal width (< mean - SD) is %5.3f" % sepal_width_ci[0][2])
    print("Info(Sepal width ([mean - SD, mean + SD]) is %5.3f" % sepal_width_ci[1][2])
    print("Info(Sepal width (> mean + SD) is %5.3f" % sepal_width_ci[2][2])

    print("\nInfo Sepal width (D) is %5.3f" % info_sepal_width_d)

    print("\n***Gain results of all dataset***")
    gain_sepal_width = info_d - info_sepal_width_d
    print("Gain (sepal_width) is %5.3f" % gain_sepal_width)


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


def fourth_middle_information_gain():
    f = open("Iris/petal_length_middle/petal_width_middle/sepal_length_middle/middle.txt", "r")
    x = f.readlines()

    n = 3  # col(3 class)
    m = 3  # row

    sepal_width = np.zeros(3)
    sepal_width_ci = [[0 for _ in range(m)] for _ in range(n)]

    iris = np.zeros(2)

    for i in range(0, len(x)):
        data = x[i].split(",")

        sepal_width_type = sw_mapping.get(data[0])
        sepal_width[sepal_width_type] += 1

        iris_mapping = {'Iris-versicolor\n': 0, 'Iris-virginica\n': 1}
        iris_type = iris_mapping.get(data[1])
        iris[iris_type] += 1

        sepal_width_ci[sepal_width_type][iris_type] += 1

    info_d = entropy_new_version(iris)

    for i in range(3):
        sepal_width_ci[i][2] = entropy_new_version([sepal_width_ci[i][0], sepal_width_ci[i][1]])

    info_sepal_width_d = inforD(sepal_width, [sepal_width_ci[0][2], sepal_width_ci[1][2], sepal_width_ci[2][2]])

    print("Sepal width count is", sepal_width)
    print("Iris computer count is", iris)

    print("Sepal width Info relate to class", sepal_width_ci)

    print("\nInfo(D) is %5.3f" % info_d)
    print("Info(Sepal width (< mean - SD) is %5.3f" % sepal_width_ci[0][2])
    print("Info(Sepal width ([mean - SD, mean + SD]) is %5.3f" % sepal_width_ci[1][2])
    print("Info(Sepal width (> mean + SD) is %5.3f" % sepal_width_ci[2][2])

    print("\nInfo Sepal width (D) is %5.3f" % info_sepal_width_d)

    print("\n***Gain results of all dataset***")
    gain_sepal_width = info_d - info_sepal_width_d
    print("Gain (sepal_width) is %5.3f" % gain_sepal_width)
