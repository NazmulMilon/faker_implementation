import faker.providers.date_time
import json
from faker import Faker
from random import randint
fake = Faker()

# print(fake.name())
# print(fake.email())
# print(fake.address())

# print(f'Name: {fake.name()}')
l =[]
for _ in range(10):
    # l.append(str(randint(10, 100)))
    # l.append(str(fake.longitude()))
    l.append(f'Name {_+1}: {fake.longitude()}')

print(l)
    # print(fake.name())


# using json declare
with open('simple_faker_prog.json', 'w') as jd:
    json.dump(l, jd)
