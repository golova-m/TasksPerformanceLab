import sys
import math


def creating_list_rational_coordinates(input_str):
    list_rational_coordinates = []
    for i in input_str:
        list_rational_coordinates.append(list(map(float, i.replace('\n', '').split(' '))))
    return list_rational_coordinates


def app(file1, file2):
    with open(file1) as f1, open(file2) as f2:
        circle = creating_list_rational_coordinates(f1.readlines())
        points = creating_list_rational_coordinates(f2.readlines())  

    for point in points:
        hypotenuse = math.sqrt((point[0] - circle[0][0]) ** 2 + (point[1] - circle[0][1]) ** 2)
        if hypotenuse == circle[1][0]:
            print(0)
        elif(hypotenuse < circle[1][0]):
            print(1)
        else:
            print(2)


if __name__ == '__main__':
    app(sys.argv[1], sys.argv[2])