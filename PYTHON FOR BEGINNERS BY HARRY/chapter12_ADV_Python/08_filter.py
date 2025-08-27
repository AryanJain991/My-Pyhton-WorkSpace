"""let's See How Filter works"""

# def which_is_greater_than_9(x):
#     if x > 9:
#         return True
#     else:
#         return False
    
# filter_with_these_number_list = [1, 8, 5, 45, 98, 259, 4, 54, 1000, 999, 9, 75, 1, 3]

# filterd_list = list(filter(which_is_greater_than_9, filter_with_these_number_list))

# print("Filterd numbers of list is: ", filterd_list)

"""Lambda uses with filter == it helps to reduce the no of lined in our program"""

filter_with_these_number_list = [1, 8, 5, 45, 98, 259, 4, 54, 1000, 999, 9, 75, 1, 3]

filterd_list = list(filter(lambda x: x>9 , filter_with_these_number_list))

print("Filterd numbers of list is: ", filterd_list)