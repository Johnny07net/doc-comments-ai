from tree_sitter_languages import get_language, get_parser

LANGUAGES = [
    'typescript',
    'tsx',

]
def test_get_parser():
    for language in LANGUAGES:
        parser = get_parser(language)
        assert parser


def test_get_language():
    for language in LANGUAGES:
        language = get_language(language)
        assert language

if __name__ == "__main__":
    test_get_language()
    