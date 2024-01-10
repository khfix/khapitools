import os

import imagehash
from PIL import Image


def find_best_similar_photo(input_photo_path, folder_path):
    input_hash = imagehash.average_hash(Image.open(input_photo_path))

    best_match_path = None
    best_match_difference = float("inf")

    for filename in os.listdir(folder_path):
        if filename.endswith((".jpg", ".png", ".jpeg")):
            photo_path = os.path.join(folder_path, filename)
            hash_value = imagehash.average_hash(Image.open(photo_path))

            difference = input_hash - hash_value

            if difference < best_match_difference:
                best_match_difference = difference
                best_match_path = photo_path

    if best_match_difference is not 0:
        return None
    else:
        return best_match_path
