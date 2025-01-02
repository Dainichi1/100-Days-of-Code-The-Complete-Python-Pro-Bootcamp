def life_in_weeks(age):
    age = age * 52
    total = 90 * 52
    left = total - age
    print (f"You have {left} weeks left.")

life_in_weeks(56)