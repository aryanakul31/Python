import random

sample = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
passwordLength = 9

password = "".join(random.sample(sample, passwordLength))
print(password)
