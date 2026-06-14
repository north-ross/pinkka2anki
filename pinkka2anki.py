import time
import json
from pathlib import Path
import requests
from genanki import Deck, Note, Model, Package

BASE_URL = "https://fmnh-ws-prod3.it.helsinki.fi/pinkka/api"

def get_all_species_ids(pinkka_id):
    """Fetch all species IDs from a pinkka and its subPinkkas"""
    
    # Get the list of sub pinkkas
    pinkka_response = requests.get(f"{BASE_URL}/pinkkas/{pinkka_id}", timeout=120)
    pinkka_data = pinkka_response.json()
    
    sub_pinkkas = pinkka_data.get('subPinkkas', [])
    print(f"Found {len(sub_pinkkas)} subPinkkas")
    
    all_taxon_ids = []
    
    # Step 2: Loop through each subPinkka
    for sub_pinkka in sub_pinkkas:
        sub_id = sub_pinkka['id']
        sub_name = sub_pinkka['name'].get('en', sub_pinkka['name'].get('fi', 'Unknown'))
        
        # Step 3: Get species from this subPinkka
        sub_response = requests.get(f"{BASE_URL}/subpinkkas/{sub_id}", timeout=120)
        sub_data = sub_response.json()

        # Extract species/taxon IDs (adjust key name based on actual JSON structure)
        species_in_sub = sub_data.get('speciesCards', [])  # or 'species', 'cards', etc.
        taxon_ids = [s['id'] for s in species_in_sub]

        print(f"  {sub_name}: {len(taxon_ids)} species")
        all_taxon_ids.extend(taxon_ids)

    print(f"\nTotal species across all subPinkkas: {len(all_taxon_ids)}")
    return all_taxon_ids

# Create Anki model (front: image, back: species name)
model_id = 1234567890
MODEL = Model(
    model_id,
    'Pinkka Species',
    fields=[
        {'name': 'Image', 'sticky': False},
        {'name': 'Species Name', 'sticky': False},
        {'name': 'Family', 'sticky': False},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Image}}',
            'afmt': '{{FrontSide}}<hr id="answer"><i>{{Species Name}}</i><br><b>{{Family}}</b>',
        },
    ]
)

def fetch_species_data(species_id):
    """Fetch species card data from API"""
    try:
        response = requests.get(f"{BASE_URL}/speciescards/{species_id}", timeout=100)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching species {species_id}: {e}")
        return None

def download_image(image_url, species_id, i):
    """_summary_

    Args:
        image_url (_type_): _description_
        species_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Create media folder
        media_dir = Path("pinkka_media")
        media_dir.mkdir(exist_ok=True)
        
        # Save image
        filename = f"species_{species_id}_{i}.jpg"
        filepath = media_dir / filename
        
        with open(filepath, 'wb') as f:
            f.write(response.content)
        return filepath
    except Exception as e:
        print(f"Error downloading image for {species_id}: {e}")
        return None


def create_anki_deck(species_list, images_number=3, lang='en', pinkka_name = '177'):
    """Creates an Anki package (.apkg) from a provided list of species IDs. 
        Downloads the specified number of images. 

    Args:
        species_list (list): List of species IDs from the Pinkka API. 
            Get using pinkka2anki.get_all_species_ids().
        images_number (int, optional): Number of images to download and include in the card. 
            Choose 100 for maximum (will not cause error). Defaults to 2.
        lang (str, optional): Language used for taxonomy tags (fi, sv or en). Defaults to 'en'.
        pinkka_name (str, optional): Language used for taxonomy tags (fi, sv or en). Defaults to 'en'.
    """
    deck_id = int(time.time() * 1000)  # Unique deck ID safe for SQLite integer
    deck = Deck(deck_id, f'Pinkka {pinkka_name} Species')
    media_list = []
    
    for species_id in species_list:
        data = fetch_species_data(species_id)
        print(f"got data for {species_id} ({data.get('scientificName')})")
        if not data:
            print(f"Could not find species {species_id}")
            continue
        
        # Extract species name, image URLs, taxonomy info
        species_name = data.get('scientificName')
        taxonomy_list = []
        family = ""
        for taxa in data.get('taxonomy'):
            taxatag = f"{taxa['rankName'][lang]}-{taxa['scientificName']}"
            taxatag = taxatag.replace(" ", "_")
            taxonomy_list.append(taxatag)
            if taxa['rankName']['en'] == "family":
                family = taxa['scientificName']
            
        # If user requested more images than exist, limit to existing number
        if images_number > len(data.get('images')):
            images_number = len(data.get('images'))
        
        # loop over images and download
        img_field = ""
        for i in range(0, images_number):
            image_url = data.get('images')[i]['urls']['square']
            image_path = download_image(image_url, species_id, i)
            # add path to media list
            media_list.append(image_path)

            # format for field
            img_field = f"{img_field} <img src=\"{image_path.name}\">"

        # Create Anki note
        note = Note(
            model=MODEL,
            fields=[img_field, species_name, family],
            tags=taxonomy_list
        )
        deck.add_note(note)

    # pack to package with media
    package = Package(deck)
    package.media_files = media_list
    # Save deck
    package.write_to_file(f'pinkka_{pinkka_name}_species.apkg')
    print(f"Anki deck created: pinkka_{pinkka_name}_species.apkg")
