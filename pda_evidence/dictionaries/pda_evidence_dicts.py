tv_shows = {
    "Friends": {
        "genre": "sitcom",
        "number_of_series": 10,
        "main_characters": {
            "Rachel": "Jennifer Aniston",
            "Monica": "Courtney Cox",
            "Pheobe": "Lisa Kudrow",
            "Joey": "Matt LeBlanc",
            "Chandler": "Matthew Perry",
            "Ross": "David Schwimmer"
        }
    },
    "After Life": {
        "genre": "comedy drama",
        "number_of_series": 3,
        "main_characters": {
            "Tony": "Ricky Gervais",
            "Lisa": "Kerry Godliman",
            "Emma": "Ashley Jensen",
            "Kath": "Diane Morgan",
            "Lenny": "Tony Way",
            "Tom": "Matt"
        }
    },
    "Killing Eve": {
        "genre": "drama",
        "number_of_series": 4,
        "main_characters": {
            "Villanelle": "Jodie Comer",
            "Eve": "Sandra Oh",
            "Carolyn": "Fiona Shaw",
            "Konstantin": "Kim Bodnia"
        }    
    }
}

def get_principal_cast_list(input_show):        
    actors = []
    main_characters = tv_shows[input_show]["main_characters"]
    for character in main_characters:
        actors.append(main_characters[character])
    return actors

print(get_principal_cast_list("After Life"))