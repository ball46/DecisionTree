from Dtreefunc import *


def decision_tree(filename):
    f = open(filename, "r")
    x = f.readlines()

    iris_mapping = {}
    data_mapping = {}
    iris_data = {}
    iris_data_ci = {}
    info_d = {}
    gain = {}
    k = 0
    n = 3

    for i in range(0, len(x)):
        iris_type = x[i].rstrip("\n").split(",")[-1]

        if iris_type not in iris_mapping:
            iris_mapping[iris_type] = k
            k += 1

    data = x[0].split(",")
    m = len(data) - 1
    for j in range(m):
        name = data[j][:-2]
        iris_data[name] = np.zeros(n)
        data_mapping[name] = {}
        for k in range(0, 3):
            string = "_L" if k == 0 else ("_M" if k == 1 else "_H")
            data_mapping[name][name + string] = k
        iris_data_ci[name] = [[0 for _ in range(len(iris_mapping) + 1)] for _ in range(n)]
    iris_data["iris"] = np.zeros(len(iris_mapping))

    name_data = iris_data.keys()
    list_name = list(name_data)

    for i in range(len(x)):
        data = x[i].rstrip("\n").split(",")

        data_type = {}

        for j in range(len(list_name)):
            if j == len(list_name) - 1:
                data_type[list_name[j]] = iris_mapping[data[j]]
            else:
                data_type[list_name[j]] = data_mapping[list_name[j]][data[j]]
            iris_data[list_name[j]][data_type[list_name[j]]] += 1

        for j in range(0, len(list_name) - 1):
            iris_data_ci[list_name[j]][data_type[list_name[j]]][data_type[list_name[-1]]] += 1

    info_d["iris"] = entropy_new_version(iris_data["iris"])

    for i in range(len(list_name) - 1):
        for j in range(n):
            cal_data = []
            for k in range(len(iris_mapping)):
                cal_data.append(iris_data_ci[list_name[i]][j][k])
            iris_data_ci[list_name[i]][j][len(iris_mapping)] = entropy_new_version(cal_data)

    for i in range(len(list_name) - 1):
        cal_data = []
        for k in range(n):
            cal_data.append(iris_data_ci[list_name[i]][k][len(iris_mapping)])
        info_d[list_name[i]] = inforD(iris_data[list_name[i]], cal_data)
        gain[list_name[i]] = info_d["iris"] - info_d[list_name[i]]

    max_key = max(gain, key=gain.get)
    max_value = gain[max_key]
    max_gain = {max_key: max_value}
    log_data(iris_data, iris_data_ci, info_d, gain, max_gain)


def log_data(data_count, data_ci, data_info, data_gain, max_gain):
    print("***result of calculate***")
    for key, value in data_count.items():
        print(f"{key} count is", value)
    print("-" * 20)
    for key, value in data_ci.items():
        print(f"{key} Info relate to class", value)
    print("-" * 20)
    for key, value in data_ci.items():
        for i in range(len(value)):
            string = "< mean - SD" if i == 0 else ("(mean - SD, mean + SD]" if i == 1 else "> mean + SD")
            print(f"Info({key} ({string}) is %5.3f" % value[i][-1])
        print("-" * 20)
    for key, value in data_info.items():
        print(f"Info {key} (D) is %5.3f" % value)
    print("-" * 20)
    for key, value in data_gain.items():
        print(f"Gain {key} %5.3f" % value)
    for key, value in max_gain.items():
        print(f"max of attributes gain is %5.3f" % value, "position is", {key})
    print("***End result of calculate***\n")
