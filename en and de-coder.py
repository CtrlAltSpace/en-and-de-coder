def encode(text):
    code_database = {
        "a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6", "g": "7", "h": "8", 
        "i": "9", "j": "10", "k": "11", "l": "12", "m": "13", "n": "14", "o": "15", 
        "p": "16", "q": "17", "r": "18", "s": "19", "t": "20", "u": "21", "v": "22", 
        "w": "23", "x": "24", "y": "25", "z": "26", " ": "/", "1": "a", "2": "b", "3": "c", "4": "d", "5": "e", "6": "f", "7": "g", "8": "h", 
        "9": "i", "10": "j", "11": "k", "12": "l", "13": "m", "14": "n", "15": "o", 
        "16": "p", "17": "q", "18": "r", "19": "s", "20": "t", "21": "u", "22": "v", 
        "23": "w", "24": "x", "25": "y", "26": "z"
    }

    # Keep special characters unchanged
    encoded = []
    for char in text.lower():
        if char in code_database:
            encoded.append(code_database[char])
        else:
            encoded.append(char)
    return ' '.join(encoded)

def decode(text):
    code_database = {
        "1": "a", "2": "b", "3": "c", "4": "d", "5": "e", "6": "f", "7": "g", "8": "h", 
        "9": "i", "10": "j", "11": "k", "12": "l", "13": "m", "14": "n", "15": "o", 
        "16": "p", "17": "q", "18": "r", "19": "s", "20": "t", "21": "u", "22": "v", 
        "23": "w", "24": "x", "25": "y", "26": "z", "/": " ",  "a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6", "g": "7", "h": "8", 
        "i": "9", "j": "10", "k": "11", "l": "12", "m": "13", "n": "14", "o": "15", 
        "p": "16", "q": "17", "r": "18", "s": "19", "t": "20", "u": "21", "v": "22", 
        "w": "23", "x": "24", "y": "25", "z": "26"
    }

    text_split = text.split()
    decoded = []

    for char in text_split:
        if char in code_database:
            decoded.append(code_database[char])
        else:
            decoded.append(char)
    return ''.join(decoded)

def menu():
    while True:
        print("Choose one option:")
        print("1. Text to Secret Code")
        print("2. Secret Code to Text")
        
        try:
            choice = int(input("Enter your choice (1/2): "))
        except ValueError:
            print("Invalid choice. Please enter 1 or 2.")
            continue

        if choice == 1:
            text = input("Enter text: ")
            if text.strip() == "":
                print("Text cannot be empty.")
                continue
            secret = encode(text)
            print(f"Secret code: {secret}")

        elif choice == 2:
            secret = input("Enter secret code: ")
            if secret.strip() == "":
                print("Secret code cannot be empty.")
                continue
            text_result = decode(secret)
            print(f"Converted text: {text_result}")

        else:
            print("Invalid choice. Please enter 1 or 2.")

menu()
