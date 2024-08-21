states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", 
                     "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", 
                     "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", 
                     "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", 
                     "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", 
                     "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", 
                     "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", 
                     "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona",
                     "Alaska", "Hawaii"]

state = states_of_america[2]
print(state)

# cambio il nome dello stato in posizione 1
states_of_america[1] = "Italia"

# stampo lo stato in posizione 3
print(states_of_america[3])

# con il "-" parte dalla fine della lista
print(states_of_america[-1])

# aggiungo uno stato alla fine della lista
states_of_america.append("Marche")

# aggiungo più stati alla fine
states_of_america.extend(["Umbria", "Lombardia"])

print(states_of_america)
