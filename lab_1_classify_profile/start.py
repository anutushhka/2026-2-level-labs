"""
Language detection starter.
"""

# pylint: disable=unused-variable, duplicate-code

from lab_1_classify_profile.main import (
    calculate_frequencies,
    create_language_profile,
    detect_language_by_mse,
    detect_language_by_top_n,
    get_top_n_words,
    remove_stop_words,
    tokenize,
)


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
    result = None

    # demonstration of getting top-7 words
    tokens = tokenize(de_text)
    filtered_tokens = None
    freq_dict = None

    if tokens is not None:
        filtered_tokens = remove_stop_words(tokens, stopwords)

    if filtered_tokens is not None:
        freq_dict = calculate_frequencies(filtered_tokens)

    if freq_dict is not None:
        result = get_top_n_words(freq_dict, 7)
    print("Top-7 words:", result)

    # creating language profiles
    de_profile = create_language_profile("de", de_text, stopwords)
    en_profile = create_language_profile("en", en_text, stopwords)
    unknown_profile = create_language_profile("unknown", unknown_text, stopwords)

    # detection with top-15
    if de_profile is not None and en_profile is not None and unknown_profile is not None:
        result = detect_language_by_top_n(unknown_profile, en_profile, de_profile, 15)

    print("Language of the text:", result)

    assert result, "Detection result is None"

    # detection with mse
    if en_profile is not None and de_profile is not None and unknown_profile is not None:
        result_mse = detect_language_by_mse(
            unknown_profile,
            en_profile,
            de_profile,
        )
        print("Language of the text (MSE):", result_mse)


if __name__ == "__main__":
    main()
