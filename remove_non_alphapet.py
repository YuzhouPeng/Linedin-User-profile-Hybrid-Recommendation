import re,itertools,collections

def remove_non_alpha(stringlist):
    new_string_list = []
    for i in range(len(stringlist)):
        non_digital_string = ''.join([i for i in stringlist[i] if not i.isdigit()])
        new_word = re.sub(r'\s*[^A-Za-z]+\s*', ' ', non_digital_string)
        new_string_list.append(' '+new_word)

    return new_string_list