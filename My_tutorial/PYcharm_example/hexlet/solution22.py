def binary(number):
    if not number:
        return '0'
    result = ''
    newnumber = number
    while newnumber:
        modul = newnumber % 2
        result = str(modul) + result
        newnumber = newnumber // 2
    return result


assert binary(0) == '0'
assert binary(1) == '1'
assert binary(5) == '101'
