def word_count(result):
   split_string = result.split()
   count = 0
   for word in split_string:
       count += 1
   return count

def character_count(result):
    char_counts = {} #dict for storing key pair values of letter and count
    result = result.lower() #turn to lower to remove any duplicates
    for char in result:
        if char in char_counts:
            char_counts[char] += 1 #increment by 1 if already exsists in dict
        else:
            char_counts[char] = 1 #set value to 1 if the letter does not exsist in dict 
    return char_counts

def sorted_count_lists(char_counts):
    #sorted() sorts the list by default in ascending order
    #key=lambda item: item[1] : sort the list by the second value item[1] which is the frequency of the chars
    #e.g if lambda item: items[1] means: item = ("e", 5000), then item[1] = 5000
    #reverse = true changes the list to descending order
    return sorted(char_counts.items(), key=lambda item: item[1], reverse=True)





