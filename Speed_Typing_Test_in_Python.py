import time

def speed_typing_test():
    quote = "The quick brown fox jumps over the lazy dog."
    print("Type the following sentence:")
    print(quote)
    input("Press Enter when you are ready.")

    start_time = time.time()
    user_input = input()
    end_time = time.time()

    elapsed_time = end_time - start_time
    words_per_minute = len(quote.split()) / elapsed_time * 60
    accuracy = calculate_accuracy(quote, user_input)

    print("Time elapsed: {:.2f} seconds".format(elapsed_time))
    print("Words per minute: {:.2f}".format(words_per_minute))
    print("Accuracy: {:.2f}%".format(accuracy))

def calculate_accuracy(original, user_input):
    original_words = original.split()
    input_words = user_input.split()

    if len(original_words) != len(input_words):
        return 0

    correct_words = 0
    for i in range(len(original_words)):
        if original_words[i] == input_words[i]:
            correct_words += 1

    accuracy = (correct_words / len(original_words)) * 100
    return accuracy

speed_typing_test()
