# a function that returns a key with the biggest integer value.

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_score_key = None
    max_score = float('-inf')

    for key, value in a_dictionary.items():
        if value > max_score:
            max_score = value
            max_score_key = key

    return max_score_key