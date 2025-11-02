import pandas

nato_codes_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_codes_dataframe.iterrows()}
print(nato_dict)

user_input = input("Enter a word: ")

coded_word = [nato_dict[letter.upper()] for letter in user_input]

print(coded_word)
