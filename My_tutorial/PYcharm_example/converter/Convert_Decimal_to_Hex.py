
def decimal_to_hex(decimal_str):
    decimal_number = int(decimal_str, 10)
    hex_number = hex(decimal_number)
    return hex_number


path= '2307222016,1700272384'
path.split(',')
print(path.split(','))
decimal_input1 = path.split(',')[0]
decimal_input2 = path.split(',')[1]
hex_output1 = decimal_to_hex(decimal_input1)
hex_output2 = decimal_to_hex(decimal_input2)
print('x={0},'.format(hex_output1),'y={0}'.format(hex_output2))
