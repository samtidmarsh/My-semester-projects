import random

# Same lists as before
fruitList=["Apple", "Banana", "Orange", "Mango", "Grapes", "Pineapple", "Strawberry", "Blueberry", "Watermelon", "Kiwi", "Peach", "Pear", "Plum", "Apricot", "Cherries", "Raspberry", "Blackberries", "Pomegranate", "Papaya", "Guava", "Lychee", "Dragonfruit", "Fig", "Date", "Coconut", "Lemon", "Lime", "Tangerine", "Cantaloupe", "Persimmon"]
CityNames=["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "Fort Worth", "Columbus", "Indianapolis", "Charlotte", "Seattle", "Denver", "Washington D.C.", "Boston", "El Paso", "Nashville", "Detroit", "Oklahoma City", "Portland", "Las Vegas", "Memphis", "Louisville", "Baltimore", "Milwaukee", "Albuquerque", "Tucson"]
endIng=["singing", "dancing", "running", "jumping", "reading", "writing", "cooking", "baking", "painting", "drawing", "flying", "swimming", "driving", "working", "studying", "sleeping", "thinking", "talking", "listening", "playing", "eating", "watching", "laughing", "crying", "waiting", "helping", "traveling", "climbing", "shopping", "building", "cleaning"]
homoPhones=["air", "heir", "bare", "bear", "be", "bee", "blue", "blew", "brake", "break", "cell", "sell", "cent", "scent", "flour", "flower", "forth", "fourth", "heal", "heel", "knight", "night", "made", "maid", "meat", "meet", "pair", "pear", "peace", "piece", "right", "rite"]
doubleLetters=["bookkeeper", "coffee", "butter", "balloon", "address", "success", "committee", "grass", "yellow", "letter", "bitter", "apple", "fluffy", "happening", "embellish", "swallow", "offer", "muffin", "dinner", "bedding", "tissue", "gutter", "pudding", "cabbage", "puppy", "bubble", "ribbon", "hollow", "jelly", "kettle"]
SilentLetters=["knight", "thumb", "write", "castle", "debt", "honest", "island", "guitar", "comb", "pterodactylus", "knee", "psychic", "receipt", "subtle", "wrist", "doubt", "gnome", "plumber", "answer", "foreign", "autumn", "vehicle", "align", "hour", "yacht", "furniture", "knock", "psychology", "wrought", "lamb"]
codingTerms=["algorithm", "variable", "function", "loop", "array", "object", "class", "inheritance", "method", "parameter", "boolean", "syntax", "compile", "debug", "framework", "API", "repository", "version", "server", "client", "database", "query", "exception", "event", "deployment", "frontend", "backend", "module", "namespace", "Git", "cache"]
animalNoises=["moo", "bark", "meow", "roar", "neigh", "oink", "quack", "bleat", "hiss", "growl", "chirp", "howl", "cluck", "ribbit", "buzz", "caw", "whistle", "trumpet", "squeal", "croak", "bray", "peep", "chatter", "whinny", "grunt", "purr", "yelp", "snort", "honk", "squawk"]
treeSpecies=["oak", "pine", "maple", "birch", "willow", "cedar", "spruce", "fir", "cherry", "apple", "peach", "plum", "almond", "coconut", "redwood", "sequoia", "magnolia", "ash", "elm", "chestnut", "beech", "cypress", "sycamore", "eucalyptus", "jacaranda", "palm", "hickory", "apricot", "juniper", "holly", "poplar"]
saltWater=["shark", "whale", "octopus", "dolphin", "seal", "sea turtle", "jellyfish", "clownfish", "starfish", "squid", "lobster", "crab", "sea urchin", "manatee", "stingray", "manta ray", "tuna", "salmon", "cod", "barracuda", "angelfish", "moray eel", "blue whale", "ray", "coral", "flounder", "trout", "albatross", "pelican", "sea lion", "sea snake"]
freshWater=["bass", "catfish", "trout", "salmon", "pike", "carp", "goldfish", "guppy", "betta", "tilapia", "perch", "muskellunge", "cichlid", "freshwater eel", "sturgeon", "crayfish", "frog", "newt", "turtle", "snapping turtle", "damselfly", "dragonfly", "water snake", "clams", "swan", "beaver", "otter", "minnow", "darter", "shad", "water buffalo"]
Reptiles=["snake", "lizard", "turtle", "crocodile", "alligator", "gecko", "chameleon", "iguana", "komodo dragon", "python", "viper", "cobra", "rattlesnake", "anaconda", "box turtle", "bearded dragon", "skink", "monitor lizard", "gila monster", "king cobra", "tarantula", "horned lizard", "frilled lizard", "leopard gecko", "tortoise", "water dragon", "green iguana", "diamondback rattlesnake", "ball python", "sand boa", "flying dragon"]
emptySalad=["caesar", "potato", "pasta", "fruit", "green", "chicken", "tuna", "coleslaw", "Greek", "egg", "avocado", "tomato", "bean", "quinoa", "rice", "cucumber", "waldorf", "spinach", "carrot", "cabbage", "beet", "chickpea", "kale", "coleslaw", "broccoli", "seafood", "sweet potato", "roasted vegetable", "caprese", "summer"]
fakeWords=["flibberflop", "bamboozle", "blorptastic", "zibber", "snorfle", "gribblesnack", "wobbleton", "splorf", "quixle", "glonker", "plumbuzzle", "jibberwocky", "froob", "twizzle", "zorp", "flumple", "snagglenorf", "wobblewomp", "squizzle", "plipplop", "blopple", "jinglewump", "fribber", "smushen", "glorp", "flitterfuzz", "nibblesnack", "swozzle", "glimmerfuzz", "twiddleflick", "slomp"]
nickShow=["bob", "sponge", "dora", "dragon", "rugrats", "wild", "krabs", "fairy", "odd", "parents", "victorious", "icarly", "jimmy", "neutron", "all", "that", "good", "burger", "hey", "arnold", "blue", "clues", "loud", "house", "rocket", "power", "puff", "friends", "ninja", "turtles"]
carBrands=["udi", "ercedes", "hevy", "errari", "oyota", "MW", "onda", "orshe", "olvo", "ubaru", "issan", "azda", "esla", "ia", "cura", "yundai", "hrysler", "exus", "aguar", "eugeot", "uick", "nfinity", "itsubishi", "ord", "ange Rover", "MC", "enault", "pel", "iat", "and Rover"]
musicGroups=["The Beatles", "The Rolling Stones", "The Supremes", "The Beach Boys", "The Who", "The Temptations", "The Four Seasons", "The Doors", "The Byrds", "The Kinks", "The Monkees", "The Zombies", "The Velvet Underground", "The Hollies", "The Mamas and the Papas", "The Dave Clark Five", "The Righteous Brothers", "The Animals", "The Turtles", "The Shirelles", "The Spencer Davis Group", "The Seekers", "The Rascals", "The Everly Brothers", "The Platters", "The Chantels", "The Drifters", "The Coasters", "The Impressions", "The Crystals"]
sodaBrands=["Pepsi", "Coca-Cola", "Sprite", "Fanta", "7Up", "Mountain Dew", "Dr. Pepper", "Sierra Mist", "A&W", "Schweppes", "Crush", "Root Beer", "Canada Dry", "Barq's", "Squirt", "Big Red", "Diet Coke", "Mirinda", "Orange Crush", "Irn-Bru", "Mug Root Beer", "Mello Yello", "Pibb Xtra", "Sunkist", "RC Cola", "Cherry Coke", "Tango", "Squirt", "Club Soda", "Yoo-hoo"]
breakFood=["pancakes", "waffles", "eggs", "bacon", "sausage", "oatmeal", "cereal", "toast", "bagel", "muffin", "croissant", "yogurt", "fruit salad", "granola", "smoothie", "poptart", "hashbrowns", "grits", "avocado toast", "smoothie bowl", "scrambled eggs", "fried eggs", "burrito", "english muffin", "quiche", "French toast", "breakfast burrito", "banana bread", "scone", "pancake sandwich"]
Veggies=["carrot", "broccoli", "spinach", "lettuce", "tomato", "cucumber", "zucchini", "kale", "pepper", "onion", "garlic", "cauliflower", "sweet potato", "asparagus", "peas", "mushroom", "eggplant", "beet", "celery", "radish", "brussels sprout", "artichoke", "corn", "squash", "pumpkin", "green beans", "leek", "chard", "okra", "parsnip", "turnip"]
listList=[fruitList, CityNames, endIng, homoPhones, doubleLetters, SilentLetters, codingTerms, animalNoises, treeSpecies, saltWater, freshWater, Reptiles, emptySalad, fakeWords, nickShow, carBrands, musicGroups, sodaBrands, breakFood, Veggies]



def plswork(money):
    global listList
    randomList = []

    # Select 4 random categories
    selected_categories = random.sample(listList, 4)  # Select 4 categories at random
    randomWordList1 = random.sample(selected_categories[0], 4)  # Sample 4 words from the first category
    randomWordList2 = random.sample(selected_categories[1], 4)  # Sample 4 words from the second category
    randomWordList3 = random.sample(selected_categories[2], 4)  # Sample 4 words from the third category
    randomWordList4 = random.sample(selected_categories[3], 4)  # Sample 4 words from the fourth category

    # Shuffle the lists of words to make their order random
    random_word_order = random.sample([randomWordList1, randomWordList2, randomWordList3, randomWordList4], 4)

    print("Welcome to the APCSP Connections game!")
    print("You are going to be choosing four words that go into one category!")

    name = input("What is your name? ")
    print(f"Watch out {name}, every time you get one wrong, you lose! You start with ${money}")

    # Print one random word per list
    print("FIRST LIST HERE: " + str(random_word_order[0]))
    print("SECOND LIST HERE: " + str(random_word_order[1]))
    print("THIRD LIST HERE: " + str(random_word_order[2]))
    print("LAST LIST HERE: " + str(random_word_order[3]))

    # Loop for guesses
    while True:
        # Get guesses from the user
        firstGuess = str(input("Please enter your first word: "))
        secondGuess = str(input("Please enter your second word: "))
        thirdGuess = str(input("Please enter your third word: "))
        fourthGuess = str(input("Please enter your fourth word: "))

        # Check if the guesses match one of the categories
        if all(word in random_word_order[0] for word in [firstGuess, secondGuess, thirdGuess, fourthGuess]):
            print("That is correct!")
            money += 100
            print(f"You have won $100! You now have: ${money}")
            break
        elif all(word in random_word_order[1] for word in [firstGuess, secondGuess, thirdGuess, fourthGuess]):
            print("That is correct!")
            money += 100
            print(f"You have won $100! You now have: ${money}")
            break
        elif all(word in random_word_order[2] for word in [firstGuess, secondGuess, thirdGuess, fourthGuess]):
            print("That is correct!")
            money += 100
            print(f"You have won $100! You now have: ${money}")
            break
        elif all(word in random_word_order[3] for word in [firstGuess, secondGuess, thirdGuess, fourthGuess]):
            print("That is correct!")
            money += 100
            print("You have won $100! You now have: $"+str(money))
            break
        else:
            print("Oh no! That was not correct. Please try again!")
            money -= 100
            print(f"You now have: ${money}")

        if money <= 0:
            print("You're out of money! Sorry!")
            print("Thank you for playing!")
            break

# Main function to start the game
def NYTConnections():
    print("Hello! Welcome to our game!")
    money = int(input("How much money would you like to start with? Pick any number between $100-$1000: "))

    if 100 <= money <= 1000:
        print(f"Awesome! You will start with ${money}!")
        plswork(money)
    else:
        print("Sorry, that was too much or too little money!")
        print("Try to pick something between $100 and $1000 dollars!")
        money = int(input("How much money would you like to start with? $100-$1000: "))
        if 100 <= money <= 1000:
            print(f"Awesome! You will start with ${money}")
            plswork(money)
        else:
            print("You aren't listening, so game over!")

# Start the game
NYTConnections()
