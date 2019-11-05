import json


def create_json_file(file_name, token):
    with open(file_name, 'w') as file:
        data = {'token': token}
        json.dump(data, file)


def load_json_file(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data


if __name__ == '__main__':
    # create_json_file('token.json', 'place your token here')
    print(load_json_file('token.json'))