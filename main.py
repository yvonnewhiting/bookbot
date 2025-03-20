import sys
from stats import word_count
from stats import character_count 
from stats import sorted_count_lists

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main ():
   if len(sys.argv) <= 1:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1)
      
   result =get_book_text(sys.argv[1])
   # Pass the result to word_count to get the word count
   count= word_count(result)
   #Pass the result to charcter_count to get sll the character counts
   chars_count = character_count(result)

   sorted_chars = sorted_count_lists(chars_count)
   #display results
   print("============ BOOKBOT ============")
   print("Analyzing book found at books/frankenstein.txt...")
   print("----------- Word Count ----------")
   print(f"Found {count} total words")
   print(" --------- Character Count -------")
   
   for char, freq in sorted_chars:
      if char.isalpha():
         print(f"{char}: {freq}")

main()
   