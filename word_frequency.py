from audioop import reverse


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as file:
        text_string = file.read()
        text_string = text_string.replace(",", "")
        text_string = text_string.replace(".", "")
        text_string = text_string.replace("'", "")
        text_string = text_string.replace("?", "")
        text_string = text_string.replace("!", "")
        text_string = text_string.replace("\\n", "")
        text_string = text_string.replace(":", "")
        text_string = text_string.replace("[", "")
        text_string = text_string.replace("]", "")
        text_string = text_string.replace("\"", "")
        text_string = text_string.replace("’", "")
        text_string = text_string.replace("-", "")
        text_string = text_string.replace("—", "")
        text_string = text_string.lower()
        text_string = text_string.split()
        no_stop_words = {}
        #print(text_string[0:100])
        #now loop through the words to remove STOP WORDS
        for word in text_string:
            # need to check if the words in the file are in STOP_WORDS
            if word not in STOP_WORDS:
                if word in no_stop_words:
                    no_stop_words[word] += 1
                else:
                    no_stop_words[word] = 1
        freqs = dict(sorted(no_stop_words.items(), key=lambda item: item[1], reverse=True))
        #print(freqs)
        for key,value in freqs.items():
            print(f"{key:>20} | {(value * '*'):<20}")


        return freqs
           


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
