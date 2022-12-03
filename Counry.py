
def display_menu():
    print("COMMAND MENU")
    print("View -View country name")
    print("Add - Add a country")
    print("Delete - Delete a country")
    print("Exit- exit")
    print()

def display_codes(countries):
    codes = list(countries.keys())
    codes.sort()
    codes_line = "Country codes: "
    for code in codes:
        codes_line  += code + " "
    print(codes_line)


def view(countries):
    display_codes(countries)
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries: 
        name = countries[code]
        print(f"Country name: {name}. \n")
    else: 
        print("No country found. Please try again. \n")


def add(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"{name} is already using this code.")
    else:
        name = input("Enter country name: ")
        name = name. title()
        countries[code]= name
        print(f"{name} was added. \n")


def delete(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries.pop(code)
        print(f"{name} was deleted.\n")
    else: 
        print("Country not found. Please try again.\n")


def main():
    countries = {"CA": "Canada",
                 "US": "United States",
                 "MX": "Mexico"}


    display_menu()
    while True:
        command = input("Command: ")
        command = command.lower()
        if command =="view":
            view(countries)
        elif command == "add":
            add(countries)
        elif command =="delete":
            delete(countries)
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please try again")

if __name__ == "__main__":
    main()
