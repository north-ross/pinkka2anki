# pinkka2anki
 A python package to convert plant image collections from pinkka.fi to an Anki deck.

I have been studying Finnish plants using Pinkka, but I thought it would be useful to have the spaced repetition from Anki, plus the ability to study one family at a time.

# Dependencies
- Python 3
- `requests` (`pip install requests`)
- [genanki](https://github.com/kerrickstaley/genanki) (`pip install genanki`)

# Use
1. Choose your class Pinkka from this list: [https://pinkka.laji.fi/pinkat/#/pinkkas/](https://pinkka.laji.fi/pinkat/#/pinkkas/). At the end of the URL there is a number. For example, for IPS-177 Fennoscandian Flora https://pinkka.laji.fi/pinkat/#/pinkkas/7 the number is 7.
2. Install the required dependencies and clone this repository on your PC
3. Using the "example_177.py" as a template, use the number from your desired Pinkka collection to get a species ID list, then convert this to an Anki deck. You can set other options, like the language of tags used for taxonomy or the number of images to include.

# Output
The Anki deck that is created will have your desired number of images on the front of the flashcard, then the given scientific name and family on the back. 

It also has the whole taxonomy as tags, so you can filter your deck to study one family or order at a time, for example.

You can import this on to your phone and use the Anki app to study. It's free on Android but the iOS app has a small fee.

If you have found this useful this consider donating to the free and open source software [Anki](https://apps.ankiweb.net/).