def write_file(read, write, choice):
    f1 = open(read, "r")
    f2 = open(write, "w")

    x = f1.readlines()
    c = 0

    for i in range(len(x)):
        data = x[i].split(",")
        if i == 0:
            data_type = choice[:-2]
            for j in range(len(data)):
                name = data[j][:-2]
                if name == data_type:
                    c = j
                    break

        if data[c] == choice:
            del data[c]
            result = ",".join(data[:c] + data[c:])
            f2.write(result)
