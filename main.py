import os
import pandas as pd
from src.download_images import download_images_from_csv
from src.ocr_extraction import extract_text_from_image
from src.dimension_extraction import extract_dimensions
from src.entity_mapping import map_entities
from src.calculate_metrics import calculate_area, calculate_volume, format_weight
from src.generate_output import generate_predictions_csv

def main():
    # Step 1: Download images
    image_folder = "images"
    os.makedirs(image_folder, exist_ok=True)
    download_images_from_csv("dataset/sample_test.csv", image_folder)

    # Step 2: Extract text from images
    predictions = []
    df = pd.read_csv("dataset/sample_test.csv")
    
    for idx, row in df.iterrows():
        image_path = os.path.join(image_folder, f"image_{idx}.jpg")
        print(f"Processing image: {image_path}")
        if os.path.exists(image_path):
            text = extract_text_from_image(image_path)
            print(f"Extracted text from image {image_path}: {text}")

            # Step 3: Extract dimensions from text
            dimensions = extract_dimensions(text)
            print(f"Extracted dimensions from text: {dimensions}")

            # Step 4: Map dimensions to entities
            length, width, height, weight = map_entities(text, dimensions)
            print(f"Mapped entities: Length: {length}, Width: {width}, Height: {height}, Weight: {weight}")

            # Step 5: Calculate area or volume
            if length and width and height:
                volume, volume_unit = calculate_volume(length[0], width[0], height[0])
                prediction = f"{volume} {volume_unit}"
            elif width and height:
                area, area_unit = calculate_area(width[0], height[0])
                prediction = f"{area} {area_unit}"
            elif weight:
                prediction = format_weight(weight[0])
            else:
                prediction = "No valid dimensions found"

            predictions.append((row['index'], prediction))
        else:
            print(f"Image file not found: {image_path}")
    
    # Step 6: Generate output file
    generate_predictions_csv(predictions, "output/sample_test_out.csv")

if __name__ == "__main__":
    main()
