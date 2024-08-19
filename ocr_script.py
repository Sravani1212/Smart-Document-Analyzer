import io
import os
from google.cloud import vision
from google.oauth2 import service_account
import re

# Authenticate with the Google Vision API
def authenticate_google_vision(key_path):
    credentials = service_account.Credentials.from_service_account_file(key_path)
    client = vision.ImageAnnotatorClient(credentials=credentials)
    return client

# Load image into memory
def load_image(image_path):
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
    return vision.Image(content=content)

# Extract text from the image using Google Cloud Vision
def extract_text(client, image):
    response = client.text_detection(image=image)
    texts = response.text_annotations
    full_text = texts[0].description if texts else ''
    return full_text

# Parse specific data from extracted text
def parse_data(text):
    data = {
        'Name': None,
        'Sex': None,
        'Date of Birth': None,
        'License Number': None,
        'Aadhar Number': None,
        'Passport Number': None
    }
    
    # Patterns to find the data with and without explicit labels
    patterns = {
        'Name': re.compile(r"(?:Name|First Name|Surname|Last Name)[\s:]((?:[A-Za-z]+\.?)(?:\s+[A-Za-z]+\.?))"),
        'Sex': re.compile(r'\b(M|F|Male|Female)\b'),
        'Date of Birth': re.compile(r'(?:DOB|Date of Birth)\s*:?[\s\n]*?(\d{2}/\d{2}/\d{4})'),
        'License Number': re.compile(r'(?i)DL\s*NO\.?\s*:?([A-Za-z0-9]{1,13})'),
        'Aadhar Number': re.compile(r'\b\d{4}\s\d{4}\s\d{4}\b'),
        'Passport Number': re.compile(r'Passport No\.?\s*([A-Z][0-9]{7})')
    }
    
    # Match each pattern in the text
    for key, pattern in patterns.items():
        match = pattern.search(text, re.IGNORECASE)
        if match:
            data[key] = match.group(1).strip()  # Extract and use the captured group directly

    return data

# Process all images in a directory
def process_directory(directory_path, key_path):
    client = authenticate_google_vision(key_path)
    results = []

    # List all image files in the directory
    for filename in os.listdir(directory_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(directory_path, filename)
            image = load_image(image_path)
            extracted_text = extract_text(client, image)
            data = parse_data(extracted_text)
            results.append(data)
            print(f"Processed {filename}: {data}")

    return results

# Example usage
if __name__ == "__main__":
    key_path = 'creds.json'
    directory_path = 'examples/'
    all_data = process_directory(directory_path, key_path)
    #print(all_data)