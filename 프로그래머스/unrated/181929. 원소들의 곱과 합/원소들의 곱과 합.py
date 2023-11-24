from math import prod

def solution(num_list):

    times_nums = prod(num_list)

    
    two_times_nums = sum(num_list) ** 2


    
    return 1 if times_nums < two_times_nums else 0