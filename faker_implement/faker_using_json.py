"""

Application 1 : Create a json of 100 students with name students.json
that contains student name, address, location coordinates and student roll number.
source::: https://www.geeksforgeeks.org/python-faker-library/
"""
from faker import Faker
from random import randint
import json

fake = Faker()

student_dict = {}
def input_data(n):
    for i in range(0,n):
        student_dict[i] = {}
        student_dict[i]['id'] = randint(1, 100)
        student_dict[i]['name'] = fake.name()
        student_dict[i]['address'] = fake.address()
        student_dict[i]['latitude'] = str(fake.latitude())
        student_dict[i]['longitude'] = str(fake.longitude())
    print(student_dict)

    # print using json file
    with open('st_json', 'w') as fp:
        json.dump(student_dict, fp)


def main():
    num_of_st = int(input("Enter student number: "))
    input_data(num_of_st)

main()
# from faker import Faker
#
# # to create a json file
# import json
#
# # for student id
# from random import randint
#
# fake = Faker()
#
#
# def input_date(x):
#     student_data = {}
#     for i in range(0, x):
#         student_data[i] = {}
#         student_data[i]['id'] = randint(1, 100)
#         student_data[i]['name'] = fake.name()
#         student_data[i]['address'] = fake.address()
#         student_data[i]['latitude'] = str(fake.latitude())
#         student_data[i]['longitude'] = str(fake.longitude())
#     print(student_data)
#
#     # dictionary dumped as json in a json file
#     with open('students.json', 'w') as fp:
#         json.dump(student_data, fp)
#
#
# def main():
#     number_of_students = 10
#     input_date(number_of_students)
#
#
# main()
