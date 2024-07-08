from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d')
        current_date = datetime.today()
        days_difference = (current_date - input_date).days
        
        return days_difference
    except ValueError:
        return "Неправильний формат дати. Будь ласка, введіть дату у форматі 'РРРР-ММ-ДД'."

# Приклад використання
today = datetime.today().strftime('%Y-%m-%d')
input_date = "2022-02-24"
days = get_days_from_today(input_date)
print(f"Сьогодні {today}. Різниця між {input_date} та сьогодні становить {days} днів.")
