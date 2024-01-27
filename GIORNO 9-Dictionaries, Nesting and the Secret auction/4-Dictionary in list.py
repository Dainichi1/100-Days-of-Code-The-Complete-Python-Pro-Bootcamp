country = input("Enter country name: ") # Add country name
visits = int(input("Enter number of visit: ")) # Number of visits
list_of_cities = eval(input('"Enter list of cities this way "name of the city,": ''')) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]


# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country (country, visits, list_of_cities) :
  new_travel_log = {"country":country,"visits":visits,"cities":list_of_cities}
  travel_log.append(new_travel_log)


add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")