md_sepal_length = [5.84 - 0.83, 5.84 + 0.83]
md_sepal_width = [3.05 - 0.43, 3.05 + 0.43]
md_petal_length = [3.76 - 1.76, 3.76 + 1.76]
md_petal_width = [1.20 - 0.76, 1.20 + 0.76]


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
