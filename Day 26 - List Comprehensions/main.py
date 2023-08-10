student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pd.read_csv("nato_phonetic_alphabet.csv")
my_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(my_dict)

word = input("Please indicate your word").upper()

phonetic_list = [my_dict[x] for x in word]
print(phonetic_list)

