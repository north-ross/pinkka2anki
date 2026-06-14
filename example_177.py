# I want to make an Anki deck for all the plants from IPS-177 Fennoscandian flora
# The URL is https://pinkka.laji.fi/pinkat/#/pinkkas/7
# So, the ID needed is "7". Get a list of species IDs:
import pinkka2anki as p2a
species_ids = p2a.get_all_species_ids(7)

# Now I will create an Anki deck with this
# (Only do the first 20 for speed)
p2a.create_anki_deck(species_ids,
        # Choose max number of images to download. Most plants have 10 images total. Increasing will mean larger file size. I picked the first 3.
        images_number=3, 

        # Pick image resolution from this list: "original" > "full" > "large" > "square" > "thumbnail".
        image_size="square", 

        lang='en', # Set language for taxonomy names ('fi', 'sv', or 'en')
        pinkka_name = 'IPS-177' # Name to include in the output files
        )

# After running, import this .apkg file into Anki