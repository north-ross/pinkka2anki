# pinkka2anki
A python module to convert plant image collections from [Pinkka](https://pinkka.laji.fi) to an Anki deck. Pinkka is a platform used by the University of Helsinki (and other Finnish organizations) for plant identification lessons. This set of functions can be used to collect data from Pinkka's API and convert them into Anki flashcards. Specifically it's useful for students who need to memorize latin names before a test.

If you just want to download the IPS-154 deck, follow [this link](https://github.com/north-ross/pinkka2anki/blob/main/pinkka_IPS-154_Subarctic_Habitats_and_Biota.apkg) and choose "download raw file" in the top right.

I have been studying Finnish plants using Pinkka, but I thought it would be useful to have the spaced repetition from Anki, plus the ability to study one family at a time.

Unfortunately, I couldn't get it to work using the image URLs, so it needs to download all the images. I used the medium-size "square" resolution as deafault, but the script can be configured to use "thumbnail" instead. For reference, four "square"-size images for 652 species resulted in a 80 MB Anki package.

The repository also includes one of the decks for IPS-177 in 2026 (pinkka_IPS-177_species.apkg).

# Dependencies
- Python 3.4+
- `requests` (`pip install requests`)
- [GenAnki](https://github.com/kerrickstaley/genanki) (`pip install genanki`)

# Use
1. Choose your class Pinkka from this list: [https://pinkka.laji.fi/pinkat/#/pinkkas/](https://pinkka.laji.fi/pinkat/#/pinkkas/). At the end of the URL there is a number. For example, for IPS-177 Fennoscandian Flora https://pinkka.laji.fi/pinkat/#/pinkkas/7 the number is 7.
2. Install the required dependencies and clone this repository on your PC
3. Using the "example_177.py" as a template, use the number from your desired Pinkka collection to get a species ID list, then convert this to an Anki deck. You can set other options, like the language of tags used for taxonomy or the number of images to include. If desired, you can also make sub-decks based on the "sub-pinkkas" from your collection.

# Notes
The Anki deck that is created will have your desired number of images on the front of the flashcard, then the given scientific name, family and Finnish name on the back. You can customize the cards once you add them to Anki.

It also has the subpinkka, family and phylum as tags. Use the [Custom Study](https://docs.ankiweb.net/filtered-decks.html?highlight=filtered%20deck#custom-study) feature with certain tags, for example "family-Asteraceae" or "phylum-Tracheophyta".

You can sync to your Anki account and use the app to study on your phone. It's free on Android but the iOS app is a bit expensive.

If you have found this useful this consider donating to the free and open source software [Anki](https://apps.ankiweb.net/).

Disclaimer: Some code advice came from [duck.ai](https://duck.ai) (Claude Haiku 4.5).
