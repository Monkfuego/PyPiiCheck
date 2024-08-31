# gov_id_detector/detector.py

from regex_patterns import ID_PATTERNS

def detect_ids(text):
    critical_alerts = {}
    lesser_critical_alerts = {}

    for id_type, pattern in ID_PATTERNS.items():
        matches = pattern.findall(text)
        if matches:
            if id_type in ['Aadhar Card', 'Pan Card', 'Passport', 'DriverLicense', 'GSTIN', 
                           'NREGA Job Card', 'IFSC', 'VoterId_India', 'NPS_PRAN', 'CreditCard', 'CVV']:
                critical_alerts[id_type] = matches
            else:
                lesser_critical_alerts[id_type] = matches

    if critical_alerts:
        print("Critical Alerts Detected:")
        for id_type, matches in critical_alerts.items():
            print(f"{id_type}: {matches}")
    elif lesser_critical_alerts:
        print("\nLesser Critical Alerts Detected:")
        for id_type, matches in lesser_critical_alerts.items():
            print(f"{id_type}: {matches}")
    else:
        print("No Alerts Detected")
