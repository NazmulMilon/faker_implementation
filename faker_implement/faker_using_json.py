"""

Application 1 : Create a json of 100 students with name students.json
that contains student name, address, location coordinates and student roll number.
source::: https://www.geeksforgeeks.org/python-faker-library/
"""

from faker import Faker

# to create a json file
import json

# for student id
from random import randint

fake = Faker()


def input_date(x):
    student_data = {}
    for i in range(0,x):
        student_data[i]={}
        student_data[i]['id']=randint(1,100)
        student_data[i]['name']=fake.name()
        student_data[i]['address'] = fake.address()
        student_data[i]['latitude'] = str(fake.latitude())
        student_data[i]['longitude'] = str(fake.longitude())
    print(student_data)

    # dictionary dumped as json in a json file
    with open('students.json', 'w') as fp:
        json.dump(student_data, fp)

def main():
    number_of_students = 10
    input_date(number_of_students)

main()