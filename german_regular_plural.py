import re

UMLAUTS = {'a': 'ä', 'o': 'ö', 'u': 'ü', 'au': 'äu'}

# "eu" should NOT get an umlaut (e.g. Freund)
RE_NO_UMLAUT_EU = re.compile('^.*eu[^aou]*$')
# special umlaut case au => äu (not aü)
RE_UMLAUT_AU = re.compile('^(.*)(au)([^aou]*)$')
# general umlaut case
RE_UMLAUT = re.compile('^(.*)([aou])([^aou]*)$')


def with_umlaut(word):
    word = word.lower()
    # if the word already has an umlaut, we're done
    if any(u in word for u in UMLAUTS.values()):
        return word.capitalize()

    umlauted = word
    if not RE_NO_UMLAUT_EU.match(word):
        for regex in (RE_UMLAUT_AU, RE_UMLAUT):
            match = regex.match(word)
            if match:
                start, to_umlaut, end = match.groups()
                umlauted = ''.join([start, UMLAUTS[to_umlaut], end])
                break
    return umlauted.capitalize()


RE_ENDS_WITH_ENT_IST_ON = re.compile('^.*(ent|ist|on)$')
RE_ENDS_WITH_EL_EN_ER = re.compile('^(.*)(el|en|er)$')
RE_HAS_ONE_SYLLABLE = re.compile('^[^aeiou]*[aeiou]+[^aeiou]*$')


def get_german_regular_plural(article, word):
    """
    Returns the expected regular plural of a german noun
    """
    if word.endswith('e'):
        return word + 'n'
    if article == 'die' and word.endswith('in'):
        return word + 'nen'
    if article == 'die' and RE_HAS_ONE_SYLLABLE.match(word):
        return with_umlaut(word + 'e')
    if article == 'die' or \
            (article == 'der' and RE_ENDS_WITH_ENT_IST_ON.match(word)):
        return word + 'en'
    if article in {'der', 'das'}:
        if RE_ENDS_WITH_EL_EN_ER.match(word):
            plural = word
        else:
            plural = word + 'e'
        return with_umlaut(plural)
