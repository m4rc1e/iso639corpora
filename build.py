"""
Generate a corpora from wikipedia articles for each language
which has iso639 codes.
"""
import wptools
from iso639 import languages
from models import db, Languages
import pycurl


def main():
    db.connect()
    db.create_tables([Languages])

    for language in languages.languages:

        if language.part1 != '':
            try:
                wp_page = wptools.page(lang=language.part1).get_query()
                wp_text = wp_page.extext
            except pycurl.error: # No wikipedia articles for this language
                wp_text = None
        else:
            wp_text = None

        Languages.create(
            name=language.name,
            part1=language.part1,
            part2=language.part2b,
            part3=language.part3,
            text=wp_text,
        )

    db.commit()


if __name__ == '__main__':
    main()
