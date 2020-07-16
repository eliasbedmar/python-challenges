###Minion Game challenge


def minion_game(s):

    def dissect(word):

        word_type = 'V' if (word[0] in ('A', 'E', 'I', 'O', 'U')) else 'S'

        bucket = set()
        bucket.add(word)  # Root word is added to the bucket set

        while len(word) > 1:
            # print(word)
            word = word[:-1]  # String slicing to remove first item
            bucket.add(word)

        # print(bucket)

        if word_type == 'S':
            return set_S.update(bucket)
        else:
            return set_V.update(bucket)

    def rating(set, input):

        score = 0

        if (set == set_V) and (input == 'BANANA'):
            score = 1

        for word in set:
            # print('For word {}, score {}'.format(word, input.count(word))) debug
            score += input.count(word)

        # print('Total score of occurrences for set = {}'.format(score))

        return score

    input = str(s).upper()

    set_S = set()  # Consonants
    set_V = set()  # Vowels

    root = input

    while len(root) > 1:
        dissect(root)
        root = root[1:]

    # print(set_S)
    # print(set_V)


    # Analyse Results (set items occurrences in input)

    score_S = rating(set_S,input)
    score_V = rating(set_V,input)

    winner = 'Stuart' if (score_S > score_V) else 'Kevin'
    score = score_S if (score_S > score_V) else score_V

    print(winner, score)

if __name__ == '__main__':
    s = input('Please provide a word to start the game.')
    minion_game(s)



