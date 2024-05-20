# #Task1
# def find_even_nums(num):
#     num2 = []
#     for x in range(1,num + 1):
#         if x % 2 == 0:
#             num2.append(x)
#     return num2
# 
# 
# print(find_even_nums(8))
# print(find_even_nums(4))
# print(find_even_nums(2))
# 
# def find_even_nums(num): # 2 Yoli
#     num2 = [x for x in range(1,num + 1) if x % 2 == 0]
#     return num2
# 
# 
# print(find_even_nums(8))
# print(find_even_nums(4))
# print(find_even_nums(2))
# 
# 
# def find_even_nums(num): # 3 Yoli
#     return list(range(2, num + 1, 2))
# 
# 
# print(find_even_nums(8))
# print(find_even_nums(4))
# print(find_even_nums(2))
# 
# 
# #Task2
# def next_in_line(zxc, nevermore):
#     if zxc == []:
#         return "No list has been selected"
#     else:
#         zxc.append(nevermore)
#         return zxc[1:]
# 
# 
# print(next_in_line([5, 6, 7, 8, 9], 1))
# print(next_in_line([7, 6, 3, 23, 17], 10))
# print(next_in_line([1, 10, 20, 42], 6))
# print(next_in_line([], 6))
# 
# 
# 
# def next_in_line(zxc, nevermore): # 2 Yoli
#     if zxc == []:
#         return "No list has been selected"
#     else:
#         zxc.append(nevermore)
#         zxc.pop(0)
#         return zxc
# 
# 
# print(next_in_line([5, 6, 7, 8, 9], 1))
# print(next_in_line([7, 6, 3, 23, 17], 10))
# print(next_in_line([1, 10, 20, 42], 6))
# print(next_in_line([], 6))
# 
# 
# def next_in_line(zxc, nevermore): # 3 Yoli
#     if zxc == []:
#         return "No list has been selected"
#     zxc.append(nevermore)
#     zxc.pop(0)
#     return zxc
# 
# 
# print(next_in_line([5, 6, 7, 8, 9], 1))
# print(next_in_line([7, 6, 3, 23, 17], 10))
# print(next_in_line([1, 10, 20, 42], 6))
# print(next_in_line([], 6))
# 
# 
# 
# 
# #Task3
# def get_budgets(lst):
#     total = 0
#     for person in lst:
#         total += person['budget']
#     return total
# 
# 
# budgets1 = [
#   {"name": "John", "age": 21, "budget": 23000},
#   {"name": "Steve", "age": 32, "budget": 40000},
#   {"name": "Martin", "age": 16, "budget": 2700}
# ]
# 
# budgets2 = [
#   {"name": "John",  "age": 21, "budget": 29000},
#   {"name": "Steve",  "age": 32, "budget": 32000},
#   {"name": "Martin",  "age": 16, "budget": 1600}
# ]
# 
# print(get_budgets(budgets1))
# print(get_budgets(budgets2))
# 
# 

#Task4
def add_indexes(lst):
    index = 0
    lst1 = []
    for i in lst:
        lst.append(i + index)
        index += 1
    return lst1


print(add_indexes([0, 0, 0, 0, 0]))
print(add_indexes([1, 2, 3, 4, 5]))
print(add_indexes([5, 5, 5, 5, 5]))


# #Task5
# def clone(lst):
#     x = lst[:]
#     lst.append(x)
#     return lst
#
#
# print(clone([1,1]))
# print(clone([1,2,3]))
# print(clone(["x", "y"]))
#
#
# def clone(lst): # 2 Yoli
#     lst.append(lst[:])
#     return lst
#
#
# print(clone([1,1]))
# print(clone([1,2,3]))
# print(clone(["x", "y"]))
#
#
# def clone(lst): # 3 Yoli
#     return lst + [lst]
#
#
# print(clone([1,1]))
# print(clone([1,2,3]))
# print(clone(["x", "y"]))
#
#
# def clone(lst): # 4 Yoli
#     lst.append(list(lst))
#     return lst
#
#
# print(clone([1,1]))
# print(clone([1,2,3]))
# print(clone(["x", "y"]))
#
#
#
# #Task6
# def return_only_integer(lst):
#     lst1 = []
#     for l in lst:
#         if type(l) == int:
#             lst1.append(l)
#     return lst1
#

# print(return_only_integer([9, 2, "space", "car", "lion", 16]))
# print(return_only_integer(["hello", 81, "basketball", 123, "fox"]))
# print(return_only_integer([10, "121", 56, 20, "car", 3, "lion"]))
# print(return_only_integer(["String",  True,  3.3,  1]))
#
#
#
# def return_only_integer(lst): # 2 Yoli
#     return [l for l in lst if type(l) == int]
#
#
# print(return_only_integer([9, 2, "space", "car", "lion", 16]))
# print(return_only_integer(["hello", 81, "basketball", 123, "fox"]))
# print(return_only_integer([10, "121", 56, 20, "car", 3, "lion"]))
# print(return_only_integer(["String",  True,  3.3,  1]))



#Task7

