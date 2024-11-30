def clean_input_string(input_string):
    # List of charachter that will be removed
    characters_to_remove = ['.', ',', '!', '?', '’', "'"]
    
    # Create a translation table that maps each character that needs to removed to None
    translation_table = str.maketrans('', '', ''.join(characters_to_remove))
    
    # Uses the translation table from above to clean the string
    cleaned_string = input_string.translate(translation_table)
    
    return cleaned_string

def reverse_string(cleaned_string):
    # Split the cleaned string into seperate words and reverse the list
    words = cleaned_string.split()
    reversed_words = words[::-1]
    
    # Join the reversed list back into a string
    reversed_string = ' '.join(reversed_words)
    
    return reversed_string

def remove_duplicates(reversed_string):
    # again Split the string into words and remember first occurrences
    words = reversed_string.split()
    seen = set()
    unique_words = []

   # Join the unique words back into a string, duplicates will not be added
    for word in words:
        if word not in seen:
            seen.add(word)
            unique_words.append(word)
    
    return ' '.join(unique_words)

def calculate_median_length(unique_string):
    # Split the string into words
    words = unique_string.split()
    word_lengths = sorted(len(word) for word in words)
    
    # Calculate the median word length of the current list
    n = len(word_lengths)
    if n == 0:
        return 0  # for unexpected empty case
    if n % 2 == 1:  # for odd number of words
        median = word_lengths[n // 2]
    else:  # for even number of words
        median = (word_lengths[n // 2 - 1] + word_lengths[n // 2]) // 2
    
    return median

def main():
    input_string = input()
    
    # clean then print the input string
    cleaned_string = clean_input_string(input_string)
    
    # reverse then print the cleaned string
    reversed_string = reverse_string(cleaned_string)
    print(reversed_string)
    
    # remove duplicates from the reversed string then 
    reversed_string_without_duplicates = remove_duplicates(reversed_string)
    print(reversed_string_without_duplicates)
    
    # find and print the median word length
    median_word_length = calculate_median_length(reversed_string_without_duplicates)
    print(median_word_length)

if __name__ == "__main__":
    main()


