from ClassificationRule import classification
from Dt4StuInclass import *
from PreprocessingData import preprocessing_data
from WriteFile import *

if __name__ == '__main__':
    # preprocessing_data()

    # decision_tree("Iris/training_path/all.txt")
    # write_file("Iris/training_path/all.txt",
    #            "Iris/training_path/petal_length/middle.txt", 'petal_length_M')

    # decision_tree("Iris/training_path/petal_length/middle.txt")
    # write_file("Iris/training_path/petal_length/middle.txt",
    #            "Iris/training_path/petal_width/middle.txt", 'petal_width_M')

    # decision_tree("Iris/training_path/petal_width/middle.txt")
    # write_file("Iris/training_path/petal_width/middle.txt",
    #            "Iris/training_path/sepal_length/middle.txt", 'sepal_length_M')
    # write_file("Iris/training_path/petal_width/middle.txt",
    #            "Iris/training_path/sepal_length/left.txt", 'sepal_length_L')

    # decision_tree("Iris/training_path/sepal_length/left.txt")
    # decision_tree("Iris/training_path/sepal_length/middle.txt")

    classification('Iris/training_path/all.txt')
    classification("Iris/testing_data.txt")
