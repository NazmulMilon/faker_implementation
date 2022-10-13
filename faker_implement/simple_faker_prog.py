import faker.providers.date_time
from faker import Faker
fake = Faker()

# print(fake.name())
# print(fake.email())
# print(fake.address())

for _ in range(10):
    print(fake.name())