'''FInd no of words in a string'''

def no_of_words_in_string(str):
    words=str.split()
    print("No. of words :",len(words))

if __name__=="__main__":
    user_str = input("Enter String :")
    no_of_words_in_string(user_str)