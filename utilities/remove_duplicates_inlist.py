from collections import Counter

# removing duplicate elements from the list

l = [1, 2, 4, 2, 1, 4, 5]
print("Original List: ", l)
res = [*set(l)]
print("List after removing duplicate elements: ", res)

# removing duplicated from list
# using list comprehension

# initializing list
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print("The original list is : "
      + str(test_list))

# using list comprehension
# to remove duplicated
# from list
res = []
[res.append(x) for x in test_list if x not in res]

# printing list after removal
print("The list after removing duplicates : "
      + str(res))

# removing duplicated from list
# using set()

# initializing list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print("The original list is : "
      + str(test_list))

# using set()
# to remove duplicated
# from list
test_list = list(set(test_list))

# printing list after removal
# distorted ordering
print("The list after removing duplicates : "
      + str(test_list))

# removing duplicated from list
# using list comprehension + enumerate()

# initializing list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print("The original list is : "
      + str(test_list))

# using list comprehension + enumerate()
# to remove duplicated
# from list
res = [i for n, i in enumerate(test_list) if i not in test_list[:n]]

# printing list after removal
print("The list after removing duplicates : "
      + str(res))

# removing duplicated from list
# using collections.OrderedDict.fromkeys()
from collections import OrderedDict

# initializing list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print("The original list is : "
      + str(test_list))

# using collections.OrderedDict.fromkeys()
# to remove duplicated
# from list
res = list(OrderedDict.fromkeys(test_list))

# printing list after removal
print("The list after removing duplicates : "
      + str(res))

# removing duplicates from list

# initializing list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print("The original list is : " + str(test_list))

res = []
for i in test_list:
    if i not in res:
        res.append(i)

# printing list after removal
print("The list after removing duplicates : " + str(res))

# removing duplicated from list
# using list comprehension and arr.index

# initializing list
arr = [1, 5, 3, 6, 3, 5, 6, 1]
print('The original list is : ' + str(arr))

# using list comprehension + arr.index()
# to remove duplicated
# from list
res = [arr[i] for i in range(len(arr)) if i == arr.index(arr[i])]

# printing list after removal
# of duplicate
print('The list after removing duplicates :'
      , res)

#removing duplicated from list
# using Counter() method

# initializing list
arr = [1, 5, 3, 6, 3, 5, 6, 1]
print('The original list is : ' + str(arr))

# using Counter() + keys()
# to remove duplicated
# from list
temp = Counter(arr)
res = [*temp]

# printing list after removal
# of duplicate
print('The list after removing duplicates :'
      , res)

