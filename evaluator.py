def evaluate_answer(answer):

    word_count = len(answer.split())

    if word_count >= 20:
        return 8

    elif word_count >= 10:
        return 6

    else:
        return 4