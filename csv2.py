"""
-----------------------------
| Python CSV-to-DICT Module |
-----------------------------
A custom python module for converting
any csv file into python dictionary
"""


def csv_to_dict(file):
    """
    _____________
    main function
    _____________

    This function converts csv to dictionary(python)
    """
    csv = open(file)
    headers = get_head(csv.readline())
    dict = {}

    for num, head in enumerate(headers):
        dict[head] = []

    temp = 0
    for data in csv:
        data = normalized_csv(data)
        length = len(data)

        if temp > length - 1:
            temp = 0

        dict[headers[temp]].append(data[temp])
        temp += 1
    return dict


def get_head(row):
    """
    _______________
    helper function
    _______________
    returns a list with the attributes of the csv i.e. the first
    line of csv file.
    """
    import re
    return re.findall('\w+', row)


def normalized_csv(word):
    """
    _______________
    helper function
    _______________
    returns a list representing a row of csv file
    with padding removed.
    """
    temp = clean_csv(word)
    return temp.split('##############')


def clean_csv(word):
    """
    _______________
    helper function
    _______________
    returns a string with newlines removed,
    quotation marks preserved and padding
    added to a row of csv file.
    """
    import re
    quote = False
    new_word = []
    index = word.find("\n")
    word = word[:index]

    for i in word:
        if i == '"':
            if not quote:
                quote = True
            else:
                quote = False
        elif i == ',' and not quote:
            new_word.append('##############')
        else:
            new_word.append(i)
    return ''.join(new_word)
