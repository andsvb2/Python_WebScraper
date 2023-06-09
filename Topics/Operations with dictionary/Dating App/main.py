def select_dates(potential_dates, age: int = 30, hobby: str = 'art', city: str = 'Berlin'):
    match_dates = [person['name'] for person in potential_dates if
                   person['age'] > age and hobby in person['hobbies'] and person['city'] == city]
    return ", ".join(match_dates)
