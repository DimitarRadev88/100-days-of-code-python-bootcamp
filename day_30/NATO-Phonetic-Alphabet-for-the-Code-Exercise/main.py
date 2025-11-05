import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# def instructor_solution():
#     word = input("Enter a word: ").upper()
#     try:
#         result_list = [phonetic_dict[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#         instructor_solution()
#     else:
#         print(result_list)
#
# instructor_solution()

def get_nato_code(word):
    try:
        result_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        return None
    else:
        return result_list


input_word = input("Enter a word: ").upper()

coded_word = get_nato_code(input_word)

while coded_word is None:
    input_word = input("Enter a word: ").upper()
    coded_word = get_nato_code(input_word)

print(coded_word)
