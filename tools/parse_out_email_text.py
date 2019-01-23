#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string


def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        (in Part 2, you will also add stemming capabilities)
        and return a string that contains all the words
        in the email (space-separated) 

        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)

        """

    stemmer = SnowballStemmer("english")

    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    words_array = []

    if len(content) > 1:
        ### remove punctuation
        text_string = content[1].translate(string.maketrans("", ""), string.punctuation)

        ### project part 2: comment out the line below
        # words = text_string

        # bad_words = {"sara", "shackleton", "chris", "germani"}
        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)
        # for word in text_string.split():
        #     stem = stemmer.stem(word)
        #     if stem not in bad_words:
        #         words_array.append(stem)
        for word in text_string.split():
            stem = stemmer.stem(word)
            words_array.append(stem)

    words_a = string.join(words_array, ' ')

    return str(words_a)


def main():
    ff = open("../text_learning/test_email.txt", "r")
    text = parseOutText(ff)
    print text


if __name__ == '__main__':
    main()
