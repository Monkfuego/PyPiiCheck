import cv2
import numpy as np

def match_template(image_path, template_path, threshold=0.8):
    image = cv2.imread(image_path, 0)
    template = cv2.imread(template_path, 0)
    
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)
    
    return max_val >= threshold

def detect_document_type(image_path, templates):
    for doc_type, template_path in templates.items():
        if match_template(image_path, template_path):
            return doc_type
    return None

def detect_ids(text, image_path, templates):
    detected_ids = {}
    document_type = detect_document_type(image_path, templates)
    
    if document_type:
        print(f"Document matched with: {document_type}")
        
        for id_type, pattern in ID_PATTERNS.items():
            matches = pattern.findall(text)
            if matches:
                if id_type in ['Aadhar Card', 'Pan Card', 'Passport', 'DriverLicense', 'GSTIN', 
                               'NREGA Job Card', 'IFSC', 'VoterId_India', 'NPS_PRAN', 'CreditCard']:
                    detected_ids[id_type] = matches
        
        return detected_ids
    else:
        print("No matching document template found.")
        return None
