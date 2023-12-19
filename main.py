
book_path = "books/frankenstein.txt"

with open(book_path) as f:
    #read txt and print full book
    file_contents = f.read()
    print(file_contents)

    #create list of words and find length
    words = file_contents.split()
    word_count = str(len(words))
    

    #create list of characters then dictionary of character count
    characters = []
    character_count = {}
    
    for word in words:
        for char in list(word.lower()):
            characters.append(char) 

    #create dictionary and count
    for char in characters:
        #check if letter
        if char.isalpha():
            if char in character_count:
                character_count[char] += 1
            else:
                character_count.update({char:1})
    #sort dict alphabetically
    character_count = dict(sorted(character_count.items()))

    #Report findings
    print("--- Begin report of "+book_path+" ---")
    print(word_count+" words found in the document")
    print("")
    for key in character_count:
        print("The "+key+" character was found "+str(character_count[key])+" times")

