from faker import Faker
import json

fake = Faker('bn_BD')

# for _ in range(10):
#     # print(fake.name())
profile_data = {}
for _ in range(10):
    print(fake.profiles())

