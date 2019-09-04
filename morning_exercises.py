# DC 08 2019  Week 2 Day 2

# Leetspeak cipher

#str = 'This is my absolute test string to see if my Leet cipher is working'
#original_character = ['A','a','E','e','G','g','I','i','O','o','S','s','T','t']
#new_character = ['4','4','3','3','6','6','1','1','0','0','5','5','7','7']
#
#index = 0
#
#while str[index] < len(str):
#    while str[index] == str[original_character]
#    return index
#    print(str[index])
#    index = index + 1

# This is where I got to above 
# This is how it should look below

#Take these characters and look to see if they exist in the list and replace with the second list

#text = 'This is my absolute test string to see if my Leet cipher is working'
#text = 'hello world'
#original_character = ['A','a','E','e','G','g','I','i','O','o','S','s','T','t']
#new_character = ['4','4','3','3','6','6','1','1','0','0','5','5','7','7']

#text = input("Please enter a phrase: ")
#original_character = ['A','a','E','e','G','g','I','i','O','o','S','s','T','t']
#new_character = [4,4,3,3,6,6,1,1,0,0,5,5,7,7]
#translation = ""
#uppercased_text = text.upper()
#
#index = 0
#while index < len(text):
#    #print(text[index])
#    
#    index_inner_loop = 0
#    letter_to_add_to_translation = ""
#    while index_inner_loop < len(original_character):
#        #print(new_character[index_inner_loop])
#        if text[index] == original_character[index_inner_loop]:
#            #print("We have a match!")
#            #print(new_character[index_inner_loop])
#            letter_to_add_to_translation = str(new_character[index_inner_loop])
#            break
#        else:
#            #print("No matches! sad face emoji")
#            letter_to_add_to_translation = text[index]
#        index_inner_loop += 1
#    index += 1
#    translation = translation + letter_to_add_to_translation
#
#print(translation)

#Morning notes

#for x in range(5):
#    print(x)

#Try/Accept
#count = 0
#input_string = input("How high should we count? ")
#MAX = int(input_string)
#while (count < MAX):
#    print(count)
#    count += 1



# Dictionaries!!

dict = {
    "A":1,
    "b":2,
    "c":3,
    'd':'Test',
}

print(dict['A'])

if 'E' in dict:
    print('Yes')
else:
    print('No')

#add item to dict

dict['e'] = 5
print(dict)
dict['A'] = 'B'
del dict['A']
print(dict)

# method is a funtion for an object such as string or dictionary

