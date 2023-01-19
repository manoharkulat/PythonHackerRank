def minion_game(string):     #---------------- need to analyse.
    Kevin = 0
    Stuart = 0
    sub_string_lst = []
    for char1_index in range(len(string)):
        char = string[char1_index]
        sub_string_lst.append(char)
        if (char1_index == (len(string)-1)):
            break
        for char2_index in range(char1_index+1, len(string)):
            char += string[char2_index]
            sub_string_lst.append(char)
        
    vowels = ("A", "E", "I","O", "U" )
    for word in sub_string_lst:
        if (word.startswith(vowels)):
            Kevin += 1
        else:
            Stuart += 1
    if (Kevin > Stuart):
        print(f"Kevin {Kevin}")
    elif (Kevin < Stuart):
        print(f"Stuart {Stuart}")
    else:
        print("Draw")
    

minion_game("BANANA")