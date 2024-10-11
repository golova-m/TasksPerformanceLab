import sys

def app(file1, file2):
    print(file1, file2)


if __name__ == '__main__':
    app(sys.argv[1], sys.argv[2])