import pytest

from german_regular_plural import get_german_regular_plural

regular_plurals = '''
    # masculine => umlaut+e
    der Freund Freunde
    der Tisch  Tische
    der Ball   Bälle
    der Stuhl  Stühle

    # masculine ends with ENT ONT ON => +en
    der Student Studenten
    der Tourist Touristen
    der Person  Personen

    # masculine or neuter ending with EL EN ER => just umlaut
    der Lehrer Lehrer
    der Apfel  Äpfel
    das Messer Messer
    der Löffel Löffel
    das Käufer Käufer
    # (that would be the regular form, although it's wrong)
    der Arm    Ärme

    # but that doesn not work for feminine nouns
    # (that would be the regular form, although it's wrong)
    die Gabel Gabelen

    # everything ending in e => +en
    die Familie Familien
    der Junge   Jungen

    # feminine => +en
    die Freundschaft Freundschaften
    die Nation       Nationen

    # but feminine ending with in => +nen
    die Lehrerin     Lehrerinnen
    die Amerikanerin Amerikanerinnen

    # feminine one syllable => umlaut + e
    die Hand  Hände
    die Stadt Städte
    die Maus  Mäuse
    # (that would be the regular form, although it's wrong)
    die Frau  Fräue
'''

regular_plurals = [
    r.split() for r in regular_plurals.strip().splitlines()
    if r and not r.strip().startswith('#')]


@pytest.mark.parametrize('article,german,plural', regular_plurals)
def test_regular_plurals(article, german, plural):
    assert get_german_regular_plural(article, german) == plural
