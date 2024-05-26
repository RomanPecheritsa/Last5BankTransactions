from funcs import json_to_list, correct_data, five_operations


def main():
    data = json_to_list()
    correct = correct_data(data)
    operations = five_operations(correct)


if __name__ == '__main__':
    main()