import random
import time


letter_pairs_dict = {
    "AB": "Abs", "AC": "AC", "AD": "Ad", "AE": "Algae", "AF": "Afro", "AG": "Alligator", "AH": "Albert Heijn", "AI": "AI", 
    "AJ": "Apple Juice", "AK": "Ark", "AL": "Alabama", "AM": "Arm", "AN": "Ant", "AO": "Aioli", "AP": "Ape", "ACH": "Ache", 
    "AR": "Arab", "AS": "Ass", "AT": "Art", "AU": "Australia", "AV": "Avenue", "AW": "Awning", "ASH": "Ash", "BA": "Bar", 
    "BC": "B.C.E.", "BD": "Bed", "BE": "Bee", "BF": "Boyfriend", "BG": "Bug", "BH": "Bahamas", "BI": "Bike", "BJ": "...y'know", 
    "BK": "Burger King", "BL": "Ball", "BM": "Bomb", "BN": "Bin", "BO": "Boba", "BP": "Backpack", "BCH": "Bitch (the dog)", 
    "BR": "Bro", "BS": "Bullsh*t", "BT": "Bat (animal)", "BU": "Bus", "BV": "Beaver", "BW": "Bow", "BSH": "Bush", "CA": "California", 
    "CB": "Cab", "CD": "Cody", "CE": "Cereal", "CF": "Calf", "CG": "Cog", "CH": "Chris (from MrBeast)", "CI": "City", "CJ": "CJya", 
    "CK": "Cock (animal)", "CL": "Cleopatrea", "CM": "Cum", "CN": "Can", "CO": "Coca Cola", "CP": "Checkpoint", "CCH": "C**ch", 
    "CR": "Crow", "CS": "Ceaser", "CT": "Cat", "CU": "C U (waving)", "CV": "Cava", "CW": "Cow", "CSH": "Cash", "DA": "Dagger", 
    "DB": "Dab", "DC": "D*ck", "DE": "Dee Dee (from UCN)", "DF": "Daffodil", "DG": "Dungeon", "DH": "Dhow", "DI": "Diddy", 
    "DJ": "DJ Khaled", "DK": "Donkey Kong", "DL": "Doll", "DM": "Deutsch Mark", "DN": "Daniel", "DO": "Dodo Bird", "DP": "Dude Perfect", 
    "DCH": "Dutch", "DR": "Door", "DS": "Nintendo DS", "DT": "Derilium Trigger", "DU": "Duck", "DV": "Dove", "DW": "Dwarf", "DSH": "Dish", 
    "EA": "Eagle", "EB": "Ebony", "EC": "Extra Credit", "ED": "Ed Sheeran", "EF": "Elf", "EG": "Egg", "EH": "Earth", "EI": "Eli (from camp)", 
    "EJ": "Ejaculate", "EK": "EKG", "EL": "Eel", "EM": "Emerald", "EN": "Enter", "EO": "Eeyore", "EP": "Epipen", "ECH": "Etch-A-Sketch", 
    "ER": "ER", "ES": "Essay", "ET": "ET", "EU": "Europe", "EV": "Environment", "EW": "Elbow", "ESH": "Eyelash", "FA": "Fat", "FB": "Football", 
    "FC": "Fifty Cent", "FD": "Fedora", "FE": "Fee", "FG": "F*g", "FH": "Fire Hydrant", "FI": "Fire", "FJ": "...uhhhh", "FK": "F**k", 
    "FL": "Flower", "FM": "Foam", "FN": "Fan", "FO": "Fortune Cookie", "FP": "Fap", "FCH": "Finch", "FR": "Fir", "FS": "Fossil", 
    "FT": "Foot", "FU": "F U (flipping off)", "FV": "Five", "FW": "Flow (haircut)", "FSH": "Fish", "GA": "Gag", "GB": "Garbage", 
    "GC": "Gotham Chess", "GD": "Geometry Dash", "GE": "Gee", "GF": "Girlfriend", "GH": "Ghost", "GI": "Giant", "GJ": "Goji Berry", 
    "GK": "Goku", "GL": "Goal", "GM": "Gem", "GN": "Good Night", "GO": "GoGo Squeez", "GP": "Ground Pound", "GCH": "Gucci", "GR": "Grow", 
    "GS": "Gas", "GT": "Goat", "GU": "Gukesh D.", "GV": "Guava", "GW": "Gwen Stefani", "GSH": "Goulash", "HA": "Hair", "HB": "Hamburger", 
    "HC": "Helicopter", "HD": "Head", "HE": "He", "HF": "High Five", "HG": "Hug", "HI": "HI-C", "HJ": "High Jump", "HK": "Hong Kong", 
    "HL": "Hell", "HM": "Ham", "HN": "Hen", "HO": "Hippo", "HP": "Harp", "HCH": "Hi-Chew", "HR": "Hriday", "HS": "Highschool", 
    "HT": "Hat", "HU": "Hunter", "HV": "Heaven", "HW": "Homework", "HSH": "Hashbrowns", "IA": "Ian", "IB": "Iceberg", "IC": "Ice", 
    "ID": "ID", "IE": "Ire", "IF": "IFly", "IG": "Igloo", "IH": "IHOP", "IJ": "Ijsje", "IK": "IKEA", "IL": "Island", "IM": "IM Eric Rosen", 
    "IN": "Inn", "IO": "Slither.io", "IP": "Ipad", "ICH": "Itch", "IR": "Iron", "IS": "Ice Spice", "IT": "IT", "IU": "Shiba Inu", 
    "IV": "IV", "IW": "Inchworm", "ISH": "Ishaan", "JA": "Ja Nike Shoes", "JB": "Jeb_", "JC": "JC the Champ", "JD": "Jedi", "JE": "Jeep", 
    "JF": "Jeff (from FNAF)", "JG": "Jug", "JH": "Jackhammer", "JI": "Jimmy (MrBeast)", "JK": "Joker", "JL": "Jello", 
    "JM": "Jam", "JN": "Jane Norris", "JO": "Jojo Siwa", "JP": "Japan", "JCH": "Judge", "JR": "Jar", "JS": "Jesus", "JT": "Jet", 
    "JU": "Jiu Jitsu", "JV": "Javelin", "JW": "Jewel", "JSH": "Joshua Lin",
    "KA": "Kat", "KB": "Keyboard", "KC": "Kody Choi", "KD": "Kid", "KE": "Key", "KF": "KFC", 
    "KG": "Keagan", "KH": "Khakis", "KI": "Kite", "KJ": "Kim Jeong Un", "KL": "Kill", "KM": "Mr. Kim", 
    "KN": "Ken (Barbie)", "KO": "Koala", "KP": "Katy Perry", "KCH": "Ketchup", "KR": "Kristian", 
    "KS": "Kiss", "KT": "Katana", "KU": "Kung Fu", "KV": "Kyiv", "KW": "Kiwi (fruit)", "KSH": "Kashmir", 
    "LA": "Los Angeles", "LB": "Laboratory", "LC": "Lice", "LD": "Ladder", "LE": "Lemon", "LF": "Loaf", 
    "LG": "Leg", "LH": "Lighthouse", "LI": "Lion", "LJ": "Long Jump", "LK": "Lick", "LM": "Lamb", 
    "LN": "Lean", "LO": "Lotus Flower", "LP": "Lips", "LCH": "Leech", "LR": "Lure", "LS": "Laser", 
    "LT": "Light", "LU": "Luigi", "LV": "Love", "LW": "Lawn", "LSH": "Leash", "MA": "Mama", "MB": "Mountain Biking", 
    "MC": "Minecraft", "MD": "Maid", "ME": "Me", "MF": "Mafia", "MG": "Mug", "MH": "Mahi Parikh", "MI": "Minion", 
    "MJ": "Michael Jackson", "MK": "Milk", "ML": "Meal", "MN": "Men", "MO": "Mohammed", "MP": "Matpat", 
    "MCH": "Mochi", "MR": "Mario", "MS": "Microsoft", "MT": "Mort", "MU": "Mustard", "MV": "Movie", "MW": "Mew", 
    "MSH": "Mashed Potatoes", "NA": "N/A", "NB": "Nordirbek", "NC": "Nick DiGiovanni", "ND": "Nerd", 
    "NE": "Knee", "NF": "Nerf Gun", "NG": "Nugget", "NH": "Niall Horan", "NI": "Nigeria", "NJ": "Ninja", 
    "NK": "Nickel", "NL": "Netherlands", "NM": "Nakamura", "NO": "No", "NP": "Nap", "NCH": "Notch", "NR": "Nurse", 
    "NS": "Nose", "NT": "Net", "NU": "Nut", "NV": "Navy", "NW": "Narwhal", "NSH": "Nashville Hot Chicken", 
    "OA": "Oasis", "OB": "Obama", "OC": "Orange Chicken", "OD": "Odie", "OE": "Ore", "OF": "OF", "OG": "Ogre", 
    "OH": "One-handed", "OI": "Oil", "OJ": "Orange Juice", "OK": "Oak", "OL": "Old", "OM": "Om nom nom", 
    "ON": "Onion", "OP": "Overpowered", "OCH": "Ostrich", "OR": "Orca", "OS": "Oswald (from FNAF)", "OT": "Orangutan", 
    "OU": "Outlet", "OV": "Olive", "OW": "Owl", "OSH": "Ocean", "PA": "Pat", "PB": "Peanut Butter", 
    "PC": "PC", "PD": "Pedo", "PE": "Pee", "PF": "P.F. Changs", "PG": "Pig", "PH": "Phone", "PI": "Pie", 
    "PJ": "Pajamas", "PK": "Pumpkin", "PL": "Planet", "PM": "PM (evening)", "PN": "Pen", "PO": "Po", 
    "PCH": "Pikachu", "PR": "Purr", "PS": "Piss", "PT": "Physical Therapy", "PU": "Puck", "PV": "Pole Vault", 
    "PW": "POW Block", "PSH": "Push", "CHA": "Cha cha slide", "CHB": "Chubby", "CHC": "Chocolate", 
    "CHD": "Chad", "CHE": "Cheep-cheep", "CHF": "Chef", "CHG": "Trigger", "CHH": "Cheetah", "CHI": "Chili", 
    "CHJ": "Chug Jug", "CHK": "Chalk", "CHL": "Chilly", "CHM": "Chime", "CHN": "Chin", "CHO": "Cheeto", 
    "CHP": "Chips", "CHR": "Chore", "CHS": "Cheese", "CHT": "Chat", "CHU": "Achoo! (sneezing)", "CHV": "Chives", 
    "CHW": "Chew", "CHSH": "Championship", "RA": "Rat", "RB": "Rub", "RC": "Rice", "RD": "Red", 
    "RE": "Reese's", "RF": "Ref.", "RG": "Rug", "RH": "Rhino", "RI": "Rye", "RJ": "Rajput", 
    "RK": "Rack", "RL": "Reel", "RM": "Ram", "RN": "Run", "RO": "Rotate", "RP": "Rap", "RCH": "Rich", 
    "RS": "Rose", "RT": "Rat", "RU": "Roux", "RV": "River", "RW": "Row", "RSH": "Rash", "SA": "Salt", 
    "SB": "Sabir", "SC": "Scooter", "SD": "Seed", "SE": "See", "SF": "Sunflower", "SG": "Segway", "SH": "Seahawks", 
    "SI": "Sign", "SJ": "Shell jump", "SK": "Ski", "SL": "Seal", "SM": "S'mores", "SN": "Sun", "SO": "Square-One", 
    "SP": "Sapnap", "SCH": "Sasquatch", "SR": "Sir", "ST": "Santa", "SU": "SIUUUU", "SV": "Sieve", "SW": "Subway (food)", 
    "SSH": "Sushi", "TA": "Tab", "TB": "Telletubbies", "TC": "Tack", "TD": "Toad (mario)", "TE": "Tee", "TF": "Team Fortress", 
    "TG": "Tigger", "TH": "Thigh", "TI": "Tiger", "TJ": "Trump jump", "TK": "Turkey", "TL": "Tall", "TM": "Team", 
    "TN": "Teen", "TO": "Tomato", "TP": "Toilet Paper", "TCH": "Teacher", "TR": "Tour", "TS": "Taser", "TU": "Tutu", 
    "TV": "TV", "TW": "Towel", "TSH": "Tasche", "UA": "Ursa", "UB": "Uber", "UC": "Unc. Wyatt", "UD": "Udder", 
    "UE": "Ube", "UF": "UFO", "UG": "Uggs", "UH": "U-Haul", "UI": "Uighur", "UJ": "Mt. Fuji", "UK": "UK", 
    "UL": "Umbrella", "UM": "Team oomi zoomi", "UN": "Unicorn", "UO": "Uno", "UP": "UPS", "UCH": "Urchin", "UR": "Urn", 
    "US": "US", "UT": "Unit (jacked)", "UV": "UV sunglasses", "UW": "UW", "USH": "Usher", "VA": "Van", "VB": "Volleyball", 
    "VC": "Voicechat", "VD": "Video", "VE": "Veradee", "VF": "Venus Flytrap", "VG": "Viagra", "VH": "VHS", "VI": "Violin", 
    "VJ": "Vidit Gujarathi", "VK": "Viking", "VL": "Vladimir Putin", "VM": "Venom", "VN": "Ms. Vincent", "VO": "Volcano", 
    "VP": "Viper", "VCH": "Videochat", "VR": "VR", "VS": "Vase", "VT": "Vulture", "VU": "Vacuum", "VW": "Volkswagen", 
    "VSH": "Viking ship", "WA": "Washington", "WB": "Web", "WC": "WC", "WD": "Wood", "WE": "We", "WF": "Waterfall", 
    "WG": "The Wiggles", "WH": "Whale", "WI": "Wii", "WJ": "Woojin", "WK": "Wok", "WL": "Well", "WM": "Women", 
    "WN": "Wonton", "WO": "Wolf", "WP": "Whip", "WCH": "Witch", "WR": "War", "WS": "Wasp", "WT": "Wet", "WU": "Empress Wu", 
    "WV": "Waves", "WSH": "Washing Machine", "SHA": "Shat", "SHB": "Shrub", "SHC": "Shack", "SHD": "Shed", "SHE": "She", 
    "SHF": "Sherrif", "SHG": "Shaggy", "SHH": "Shah", "SHI": "Shiny", "SHJ": "Shoji", "SHK": "Shakira", "SHL": "Shell", 
    "SHM": "Shamrock", "SHN": "Shin", "SHO": "Show", "SHP": "Sheep", "SHCH": "Schach", "SHR": "Shore", 
    "SHS": "Schlüssel", "SHT": "Sh*t", "SHU": "Shoe", "SHV": "Shovel", "SHW": "Shower"
}

unknown = []

gamemode = input("Select a gamemode (infinite or memorize): ")
print()

if gamemode.lower() == "memorize":
    answer = []
    number_of_letter_pairs = int(input("Select the number of letter pairs you want to be quizzed on: "))
    input("Press enter to begin")
    print("\n"*50)

    for i in range(number_of_letter_pairs):
        pair = random.choice(list(letter_pairs_dict.keys()))
        print(pair)
        answer.append(pair)
        if i % 2 == 0:
            time.sleep(1)
        else:
            time.sleep(4)
        print("\n"*50)

    score = number_of_letter_pairs
    for i in range(number_of_letter_pairs):
        user_input = input("Letter pair: ")
        if user_input != answer[i]:
            print(f"You failed! It was {answer[i]}")
            score -= 1

    print()
    print(f"{score}/{number_of_letter_pairs}")


elif gamemode.lower() == "infinite":

    letter = input("Enter the letter category you want to practice (\"all\" for all letter pairs): ")
    letter_pairs = list(letter_pairs_dict.keys())
    if letter != "all":
        letter_pairs = list([pair for pair in letter_pairs if pair[0] == letter.upper()])

    while True:
        pair = random.choice(letter_pairs)
        word = letter_pairs_dict.get(pair).lower()

        print(f"Your letter pair is: {pair}")
        user_input = input("What does this stand for (\"stop\" to stop)? ")

        letter_pairs.remove(pair)

        if user_input.lower() == "stop":
            break

        elif user_input.lower() != word:
            print(f"That's wrong! The word was {word}")
            unknown.append(pair)

        print(f"{len(letter_pairs)} pairs remaining")

        if len(letter_pairs) == 0:
            print()
            if len(unknown) != 0:
                print("Let's go over the letters you missed!")
            else:
                print("You did it!")
                break
            letter_pairs = unknown
            unknown = []

        print()


else:
    print("u don't want to pway my game?!? 😟🥺")


