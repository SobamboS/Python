# def add(first_number: int, second_number: int) -> int:
#     """
#     :param first_number:
#     :param second_number:
#     :return:
#     """
#     return first_number + second_number
#
# print(add(2, 3))
# print(add('2', '3'))
# print(add.__doc__)
# print(add.__name__)
# print(add.__annotations__)
# help(add)

def get_digit(number, position):
    '''return  digit at  position in number, counting from right'''
    return number//(10**position)%10

print(get_digit(12342456, 5))

def get_length(number: int) -> int:
    import math
    math.log10(number)
    return math.ceil(math.log10(number))
print(get_length(456))

    # return get_length//(5**position)%5