# gov_id_detector/detector.py

from regex_patterns import ID_PATTERNS

def detect_ids(text):
    detected_ids = {}
    for id_type, pattern in ID_PATTERNS.items():
        matches = pattern.findall(text)
        if matches:
            detected_ids[id_type] = matches 
            print(detected_ids)
    else:
        print("ids not detected")
