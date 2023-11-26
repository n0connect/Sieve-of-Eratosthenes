from eratosthenes_algoritm import Prime


user_number = int(input("Enter the number: "))
user_number_list = list(range(3, user_number + 1, 2))
print("Sending...")
Prime(user_number_list)
