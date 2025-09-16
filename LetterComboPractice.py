import random
import time


letter_pairs_dict = {
    "AB": "Abs", "AC": "AC", "AD": "Ad", "AE": "Algae", "AF": "Afro", "AG": "Alligator", "AH": "Albert Heijn", "AI": "AI", 
    "AJ": "AJ (& Big Justice)", "AK": "Ark", "AL": "Alabama", "AM": "AM (morning)", "AN": "Ant", "AO": "Aioli", "AP": "Ape", "ACH": "Ache",
    "AR": "Arab", "AS": "Ass" + "\n"*50, "AT": "Art", "AU": "Australia", "AV": "Avenue", "AW": "Awning", "ASH": "Ash", "BA": "Banana",
    "BC": "B.C.E.", "BD": "Bed", "BE": "Bee", "BF": "Boyfriend", "BG": "Bug", "BH": "Bahamas", "BI": "Bike", "BJ": "Blowjob" + "\n"*50,
    "BK": "Burger King", "BL": "Ball", "BM": "Bomb", "BN": "Bin", "BO": "Boba", "BP": "Backpack", "BCH": "Bitch" + "\n"*50,
    "BR": "Baskin Robbins", "BS": "Bullshit" + "\n"*50, "BT": "Bat", "BU": "Bus", "BV": "Beaver", "BW": "Bow", "BSH": "Bush", "CA": "California",
    "CB": "Cab", "CD": "CD", "CE": "Cereal", "CF": "Calf", "CG": "Cog", "CH": "Chris (from MrBeast)", "CI": "City", "CJ": "CJya", 
    "CK": "Cock" + "\n"*50, "CL": "Call", "CM": "Cum" + "\n"*50, "CN": "Can", "CO": "Coca Cola", "CP": "Checkpoint", "CCH": "Cooch" + "\n"*50,
    "CR": "Car", "CS": "Caesar", "CT": "Cat", "CU": "C U (waving)", "CV": "Cava", "CW": "Cow", "CSH": "Cash", "DA": "Daddy", 
    "DB": "Dab", "DC": "Washington DC", "DE": "Dee Dee (from UCN)", "DF": "Daffodil", "DG": "Dog", "DH": "Dhar Mann", "DI": "Diddy", 
    "DJ": "DJ", "DK": "Donkey Kong", "DL": "Doll", "DM": "Dam", "DN": "Daniel", "DO": "Dodo Bird", "DP": "Dude Perfect", 
    "DCH": "Dutch", "DR": "Door", "DS": "Nintendo DS", "DT": "Dot", "DU": "Duck", "DV": "Dove", "DW": "Dwarf", "DSH": "Dish", 
    "EA": "Eagle", "EB": "Ebony", "EC": "Extra Credit", "ED": "Ed Sheeran", "EF": "Elf", "EG": "Egg", "EH": "Earth", "EI": "Ein Ei", 
    "EJ": "Ejaculate" + "\n"*50, "EK": "EKG", "EL": "Eel", "EM": "Emerald", "EN": "Enter", "EO": "Eeyore", "EP": "Epipen", "ECH": "Etch-A-Sketch",
    "ER": "ER", "ES": "Essay", "ET": "E.T.", "EU": "Europe", "EV": "Environment", "EW": "Ew!", "ESH": "Eshaan", "FA": "Fanta", "FB": "Facebook", 
    "FC": "Fifty Cent", "FD": "Fedora", "FE": "Fee", "FG": "Fog", "FH": "Fire Hydrant", "FI": "Fire", "FJ": "Footjob" + "\n"*50, "FK": "Fuck" + "\n"*50,
    "FL": "Florida", "FM": "Foam", "FN": "Fan", "FO": "Fortune Cookie", "FP": "Fap" + "\n"*50, "FCH": "Finch", "FR": "Frog", "FS": "Fossil",
    "FT": "Foot", "FU": "F U (flipping off)", "FV": "Five", "FW": "Flow (haircut)", "FSH": "Fish", "GA": "Gag", "GB": "Great Britain", 
    "GC": "Group Chat", "GD": "Geometry Dash", "GE": "Ghee", "GF": "Girlfriend", "GH": "Ghost", "GI": "Giant", "GJ": "Gojo", 
    "GK": "Goku", "GL": "Goal", "GM": "Gem", "GN": "Good Night", "GO": "GoGo Squeez", "GP": "Ground Pound", "GCH": "Gucci", "GR": "Grow", 
    "GS": "Goose", "GT": "Goat", "GU": "Gukesh D.", "GV": "Guava", "GW": "Gwen Stefani", "GSH": "Goulash", "HA": "Ha ha (laughing)", "HB": "Hamburger", 
    "HC": "Hi-C", "HD": "Head", "HE": "Heel", "HF": "High Five", "HG": "Hug", "HI": "Hi", "HJ": "High Jump", "HK": "Hawk Tuah" + "\n"*50,
    "HL": "Hell", "HM": "Ham", "HN": "Hen", "HO": "Hippo", "HP": "Health Points", "HCH": "Hi-Chew", "HR": "Hriday", "HS": "Highschool", 
    "HT": "Hat", "HU": "Huzz", "HV": "Heaven", "HW": "Homework", "HSH": "Hashbrowns", "IA": "Ian", "IB": "Iceberg", "IC": "Ice", 
    "ID": "ID", "IE": "Ireland", "IF": "IFly", "IG": "Instagram", "IH": "IHOP", "IJ": "Ijsje", "IK": "IKEA", "IL": "Ill", "IM": "IM Levy Rozman", 
    "IN": "Inn", "IO": "Slither.io", "IP": "Ipad", "ICH": "Itch", "IR": "Iron", "IS": "Ice Spice", "IT": "IT", "IU": "Shiba Inu", 
    "IV": "IV", "IW": "Inchworm", "ISH": "Ishaan", "JA": "Ja Nike Shoes", "JB": "J*b", "JC": "JC the Champ", "JD": "Jedi", "JE": "Jeep", 
    "JF": "Jeff (from FNAF)", "JG": "Jug", "JH": "Jackhammer", "JI": "Jimmy (MrBeast)", "JK": "Joker", "JL": "Jello", 
    "JM": "Jam", "JN": "Jane Norris", "JO": "Jojo Siwa", "JP": "Japan", "JCH": "Judge", "JR": "Jar", "JS": "Jesus", "JT": "Jet", 
    "JU": "Jiu Jitsu", "JV": "Java", "JW": "Jewel", "JSH": "Joshua Lin",
    "KA": "Kayak", "KB": "Keyboard", "KC": "Kick", "KD": "Kid", "KE": "Key", "KF": "KFC", 
    "KG": "Keagan", "KH": "Khakis", "KI": "Kite", "KJ": "Kim Jeong Un", "KL": "Kill", "KM": "Kam", 
    "KN": "Ken (Barbie)", "KO": "Koala", "KP": "Katy Perry", "KCH": "Ketchup", "KR": "Kristian", 
    "KS": "Kiss", "KT": "Kat", "KU": "Kung Fu", "KV": "Kyiv", "KW": "Kiwi", "KSH": "Jake Kashi", 
    "LA": "Los Angeles", "LB": "Laboratory", "LC": "Lick", "LD": "Lead (element)", "LE": "Darci Lee", "LF": "Leaf", 
    "LG": "Leg", "LH": "Lighthouse", "LI": "Lion", "LJ": "Long Jump", "LK": "Loki", "LM": "Lamb", 
    "LN": "Lean", "LO": "Low", "LP": "Lips", "LCH": "Leech", "LR": "Lure", "LS": "Laser", 
    "LT": "Light", "LU": "Luigi", "LV": "Love", "LW": "Lawn", "LSH": "Leash", "MA": "Mama", "MB": "Mob", 
    "MC": "Minecraft", "MD": "Maid", "ME": "Me", "MF": "Mafia", "MG": "Mug", "MH": "Mahi Parikh", "MI": "Minion", 
    "MJ": "Michael Jackson", "MK": "Milk", "ML": "Meal", "MN": "Men", "MO": "Mohammad", "MP": "Mop", 
    "MCH": "Mochi", "MR": "Mario", "MS": "Microsoft", "MT": "Mountain", "MU": "Mustard", "MV": "Movie", "MW": "Mew", 
    "MSH": "Mashed Potatoes", "NA": "N/A", "NB": "Knob", "NC": "Nick DiGiovanni", "ND": "Nerd", 
    "NE": "Knee", "NF": "Nerf Gun", "NG": "Nugget", "NH": "Niall Horan", "NI": "Nigeria", "NJ": "Ninja", 
    "NK": "North Korea", "NL": "Netherlands", "NM": "Nemo", "NO": "No", "NP": "Nap", "NCH": "Notch", "NR": "Nurse", 
    "NS": "Nose", "NT": "Net", "NU": "Nut", "NV": "Nevada", "NW": "Narwhal", "NSH": "Nashville Hot Chicken", 
    "OA": "Oasis", "OB": "Obama", "OC": "Orange Chicken", "OD": "Odie", "OE": "Oboe", "OF": "Onlyfans", "OG": "Ogre", 
    "OH": "One-handed", "OI": "Oil", "OJ": "Orange Juice", "OK": "Oak", "OL": "Old", "OM": "Om nom nom", 
    "ON": "Onion", "OP": "Overpowered", "OCH": "Ostrich", "OR": "Oregon", "OS": "Operating System", "OT": "Oats", 
    "OU": "Outlet", "OV": "Olive", "OW": "Ow!", "OSH": "Ocean", "PA": "Pat", "PB": "Peanut Butter", 
    "PC": "PC", "PD": "Pedo", "PE": "Physical Education", "PF": "P.F. Changs", "PG": "Pig", "PH": "PH", "PI": "Pippy", 
    "PJ": "Pajamas", "PK": "Peak", "PL": "Planet", "PM": "PM (evening)", "PN": "Pen", "PO": "Po", 
    "PCH": "Pikachu", "PR": "PR (running)", "PS": "Piss", "PT": "Physical Therapy", "PU": "Puck", "PV": "Pole Vault", 
    "PW": "POW Block", "PSH": "Push", "CHA": "Cha cha slide", "CHB": "Chubby", "CHC": "Chicken", 
    "CHD": "Chad", "CHE": "Cheep-cheep", "CHF": "Chef", "CHG": "Trigger", "CHH": "Cheetah", "CHI": "Chili", 
    "CHJ": "Chug Jug", "CHK": "Chalk", "CHL": "Chilly", "CHM": "Chime", "CHN": "Chin", "CHO": "Cheeto", 
    "CHP": "Chips", "CHR": "Chair", "CHS": "Cheese", "CHT": "Chat", "CHU": "Achoo!", "CHV": "Chives", 
    "CHW": "Chew", "CHSH": "Championship", "RA": "Rain", "RB": "Ribs", "RC": "RC Car", "RD": "Road", 
    "RE": "Reese's", "RF": "Reef", "RG": "Rug", "RH": "Rhino", "RI": "Rye", "RJ": "Rajput", 
    "RK": "Rake", "RL": "Roll", "RM": "Ram", "RN": "Run", "RO": "Rotate", "RP": "Rap", "RCH": "Rich", 
    "RS": "Rose", "RT": "Rat", "RU": "Roux", "RV": "RV Trailer", "RW": "Row", "RSH": "Rash", "SA": "Santa", 
    "SB": "Sob", "SC": "Scooter", "SD": "Sad", "SE": "See", "SF": "Sunflower", "SG": "Segway", "SH": "Seahawks", 
    "SI": "Sign", "SJ": "Slim Jim", "SK": "Ski", "SL": "Seal", "SM": "S'mores", "SN": "Sun", "SO": "Square-One", 
    "SP": "Sap", "SCH": "Sasquatch", "SR": "Sir", "ST": "Street", "SU": "SIUUUU", "SV": "SUV", "SW": "Sow", 
    "SSH": "Sushi", "TA": "Tab", "TB": "Telletubbies", "TC": "Tack", "TD": "Toad", "TE": "Tee", "TF": "Team Fortress", 
    "TG": "Tigger", "TH": "Theo", "TI": "Tiger", "TJ": "Trump jump", "TK": "Turkey", "TL": "Tall", "TM": "Team", 
    "TN": "Teen", "TO": "Tomato", "TP": "Toilet Paper", "TCH": "Teacher", "TR": "Tour", "TS": "Taser", "TU": "Tutu", 
    "TV": "TV", "TW": "Towel", "TSH": "Tasche", "UA": "UAE", "UB": "Uber", "UC": "Ulcer", "UD": "Udder", 
    "UE": "Ube", "UF": "UFO", "UG": "Uggs", "UH": "U-Haul", "UI": "User Interface", "UJ": "Mt. Fuji", "UK": "UK", 
    "UL": "Umbrella", "UM": "Team oomi zoomi", "UN": "Unicorn", "UO": "Uno", "UP": "UPS", "UCH": "Urchin", "UR": "Urn", 
    "US": "US", "UT": "Unit (jacked)", "UV": "UV sunglasses", "UW": "UW", "USH": "Usher", "VA": "Van", "VB": "Volleyball", 
    "VC": "Voicechat", "VD": "Video", "VE": "Veradee", "VF": "Venus Flytrap", "VG": "Viagra", "VH": "VHS", "VI": "Vi", 
    "VJ": "Vidit Gujarathi", "VK": "Viking", "VL": "Vladimir Putin", "VM": "Venom", "VN": "Ms. Vincent", "VO": "Volcano", 
    "VP": "Viper", "VCH": "Voucher", "VR": "VR", "VS": "Vase", "VT": "Vulture", "VU": "Vacuum", "VW": "Volkswagen", 
    "VSH": "Viking ship", "WA": "Washington", "WB": "Web", "WC": "WC", "WD": "Wood", "WE": "We", "WF": "Wife", 
    "WG": "Wagon", "WH": "Whale", "WI": "Wii", "WJ": "Woojin", "WK": "Wok", "WL": "Well", "WM": "Women", 
    "WN": "Wonton", "WO": "Wolf", "WP": "Whip", "WCH": "Witch", "WR": "War", "WS": "Wasp", "WT": "Wet", "WU": "Empress Wu", 
    "WV": "Waves", "WSH": "Washing Machine", "SHA": "Shat", "SHB": "Shrub", "SHC": "Shack", "SHD": "Shed", "SHE": "She", 
    "SHF": "Sherrif", "SHG": "Shaggy", "SHH": "Shah", "SHI": "Shiny", "SHJ": "Shoji", "SHK": "Shakira", "SHL": "Shell", 
    "SHM": "Shamrock", "SHN": "Shin", "SHO": "Show", "SHP": "Sheep", "SHCH": "Schach", "SHR": "Shore", 
    "SHS": "Schlüssel", "SHT": "Shit", "SHU": "Shoe", "SHV": "Shovel", "SHW": "Show"
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
        user_input = input("Letter pair: ").upper()
        if user_input != answer[i]:
            print(f"You failed! It was {answer[i]}")
            score -= 1

    print()
    print(f"{score}/{number_of_letter_pairs}")


elif gamemode.lower() == "infinite":

    letter = input("Enter the letter category you want to practice (\"all\" for all letter pairs): ")
    letter_pairs = list(letter_pairs_dict.keys())

    if letter != "all":

        new = []
        for pair in letter_pairs:
            if len(letter) == 1 and pair[0] == letter.upper() and (len(pair) == 2 or (len(pair) > 2 and pair[1] != "H")):
                new.append(pair)
            elif len(letter) == 2 and pair[:2] == letter.upper() and len(pair) > 2:
                new.append(pair)
        
        letter_pairs = new

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


