import sys
import json


def creating_dict_values(data):
    value_dict = {}
    for value in data['values']:
        value_dict[value['id']] = value['value']
    return(value_dict)


def iter_test(data, key, value_dict):
    for i in data:
        if key in i:
            if i['id'] in value_dict:
                i['value'] = value_dict[i['id']]          
            iter_test(i[key], key, value_dict)
        else:
            if i['id'] in value_dict:
                i['value'] = value_dict[i['id']]
    return data


def app(file1, file2, file3):
    with open(file1, 'r') as file1, open(file2, 'r') as file2:
        data_value_json = json.load(file1)
        data_tests_json = json.load(file2)
    value_dict = creating_dict_values(data_value_json)
    data_tests_json['tests'] = iter_test(data_tests_json['tests'], 'values', value_dict)
    
    with open(file3, 'w') as file:
        json.dump(data_tests_json, file)
    


if __name__ == '__main__':
    app(sys.argv[1], sys.argv[2], sys.argv[3])