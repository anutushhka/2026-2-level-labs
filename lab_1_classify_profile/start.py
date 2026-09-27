"""
Language detection starter.
"""

# pylint: disable=unused-variable, duplicate-code

from lab_1_classify_profile.main import (
    tokenize,
    remove_stop_words,
    calculate_frequencies,
    get_top_n_words,
    create_language_profile,
    detect_language_by_top_n,
    detect_language_by_mse
    )

if __name__ == "__main__":
    main()

def main() -> None:
    """
    Launches an implementation.
    """
    with open("lab_1_classify_profile/assets/texts/de.txt", "r", encoding="utf-8") as file:
        de_text = file.read()
    with open("lab_1_classify_profile/assets/texts/unknown.txt", "r", encoding="utf-8") as file:
        unknown_text = file.read()
    with open("lab_1_classify_profile/assets/stopwords.txt", "r", encoding="utf-8") as file:
        stopwords = file.read().split("\n")
    with open("lab_1_classify_profile/assets/texts/en.txt", "r", encoding="utf-8") as file:
        en_text = file.read()

    # demonstration of getting top-7 words
    tokens = tokenize(de_text)
    filtered_tokens = remove_stop_words(tokens, stopwords)
    freq_dict = calculate_frequencies(filtered_tokens)
    top_7_words = get_top_n_words(freq_dict, 7)

    print(top_7_words)

    # creating language profiles
    en_profile = create_language_profile("en", en_text, stopwords)
    de_profile = create_language_profile("de", de_text, stopwords)
    unknown_profile = create_language_profile("unknown", unknown_text, stopwords)

    # detection with top-15
    result = detect_language_by_top_n(
    unknown_profile,
    en_profile,
    de_profile,
    15,
    )
    print(result)

    # detection with mse
    result_mse = detect_language_by_mse(
    unknown_profile,
    en_profile,
    de_profile,
    )
    print(result_mse)



