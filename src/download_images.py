import os
import requests
import pandas as pd
from tqdm import tqdm

def download_images_from_csv(csv_file, image_folder):
    # Load the CSV file
    df = pd.read_csv(csv_file)
    
    # Ensure image_folder exists
    os.makedirs(image_folder, exist_ok=True)

    # Iterate through the CSV file
    for index, row in tqdm(df.iterrows(), total=len(df)):
        # Get the image URL
        image_url = row.get('image_link')  # Ensure 'image_link' column is correctly named
        if pd.isna(image_url) or not image_url.strip():
            print(f"Row {index} is missing an image URL")
            continue

        # Set the image file name
        image_path = os.path.join(image_folder, f"image_{index}.jpg")

        try:
            # Attempt to download the image
            response = requests.get(image_url, stream=True)
            if response.status_code == 200:
                with open(image_path, 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                print(f"Downloaded: {image_path}")
            else:
                print(f"Failed to download image at {image_url}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error downloading image at {image_url}: {e}")
