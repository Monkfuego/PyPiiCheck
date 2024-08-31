import sys
from .file_handler import extract_text, extract_image_from_file
from .detector import detect_ids

def main():
    if len(sys.argv) != 2:
        print("Usage: python -m gov_id_detector <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    templates = {
        'Aadhar Card': 'templates/aadhar_template.jpg',
        'Pan Card': 'templates/pan_template.jpg',
        # Add more templates here
    }
    
    try:
        text = extract_text(file_path)
        image_path = extract_image_from_file(file_path)  # Extract or provide the image for template matching
        
        detected_ids = detect_ids(text, image_path, templates)
        
        if detected_ids:
            print("Detected IDs:")
            for id_type, ids in detected_ids.items():
                print(f"{id_type}: {', '.join(ids)}")
        else:
            print("No IDs detected.")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
