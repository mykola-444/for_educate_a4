def hex_to_decimal(hex_str):
    decimal_number = int(hex_str, 16)
    return decimal_number


path = 'x=0xc9d519dd, y=0x40f42ad2'

path.split(',')
#print(path.split(','))
#hex_input1 = (path.split(',')[0])[4:]
#print(hex_input1)
#hex_input2 = (path.split(',')[1])[5:]
#print(hex_input2)
decimal_output1 = hex_to_decimal((path.split(',')[0])[4:])
decimal_output2 = hex_to_decimal((path.split(',')[1])[5:])
print('{0},'.format(decimal_output1),'{0}'.format(decimal_output2))