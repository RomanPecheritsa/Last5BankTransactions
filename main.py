from coursework3.funcs import (json_to_list, correct_data,
                               five_operations,
                               dt_to_str, masked,
                               transfer_amount_currency)


def main():
    data = json_to_list()
    correct = correct_data(data)
    operations = five_operations(correct)
    for op in operations:
        date = dt_to_str(op.get('date'))
        source_from = masked(op.get('from'))
        source_to = masked(op.get('to'))
        amount_currency = transfer_amount_currency(op)


if __name__ == '__main__':
    main()