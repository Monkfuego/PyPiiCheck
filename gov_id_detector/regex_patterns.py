# gov_id_detector/regex_patterns.py

import re

ID_PATTERNS = {
    'SSN': re.compile(r'\b\d{3}-\d{2}-\d{4}\b'),
    'Passport': re.compile(r'\b[A-Z0-9]{6,9}\b'),
    'DriverLicense': re.compile(r'\b[A-Z0-9]{5,12}\b'),
    # Additional patterns as needed
}
