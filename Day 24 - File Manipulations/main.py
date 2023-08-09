
with open("./Input/Names/invited_names.txt") as file:
    names = file.read()
    names_list = names.split()
    print(names_list)

with open("./Input/Letters/starting_letter.txt", mode="r+") as file:
    content = file.read()
    print(content)


for name in names_list:
    with open(f"./Output/ReadyToSend/Letter_for_{name}", mode="w") as file:
        letter = content.replace("[name]", f"{name}")
        print(letter)
        file.write(letter)

