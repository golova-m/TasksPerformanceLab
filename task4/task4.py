import sys


def app(file):
    with open(file, 'r') as file_nums:
        nums_str = file_nums.readlines()
    nums = [int(i.replace('\n', '')) for i in nums_str]
    median = sorted(nums)[len(nums) // 2]
    print(sum(abs(elem - median) for elem in nums))


if __name__ == '__main__':
    app(sys.argv[1])