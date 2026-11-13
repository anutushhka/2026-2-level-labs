"""
Generation by NGrams starter
"""

# pylint:disable=too-many-locals, unused-import, unused-variable

from main import TextProcessor


def main() -> None:
    """
    Launches an implementation.

    In any case returns, None is returned
    """
    with open(
        "./lab_3_generate_by_ngrams/assets/Harry_Potter.txt", "r", encoding="utf-8"
    ) as text_file:
        text = text_file.read()

    text_processor = TextProcessor("_")

    tokens = text_processor._tokenize(text)
    assert tokens is not None

    encoded_corpus = text_processor.encode(text)
    assert encoded_corpus is not None

    decoded_text = text_processor.decode(encoded_corpus)
    assert decoded_text is not None

    print("Tokens:", tokens[:30])
    print("Encoded corpus:", encoded_corpus[:30])
    print("Decoded text:", decoded_text[:200])


if __name__ == "__main__":
    main()
