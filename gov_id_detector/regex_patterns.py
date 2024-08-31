# gov_id_detector/regex_patterns.py

import re

import re

ID_PATTERNS = {
    # Indian Documents and Identification Numbers
    'Aadhar Card': re.compile(r'\b\d{4}\s\d{4}\s\d{4}\b'),
    'Pan Card': re.compile(r'\b[A-Z]{5}[0-9]{4}[A-Z]\b'),
    'DriverLicense': re.compile(r'\b[A-Z]{2}\d{2}\s\d{11}\b'),
    'GSTIN': re.compile(r'\b\d{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[A-Z0-9]{3}\b'),
    'NREGA Job Card': re.compile(r'\b\d{2}\s\d{4}\s\d{4}\s\d{4}\b'),
    'PhoneNumber_India': re.compile(r'\b(\+91[\-\s]?)?[6789]\d{9}\b'),
    'Email': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
    'BankAccount_India': re.compile(r'\b\d{9,18}\b'),
    'CreditCard': re.compile(r'\b(?:\d{4}[-\s]?){3}\d{4}\b'),
    'DOB': re.compile(r'\b\d{2}/\d{2}/\d{4}\b'),
    'IPv4': re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b'),
    'IPv6': re.compile(r'\b([0-9a-fA-F]{1,4}:){7}([0-9a-fA-F]{1,4}|:)\b'),
    'IFSC': re.compile(r'\b[A-Z]{4}0[A-Z0-9]{6}\b'),
    'Passport_India': re.compile(r'\b[A-Z]{1}[0-9]{7}\b'),
    'VehicleRegistration_India': re.compile(r'\b[A-Z]{2}[0-9]{2}[A-Z]{1,2}\d{4}\b'),
    'EPFO': re.compile(r'\b[A-Z]{2}/\d{5}/\d{7}\b'), 
    'VoterId_India': re.compile(r'\b[A-Z]{3}[0-9]{7}\b'),  
    'NPS_PRAN': re.compile(r'\b\d{12}\b'),
}
