import pandas as pd

def generate_predictions_csv(predictions, output_file):
    """Generates the output CSV file in the required format."""
    df = pd.DataFrame(predictions, columns=["index", "prediction"])
    df.to_csv(output_file, index=False)
    print(f"Predictions saved to {output_file}")
