#Task1
def find_even_nums(num):
    num2 = []
    for x in range(1,num + 1):
        if x % 2 == 0:
            num2.append(x)
    return num2


print(find_even_nums(8))
print(find_even_nums(4))
print(find_even_nums(2))

def find_even_nums(num): # 2 Yoli
    num2 = [x for x in range(1,num + 1) if x % 2 == 0]
    return num2


print(find_even_nums(8))
print(find_even_nums(4))
print(find_even_nums(2))


def find_even_nums(num): # 3 Yoli
    return list(range(2, num + 1, 2))


print(find_even_nums(8))
print(find_even_nums(4))
print(find_even_nums(2))


#Task2
def next_in_line(zxc, nevermore):
    if zxc == []:
        return "No list has been selected"
    else:
        zxc.append(nevermore)
        return zxc[1:]


print(next_in_line([5, 6, 7, 8, 9], 1))
print(next_in_line([7, 6, 3, 23, 17], 10))
print(next_in_line([1, 10, 20, 42], 6))
print(next_in_line([], 6))



def next_in_line(zxc, nevermore): # 2 Yoli
    if zxc == []:
        return "No list has been selected"
    else:
        zxc.append(nevermore)
        zxc.pop(0)
        return zxc


print(next_in_line([5, 6, 7, 8, 9], 1))
print(next_in_line([7, 6, 3, 23, 17], 10))
print(next_in_line([1, 10, 20, 42], 6))
print(next_in_line([], 6))


def next_in_line(zxc, nevermore): # 3 Yoli
    if zxc == []:
        return "No list has been selected"
    zxc.append(nevermore)
    zxc.pop(0)
    return zxc


print(next_in_line([5, 6, 7, 8, 9], 1))
print(next_in_line([7, 6, 3, 23, 17], 10))
print(next_in_line([1, 10, 20, 42], 6))
print(next_in_line([], 6))




#Task3
def get_budgets(lst):
    total = 0
    for person in lst:
        total += person['budget']
    return total


budgets1 = [
  {"name": "John", "age": 21, "budget": 23000},
  {"name": "Steve", "age": 32, "budget": 40000},
  {"name": "Martin", "age": 16, "budget": 2700}
]

budgets2 = [
  {"name": "John",  "age": 21, "budget": 29000},
  {"name": "Steve",  "age": 32, "budget": 32000},
  {"name": "Martin",  "age": 16, "budget": 1600}
]

print(get_budgets(budgets1))
print(get_budgets(budgets2))



#Task4
def add_indexes(lst):
    index = 0
    lst1 = []
    for i in lst:
        lst1.append(i + index)
        index += 1
    return lst1


print(add_indexes([0, 0, 0, 0, 0]))
print(add_indexes([1, 2, 3, 4, 5]))
print(add_indexes([5, 5, 5, 5, 5]))


#Task5
def clone(lst):
    x = lst[:]
    lst.append(x)
    return lst


print(clone([1,1]))
print(clone([1,2,3]))
print(clone(["x", "y"]))


def clone(lst): # 2 Yoli
    lst.append(lst[:])
    return lst


print(clone([1,1]))
print(clone([1,2,3]))
print(clone(["x", "y"]))


def clone(lst): # 3 Yoli
    return lst + [lst]


print(clone([1,1]))
print(clone([1,2,3]))
print(clone(["x", "y"]))


def clone(lst): # 4 Yoli
    lst.append(list(lst))
    return lst


print(clone([1,1]))
print(clone([1,2,3]))
print(clone(["x", "y"]))



#Task6
def return_only_integer(lst):
    lst1 = []
    for l in lst:
        if type(l) == int:
            lst1.append(l)
    return lst1


print(return_only_integer([9, 2, "space", "car", "lion", 16]))
print(return_only_integer(["hello", 81, "basketball", 123, "fox"]))
print(return_only_integer([10, "121", 56, 20, "car", 3, "lion"]))
print(return_only_integer(["String",  True,  3.3,  1]))



def return_only_integer(lst): # 2 Yoli
    return [l for l in lst if type(l) == int]


print(return_only_integer([9, 2, "space", "car", "lion", 16]))
print(return_only_integer(["hello", 81, "basketball", 123, "fox"]))
print(return_only_integer([10, "121", 56, 20, "car", 3, "lion"]))
print(return_only_integer(["String",  True,  3.3,  1]))



#Task7
def list_operation(x, y, n):
    result = []
    for i in range(x, y + 1):
        if i % n == 0:
            result.append(i)
    return result


print(list_operation(1, 10, 3)) # ---> [3, 6, 9]
print(list_operation(7, 9, 2)) # ---> [8]
print(list_operation(15, 20, 7)) # ---> []

def list_operation(x, y, n): # 2 Yoli
    return [i for i in range(x, y+1) if i % n == 0]


print(list_operation(1, 10, 3)) # ---> [3, 6, 9]
print(list_operation(7, 9, 2)) # ---> [8]
print(list_operation(15, 20, 7)) # ---> []


#Task8
def society_name(friends):
    lst = []
    for zxc in friends:
        lst += zxc[0]
    return "".join(sorted(lst))


print(society_name(["Adam", "Sarah", "Malcolm"])) # ---> "AMS"
print(society_name(["Harry", "Newt", "Luna", "Cho"])) # ---> "CHLN"
print(society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"])) # ---> "CJMPRR"


def society_name(friends): # 2 Yoli
    return "".join(sorted(zxc[0] for zxc in friends))


print(society_name(["Adam", "Sarah", "Malcolm"])) # ---> "AMS"
print(society_name(["Harry", "Newt", "Luna", "Cho"])) # ---> "CHLN"
print(society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"])) # ---> "CJMPRR"


#Task9
def unique_sort(lst):
    return sorted(set(lst))


print(unique_sort([1, 2, 4, 3]))  # ---> [1, 2, 3, 4]
print(unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]))  # ---> [1, 2, 3, 4]
print(unique_sort([6, 7, 3, 2, 1]))  # ---> [1, 2, 3, 6, 7]


#Task10
def setify(lst):
    return list(set(lst))


print(setify([1, 3, 3, 5, 5])) # ---> [1, 3, 5]
print(setify([4, 4, 4, 4])) # ---> [4]
print(setify([5, 7, 8, 9, 10, 15])) # ---> [5, 7, 8, 9, 10, 15]
print(setify([3, 3, 3, 2, 1])) # ---< [1, 2, 3]


#Task11
def get_student_names(students):
    return sorted(students.values())


print(get_student_names({
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}))  # ---> ["Becky", "John", "Steve"]



#Task12
def greet_people(names):
    return ", ".join([f"Hello{name}" for name in names])


print(greet_people(["Joe"])) # ---> "Hello Joe"
print(greet_people(["Angela", "Joe"])) # ---> "Hello Angela, Hello Joe"
print(greet_people(["Frank", "Angela", "Joe"])) # ---> "Hello Frank, Hello Angela, Hello Joe"




def greet_people(names): #2 Toli
    str = " "
    for name in names:
        str += f"Hello{name}, "
    return str[:-2]


print(greet_people(["Joe"])) # ---> "Hello Joe"
print(greet_people(["Angela", "Joe"])) # ---> "Hello Angela, Hello Joe"
print(greet_people(["Frank", "Angela", "Joe"])) # ---> "Hello Frank, Hello Angela, Hello Joe"


#Task13
def total_volume(*boxes):
    t = 0
    for b in boxes:
        v = 1
        for s in b:
            v *= s
        t += v
    return t


print(total_volume([4, 2, 4], [3, 3, 3], [1, 1, 2], [2, 1, 1])) # ---> 63
print(total_volume([2, 2, 2], [2, 1, 1])) # ---> 10
print(total_volume([1, 1, 1])) # ---> 1



#Task14
def integer_boolean(a):
    lst_bool = []
    for x in a:
        lst_bool.append(bool(int(x)))
    return lst_bool


print(integer_boolean("100101")) # ---> [True, False, False, True, False, True]
print(integer_boolean("10")) # ---> [True, False]
print(integer_boolean("001")) # ---> [False, False, True]



#Task15
def is_subset(lst1, lst2):
    return set(lst1) <= set(lst2)


print(is_subset([3, 2, 5], [5, 3, 7, 9, 2]))  # ---> True
print(is_subset([8, 9], [7, 1, 9, 8, 4, 5, 6]))  # ---> True
print(is_subset([1, 2], [3, 5, 9, 1]))  # ---> False