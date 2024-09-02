def remove(input, words_to_remove):
    words = input.split()
    filtered_words = [word for word in words if word.lower() not in words_to_remove]
    result_string = ' '.join(filtered_words)
    return result_string