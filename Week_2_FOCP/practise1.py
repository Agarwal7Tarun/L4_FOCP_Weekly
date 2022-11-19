len_of_list=int(input("Enter the length of list between 1 and 10: "))
lst=['a','b','c','d','e','f','g','h','i','j']
new_lst=[]
new_lst.extend(lst[:len_of_list])
print(new_lst)
