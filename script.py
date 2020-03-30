import re

#list of all the possible values that will be used
value_list = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
}

# word list to denote important checkpoints
word_list = {
    "million": 1000000,
    "thousand": 1000,
    "hundred": 100
}

#Replace possible causes of error
def clean_data(data):
    data = data.replace('and ', '')
    data = data.replace(', ', ' ')
    data = data.replace('.', '')
    data = data.replace(',', ' ')
    data = data.strip(' ')

    # return the cleaned data
    return str(data)

# This is where all the manipulation and activities occur
def manipulate(data, item):
    # The data is cleaned to prevent errors
    data = clean_data(data)
    res = 0
    # Hundred is most common like in hundred thousand hundred million, so it needs to be a checkpoint
    if 'hundred' in data:
        temp_data = data.split('hundred')
        res = value_list[temp_data[0].strip( )] * word_list['hundred']
        if(bool(temp_data[1]) == True):
            a = clean_data(temp_data[1])
            if(len(a.split(' ')) >= 2):
                a = a.split(' ')
                for data_item in range(0,len(a)):
                    res += value_list[a[data_item]]
            else:
                res = res + value_list[a]
        res = res * word_list[item]
    else:
        if(len(data.split(' ')) >= 2):
            temp_data = data.split(' ')
            for data_item in range(0, len(temp_data)):
                res += value_list[temp_data[data_item]] * word_list[item]
        else:
            res = res + value_list[data]

        if(len(data.split(' ')) == 1):
            res = value_list[data.split(' ')[0]]
            res = res *  word_list[item]
    return res

# This function is the main function that runs when the file is requested
def words_to_figures(word):

    if word == 'q':
        return
    result = []
    final_value = 0
    if(len(word) < 3):
        print("Wrong input... Try again :(")
        request_input()
    
    if(len(word) < 9):
        for value in value_list:
            if (word == value):
               final_value = value_list[value]
    else:
        for value in word_list:
            if(re.search(value,word)):
                temp = word.split(value)
                # append the return value to result
                result.append(manipulate(temp[0], value))
                word = temp[1]
        
    
    #Clean the word to prevent any error in the last steps
    word = clean_data(word)
    res = 0
    if(len(word.split(' ')) > 1):
        temp_word = word.split(' ')
        for data_item in temp_word:
            res += value_list[data_item]
        result.append(res)
    elif(word != ''):
        if(final_value == 0):
            res = value_list[word]
            result.append(res)
    
    # sum all the numbers in the array
    for number in result:
        final_value += number
    
    #uncomment this line if you need to return the value to be used in another process
    # return final_value

    print(final_value)



print("Word to figures converter by ", end=" ")
print("Name: Akachukwu Simon Mbe", "  Reg No: 17/EG/EE/1386", end="\n")


def request_input():
    word = input("Enter a valid figure in words(q to quit):")
    words_to_figures(word)


request_input()

#### Test cases ####
# twenty one
# six hundred and eight
# ten million
# ten million and thirty two
# fifteen million three hundred and twenty one thousand
# thirty million five hundred and twenty two thousand three hundred and forty six
