
import random

random_number = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_number}")

my_lst = list(range(1, 20))
print(f"Original list: {my_lst}")

random.shuffle(my_lst)
print(f"Shuffled list: {my_lst}")

random_choice = random.choice(my_lst)
print(f"Random choice from the list: {random_choice}")

# sample with replacement
# some number duplicated 
sample_with_replacement = random.choices(my_lst, k=15)
print(f"Sample with replacement (15 elements): {sample_with_replacement}")

#samepl without replacement
sample_without_replacement = random.sample(my_lst, k=12)
print(f"Sample without replacement (12 elements): {sample_without_replacement}")


# can be a floating point number
print(f"Random float between 0 and 1: {random.uniform(a=0, b=1)}")


# normal distribution
print(f"Random number from normal distribution (mu=0, sigma=1): {random.gauss(mu=0, sigma=1)}")