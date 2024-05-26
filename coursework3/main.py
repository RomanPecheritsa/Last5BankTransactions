from funcs import json_to_list, correct_data


def main():
    data = json_to_list()
    correct = correct_data(data)

if __name__ == '__main__':
    main()