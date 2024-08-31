from file_handler import extract_text
from detector import detect_ids

file_path = "/home/josephremingston/code/Hackathon/gov_id_detector/Adhr_crdSubro.pdf"

text = extract_text(file_path)
detect_ids(text)
