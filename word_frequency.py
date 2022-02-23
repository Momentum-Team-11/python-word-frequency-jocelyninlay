STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as file:
        text_string = file.read()
        # print(text_string[0:100])
        #print(f"{len(text_string)}")
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
        print(text_string[0:100])

# def clean_text(text):
#     text = text.lower()
#     all_letters = "abcdefghijklmnopqrstuvwxyz"
#     text_to_keep = ""
#     for char in text:
#         if char in all_letters:
#             text_to_keep += char
#     return text_to_keep
#     print(text)

# delete punctutation       
# deinfitely gonna need a for loop .. for lines in file??
# want to use x.lower() to make everything lowercase
# want to use x.split(" ") to make the text into a list
# might use x.replace(y,"") to get rid of words or punctuation 
# want to use x.count(y) to count the words 
# python word_frequency.py praise_song_for_the_day.txt
# dont forget to close the file at the end, so it stops reading it.      


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
