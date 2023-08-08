with open("./Input/Names/invited_names.txt") as file:
    names = file.read()
    names_list = names.split()
    print(names_list)

with open("./Input/Letters/starting_letter.txt", mode="r+") as file:
    content = file.read()
    print(content)
    var = content.find("[name]")
    print(f"var: {var}")
    content = file.read()
    print(content)