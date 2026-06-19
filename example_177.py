# I want to make an Anki deck for all the plants from IPS-154 Subarctic Habitats and Biota
# The URL is https://pinkka.laji.fi/pinkat/#/pinkkas/68
# So, the ID needed is "68". Get a list of species IDs:
import pinkka2anki as p2a
species_ids = p2a.get_all_species_ids(68)

# Now I will create an Anki deck with this
p2a.create_anki_deck(species_ids,
        # Choose max number of images to download. Most plants have 10 images total. It will get half from the beginning and half from the end of the list.
        # Increasing will mean larger file size. I picked the first and last two (four total).
        req_images_number=4, 

        # Pick image resolution from this list: 
        # "original" > "full" > "large" > "square" > "thumbnail".
        image_size="square", 

        lang='en', # Set language for taxonomy names ('fi', 'sv', or 'en')
        pinkka_name = 'IPS-154 Subarctic Habitats and Biota', # Name of the deck and output file
        make_subdecks=True
        )

# After running, import this .apkg file into Anki