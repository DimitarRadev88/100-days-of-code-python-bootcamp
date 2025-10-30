#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

names = []

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()

with open("Input/Names/invited_names.txt") as names_file:
    lines = names_file.readlines()
    for line in lines:
        names.append(line.strip())

for name in names:
    with open(f"Output/ReadyToSend/letter_for_{name}.docx", mode="w") as ready_letter_file:
        ready_letter_file.write(letter.replace("[name]", name))