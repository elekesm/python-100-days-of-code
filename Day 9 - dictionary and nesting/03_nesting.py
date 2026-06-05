capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Task: print "Little"
print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D", "E"]]
# Task: print "D"
print(nested_list[2][1])

travel_log_dictionary = {
    "France": {
        "cities_visited": ["Paris", "Versailles", "Dijon"],
        "number_of_visits": 1
    },
    "Hungary": {
        "cities_visited": ["Budapest", "Nagykanizsa", "Győr"],
        "number_of_visits": 420
    }
}

# Task: print "Nagykanizsa"
print(travel_log_dictionary["Hungary"]["cities_visited"][1])