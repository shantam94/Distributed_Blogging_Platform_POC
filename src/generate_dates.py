import random
from datetime import datetime, timedelta

# Function to generate a random date
def generate_random_date(start_year=1900, end_year=datetime.now().year):
    # Generate a date in the given year range
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date

    # Choose a random number of days to add to the start date
    random_days = random.randrange(delta.days)
    random_date = start_date + timedelta(days=random_days)

    return random_date

# Generate a random date
random_date = generate_random_date()
random_date.strftime("%Y-%m-%d")  # Formatting the date for readability

