def find_anagram():
    # [assignment] Add your code here
    word = input("Enter first word: ")
    anagram = input("Enter second word: ")
    
    if len(word) !=  len(anagram): return 

    for char in word: 
        if char not in anagram:
            return False
    return True
i  = "yes"
while i == 'yes':
    print(find_anagram())
