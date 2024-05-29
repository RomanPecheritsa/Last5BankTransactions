from coursework3.funcs import (json_to_list, correct_data,
                               five_operations,
                               dt_to_str, masked,
                               transfer_amount_currency)


def get_formated_info(op):
    date = dt_to_str(op.get('date'))
    desc = op.get('description')
    source_from = masked(op.get('from'))
    source_to = masked(op.get('to'))
    amount_currency = transfer_amount_currency(op)
    return f'{date} {desc}\n{source_from} -> {source_to}\n{amount_currency}\n'


def main():
    data = json_to_list()
    correct = correct_data(data)
    operations = five_operations(correct)
    for op in operations:
        print(get_formated_info(op))


if __name__ == '__main__':
    main()
