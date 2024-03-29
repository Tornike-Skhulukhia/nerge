"""
Todo:
    add most accurate new match_case, which
    will match only when we have possible quote-ending-phrase followed with
    name_surname in base form "სახელობითი ბრუნვა", or
    in second form, which indicates that this text is said/written
    by that person.
"""

"""
Todo:
    add case that matches these:

        "მოგიწოდებთ, მიმართეთ ნორვეგიის ნობელის კომიტეტს,
          განიხილოს წინადადება ვლადიმერ ზელენსკისთვის მშვიდობის დარგში ნობელის პრემიის მინიჭების თაობაზე!",
        - ამის შესახებ "მთავარი არხის" გენერალური დირექტორი ნიკა გვარამია წერს.
"""

import re
from collections import Counter
from string import punctuation
from uuid import uuid4

from . import SURNAMES
from .extract import extract_persons
from .util import normalize_surname

# maybe in the future we should normalize text -
# leave just one specific type on normal quote -" for
# full quotes and one quote - ' for inside quotes.
# this will change initial text more then currently,
# but it will remove the need of encode/decode parts

QUOTE_LIKE_CHARS = [
    '"',  # basic double quote
    "'",  # basic single quote
    "“",  # quote start sign
    "„",  # quote end sign
    "’’",  # WTF (What the function :) ?
    "’",  # WTF (What the function :) ?
    "”",  # from other site
    '"',  # other double quote
    ",,",  # other weirdness yohoo,
]

# because of quote in quotes replacement
for i in QUOTE_LIKE_CHARS:
    assert "-" not in i

QUOTE_ENDING_PHRASES = {
    "განაცხადა",
    "განგვიცხადა",
    "განუცხადა",
    "აცხადებს",
    "ამბობს",
    "ნათქვამია",
    "თქვა",
    "მითხრა",
    "უთხრა",
    "წერს",
    "მწერს",
    "ვკითხულობთ",
    "წერია",
    "იკითხა",
    "დაამატა",
    "მოიწერა",
    "იწერება",
    "ნახსენებია",
    "აღნიშნა",
    "აღნიშნულია",
    "აღნიშნავს",
    "მიმართა",
    "ეხმიანება",
}


_is_geo_letter_or_digit = lambda l: 4304 <= ord(l) <= 4336 or l.isdigit()


def _tokenize_text(
    raw_text,
):
    # leave georgian letters and replace all other symbol with space
    text = []
    for c in raw_text:
        # letter is georgian
        if _is_geo_letter_or_digit(c):
            text.append(c)
        else:
            text.append(" ")

    text = "".join(text)

    # rm more than 1 spaces between and get resulting list
    text = text.split()

    return text


def _get_normalized_surname_if_surname(word):
    normalized = normalize_surname(word)

    if normalized in SURNAMES:
        return normalized
    return False


def _encode_quotes_in_quotes(raw_text):
    """
    Sometimes we have texts like this:

    "შეგახსენებთ, რომ რუსეთი მთელი თავისი ისტორიის განმავლობაში არასდროს არავის
    დასხმია თავს( მტყუნის? :-) - ავტორის შენიშვნა). რუსეთი, რომელმაც ამდენი ომი გადაიტანა,
    უკანასკნელი ქვეყანაა ევროპაში, რომელსაც საერთოდ სიტყვა "ომის" წარმოთქმა სურს".

    Here we have a quote with quote inside of it, so our current basic
    splitting by possible quotes approach will fail and think that first quote ends when
    next quoted text starts (3-rd last word).

    To make important step towards fixing this problem, lets encode quotes
    in parts where main quote is not yet finished, with some random string,
    so that out splitting method will continue working as these words will not
    have valid quote-like strings. Of course we replace this encoded strings with
    their basic quotes form at the end.

    How to decide if specific quote is not the one that ends currently
    started quote? According to our observation, real quote endings most of the
    time happen without space between letter and quote mark, so if we have
    any quote-like character after space(not directly followed after word, without space)
    and are in a place where quoting started somewhere and not ended yet,
    we encode that quote mark and its ending pair.
    """

    text = []

    in_quoted_part = False
    encode_next_quote_char = False
    decoder = {}  # what encoded string replaces what quote mark

    for index, c in enumerate(raw_text):
        if c not in QUOTE_LIKE_CHARS:
            text.append(c)
            continue

        if encode_next_quote_char:
            encoded_char = str(uuid4())
            text.append(encoded_char)

            decoder[encoded_char] = c

            encode_next_quote_char = False
            continue

        if not in_quoted_part:
            in_quoted_part = True
            text.append(c)
        else:
            # quote does not end previous quote
            if (
                not _is_geo_letter_or_digit(raw_text[index - 1])
                and raw_text[index - 1] not in punctuation
            ):
                encode_next_quote_char = True

                encoded_char = str(uuid4())
                decoder[encoded_char] = c
                text.append(encoded_char)
            else:
                in_quoted_part = False
                text.append(c)

    text = "".join(text)

    return text, decoder


def _preprocess_text(text):
    # rm newlines
    text = re.sub("\n", " ", text)

    # rm double quotes with
    for i in QUOTE_LIKE_CHARS:
        text = text.replace(i * 2, '"')

    # rm multiple continuous spaces
    text = " ".join(text.split())

    return text


def _decode_result(result, quotes_decoder):
    # decode - will slow things a lot, but may be worth it, as
    # we do not want to change original text much, may optimize later...
    for i in result:
        for encoded_char, original_char in quotes_decoder.items():
            i["quote"] = i["quote"].replace(encoded_char, original_char)

    return result


def _deduplicate_result(result):
    deduplicated_result = []

    seen_person_and_quotes = set()

    for i in result:
        key = (i["person"], i["quote"])

        if key not in seen_person_and_quotes:
            seen_person_and_quotes.add(key)

            deduplicated_result.append(i)

    return deduplicated_result


def get_quotes(text, v=0):
    """
    extract quotes and persons who say that in given Georgian text.

    Before extraction from text starts, any newline and multiple
    continuous space characters are replaced with just one,
    no other normalization is done, like making sure quotes end with dots
    or something like that.

    result structure:
    [
        {
            "person": "person_1",
            "quote": "continuous_quote_1",
            "match_case": 1,
        },
        {
            "person": "person_2",
            "quote": "continuous_quote_2",
            "match_case": 2,
        },
        ...
    ]


    ------------------------------------------------------------------------
    result explanation:
    ------------------------------------------------------------------------
        each identified quote with person who said that, are in a separate
        dictionary with keys "person" and "quote" accordingly.

        match_case key denotes which method resulted this quote identification,
        their extraction logics are different and lower number means it is usually
        more realiable, so having this information can be useful to make decisions
        in our specific use case.

        From our testing, most of the time results with match_case < X(?)
        are good enough.

        ---------------------------------------------------------------------
            match_case explanation:
        ---------------------------------------------------------------------

                ----
                1.
                ----
                    "quote" -> quote_ending_string -> person_name_surname

                    ex:
                        "ტესტი", - განაცხადა გიორგი გიორგაძემ

                ----
                2.  person_name_surname: "quote"
                ----
                    ex:
                        გიორგი გიორგაძე: "ჩემთვის დიდი პატივია"

                ----
                3.
                ----
                    "quote" - quote_ending_string person_surname.
                    only one person was mentioned in full text with this surname

                    ex:
                        გიორგი გიორგაძე დღეს ილაპარაკებს.
                        "ვილაპარაკე", განაცხადა გიორგაძემ ჟურნალისტებთან.


    For example real input/outputs see test files/do your testing.
    """

    text = _preprocess_text(text)

    if v:
        print(f"preprocessed_text={text}")

    text, quotes_decoder = _encode_quotes_in_quotes(text)

    result = []
    parts_splitted_by_quote_chars = re.split("|".join(QUOTE_LIKE_CHARS), text)

    # { index_in_splitted_part: quote_text }
    quote_indices_and_texts = {}

    start_i = 1

    while start_i < len(parts_splitted_by_quote_chars):
        quote_indices_and_texts[start_i] = parts_splitted_by_quote_chars[
            start_i
        ]
        start_i += 2

    normalized_splitted_parts = [
        _tokenize_text(part) for part in parts_splitted_by_quote_chars
    ]

    # to skip for next match_cases
    already_matched_quotes_indices = set()

    text_to_extract_persons_from = " ".join(
        [
            i
            for index, i in enumerate(parts_splitted_by_quote_chars)
            if index not in quote_indices_and_texts
        ]
    )

    extracted_persons = extract_persons(text_to_extract_persons_from)

    if v:
        print(f"{text=}")
        print(f"{parts_splitted_by_quote_chars=}")
        print(f"{extracted_persons=}")
    ####################################################

    """
        case 1

        ex:
            "ტესტი", - განაცხადა გიორგი გიორგაძემ
    """
    for quote_index, quote_text in quote_indices_and_texts.items():

        if quote_index in already_matched_quotes_indices:
            continue

        try:
            tokens = normalized_splitted_parts[quote_index + 1]
        except IndexError:
            continue

        if len(tokens) < 3 or tokens[0] not in QUOTE_ENDING_PHRASES:
            continue

        # get max length of 4 name_surname combo if possible | ex: ურსულა ფონ დერ ლაიენი
        if len(tokens) >= 5:
            author_candidate = extract_persons(
                f"{tokens[1]} {tokens[2]} {tokens[3]} {tokens[4]}"
            )

            if (
                len(author_candidate) == 1
                and len(author_candidate[0].split()) == 4
            ):
                result.append(
                    {
                        "person": author_candidate[0],
                        "quote": quote_text,
                        "match_case": 1,
                    }
                )
                already_matched_quotes_indices.add(quote_index)
                continue

        # get max length of 3 name_surname combo if possible | ex: კიმ ჩენ ინი
        if len(tokens) >= 4:
            author_candidate = extract_persons(
                f"{tokens[1]} {tokens[2]} {tokens[3]}"
            )

            if (
                len(author_candidate) == 1
                and len(author_candidate[0].split()) == 3
            ):
                result.append(
                    {
                        "person": author_candidate[0],
                        "quote": quote_text,
                        "match_case": 1,
                    }
                )
                already_matched_quotes_indices.add(quote_index)
                continue

        # get max length of 2 name_surname combo if possible | ex: შარლ მიშელი
        author_candidate = extract_persons(f"{tokens[1]} {tokens[2]}")

        if author_candidate:
            result.append(
                {
                    "person": author_candidate[0],
                    "quote": quote_text,
                    "match_case": 1,
                }
            )
            already_matched_quotes_indices.add(quote_index)

    """
        case 2

        ex:
            გიორგი გიორგაძე: "ჩემთვის დიდი პატივია"
    """

    for quote_index, quote_text in quote_indices_and_texts.items():

        if quote_index in already_matched_quotes_indices:
            continue

        prev_text = parts_splitted_by_quote_chars[quote_index - 1]

        if not prev_text.strip().endswith(":"):
            continue

        _tokenized_prev_text = _tokenize_text(prev_text)

        if len(_tokenized_prev_text) < 2:
            continue

        # get max length of 4 name_surname combo if possible | ex: ურსულა ფონ დერ ლაიენი
        if len(_tokenized_prev_text) >= 4:
            here_should_be_person_mentioned = " ".join(
                _tokenized_prev_text[-4:]
            )

            author_candidate = extract_persons(here_should_be_person_mentioned)
            raw_part_author_candidates = extract_persons(
                prev_text, dont_deduplicate_or_sort_result=True
            )

            if (
                len(author_candidate) == 1
                and len(author_candidate[0].split()) == 4
            ):

                result.append(
                    {
                        "person": raw_part_author_candidates[-1],
                        "quote": quote_text,
                        "match_case": 2,
                    }
                )
                already_matched_quotes_indices.add(quote_index)
                continue

        # get max length of 3 name_surname combo if possible | ex: კიმ ჩენ ინი
        if len(_tokenized_prev_text) >= 3:
            here_should_be_person_mentioned = " ".join(
                _tokenized_prev_text[-3:]
            )

            author_candidate = extract_persons(here_should_be_person_mentioned)
            raw_part_author_candidates = extract_persons(
                prev_text, dont_deduplicate_or_sort_result=True
            )

            if (
                len(author_candidate) == 1
                and len(author_candidate[0].split()) == 3
            ):
                result.append(
                    {
                        "person": raw_part_author_candidates[-1],
                        "quote": quote_text,
                        "match_case": 2,
                    }
                )
                already_matched_quotes_indices.add(quote_index)
                continue

        # get max length of 2 name_surname combo if possible | ex: გიორგი გიორგაძე
        here_should_be_person_mentioned = " ".join(_tokenized_prev_text[-2:])

        author_candidate = extract_persons(here_should_be_person_mentioned)

        if author_candidate:
            result.append(
                {
                    "person": author_candidate[0],
                    "quote": quote_text,
                    "match_case": 2,
                }
            )
            already_matched_quotes_indices.add(quote_index)

    """
    case 3

    ex:
        გიორგი გიორგაძე დღეს ილაპარაკებს.
        "ვილაპარაკე", განაცხადა გიორგაძემ ჟურნალისტებთან.

    """
    if len(extracted_persons) > 0:

        extracted_surnames_counter = Counter(
            [i.split()[-1] for i in extracted_persons]
        )

        if v:
            print(f"{extracted_surnames_counter=}, {quote_indices_and_texts=}")

        for quote_index, quote_text in quote_indices_and_texts.items():

            if quote_index in already_matched_quotes_indices:
                continue

            try:
                tokens = normalized_splitted_parts[quote_index + 1]
            except IndexError:
                continue

            if len(tokens) < 2 or tokens[0] not in QUOTE_ENDING_PHRASES:
                continue

            possible_surname = _get_normalized_surname_if_surname(tokens[1])

            if (
                possible_surname
                and extracted_surnames_counter[possible_surname] == 1
            ):
                person = [
                    i
                    for i in extracted_persons
                    if i.split()[-1] == possible_surname
                ][0]

                result.append(
                    {
                        "person": person,
                        "quote": quote_text,
                        "match_case": 3,
                    }
                )
                already_matched_quotes_indices.add(quote_index)

    result = _decode_result(result, quotes_decoder)
    result = _deduplicate_result(result)

    return result
