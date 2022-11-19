no_of_stu_per_group=24
no_of_total_students=int(input("Enter number of students: "))
no_of_group=no_of_total_students//no_of_stu_per_group
no_of_left_out=no_of_total_students-(no_of_group*24)
print("No of Groups with 24 Students each: ", no_of_group)
print("No of Left Out Students: ", no_of_left_out)
