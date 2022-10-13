from faker import Faker

fake = Faker('en_US')

# for _ in range(10):
#    print(fake.name())


# using multiple locales

mul_locale = Faker(['en_US', 'it_IT', 'ja_JP', 'bn_BD', 'hi_IN'])
for _ in range(20):
    print(mul_locale.name())
