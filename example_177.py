# I want to make an Anki deck for all the plants from IPS-177 Fennoscandian flora
# The URL is https://pinkka.laji.fi/pinkat/#/pinkkas/7
# So, the ID needed is "7". Get a list of species IDs:
import pinkka2anki as p2a
species_ids = p2a.get_all_species_ids(7)


# Now I will create an Anki deck with this
# (Only do the first 20 for speed)
p2a.create_anki_deck(species_ids[0:20], 
                    pinkka_name = '177')

# Now just import this .apkg file into Anki