def main():
    filename = "books/frankenstein.txt"
    with open(filename) as f:
        textfile = f.read()

    wordcount = count_words(textfile)
    letter_dict = count_letters(textfile)
    sorted_letters = list(count_letters(textfile))
    sorted_letters.sort()

    print(f"---Begin report---\n")
    print(f"* {wordcount} words found in the document\n")
    for char in sorted_letters:
        print(f"- The' {char}' character  was found {letter_dict[char]} times.")
    print("\n---End report---") 

    
def count_words(text):    
    wordcount = text.split()
    return len(wordcount)

def count_letters(text):
    text = text.lower()
    letters = dict()
    for char in text:
        if char.isalpha() and char not in letters:
            letters[char] = 1
        elif char.isalpha():
            letters[char] += 1
    return letters

main()