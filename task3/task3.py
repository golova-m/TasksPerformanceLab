import sys
import json


def print_el(data):
    value_dic = {}
    for value in data['values']:
        value_dic[value['id']] = value['value']
    return(value_dic)


def iter_test(data, key, value_dic):
    for i in data:
        if key in i:
            if i['id'] in value_dic:
                i['value'] = value_dic[i['id']]          
            iter_test(i[key], key, value_dic)
        else:
            if i['id'] in value_dic:
                i['value'] = value_dic[i['id']]
    return data


def app(file1, file2, file3):
    with open(file1, 'r') as test_str:
        data = json.load(test_str)
    value_dic = print_el(data)

    with open(file2, 'r') as test_str:
        data = json.load(test_str)

    data['tests'] = iter_test(data['tests'], 'values', value_dic)
    

    with open(file3, 'w') as test_str:
        json.dump(data, test_str)
    


if __name__ == '__main__':
    app(sys.argv[1], sys.argv[2], sys.argv[3])