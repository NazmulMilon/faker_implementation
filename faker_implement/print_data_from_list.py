"""
    Generating a sentence that contains the words we provided.
    https://www.geeksforgeeks.org/python-faker-library/
"""

from faker import Faker
fake = Faker()

# print random sentence
print(fake.sentence())

# list has words that we want in our sentence
word_list = ["FAKER", "PRACTICE", "IUBAT", "BANGLADESH", "iQuantile"]

for i in range(0,5):
    print(fake.sentence(ext_word_list=word_list))
