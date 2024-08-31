# gov_id_detector/regex_patterns.py

import re

ID_PATTERNS = {
    'SSN': re.compile(r'\b\d{3}-\d{2}-\d{4}\b'),
    'Passport': re.compile(r'\b[A-Z0-9]{6,9}\b'),
    'DriverLicense': re.compile(r'\b[A-Z0-9]{5,12}\b'),
    "Aadhar Card" : re.compile(r'\b\d{4}\s\d{4}\s\d{4}\b'),
    "Pan Card" : re.compile(r'\b[A-Z]{5}[0-9]{4}[A-Z]\b'),
    "Voter Id" : re.compile(r'\b[A-Z]{1,2}[0-9]{7}\b'),
    "GSTIN" : re.compile(r'\b[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[A-Z0-9]{3}\b'),
    "NREGA JOB CARD" : re.compile(r'\b\d{2}\s\d{4}\s\d{4}\s\d{4}\b')
}
