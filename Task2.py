import random

def get_numbers_ticket(min_val, max_val, quantity):
    if not (1 <= min_val <= max_val <= 1000):
        return []
    
    unique_numbers = set()
    while len(unique_numbers) < quantity:
        unique_numbers.add(random.randint(min_val, max_val))
    
    return sorted(list(unique_numbers))

# Приклад використання:
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
