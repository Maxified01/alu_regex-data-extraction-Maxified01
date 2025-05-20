import re

def extract_data(text):
    data = {
        'emails': [],
        'urls': [],
        'phone_numbers': [],
        'credit_cards': [],
        'times': [],
    }

    # Extract email addresses (supports subdomains and standard formats)
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    data['emails'] = re.findall(email_regex, text, re.IGNORECASE)

    # Extract URLs (case-insensitive and supports domains like cryptoWrld.com)
    url_regex = r'https?://(?:www\.)?[A-Za-z0-9-]+(?:\.[A-Za-z-]+)+(?:[/?][^\s]*)?'
    data['urls'] = re.findall(url_regex, text, re.IGNORECASE)

    # Extract phone numbers with optional country codes and various separators
    phone_regex = r'\+\d{1,3}[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    data['phone_numbers'] = re.findall(phone_regex, text)

    # Extract credit card numbers (supports hyphens or spaces between groups)
    cc_regex = r'\b(?:\d{4}[ -]?){3}\d{4}\b'
    data['credit_cards'] = re.findall(cc_regex, text)

    # Extract time (24-hour and 12-hour formats with single-digit support)
    time_24 = r'(?:0?[0-9]|1[0-9]|2[0-3]):[0-5]\d'  # 9:50 or 09:50
    time_12 = r'(?:1[0-2]|0?[1-9]):[0-5]\d\s?[APap][Mm]'  # 2:30 PM
    time_regex = rf'\b(?:{time_24}|{time_12})\b'
    data['times'] = re.findall(time_regex, text)

    return data

# Sample test
sample_text = """
Email: a.emoh@alu.student.com, 
URL: https://www.cryptoWrld.com, 
Phone numbers: +2348124559142, +1202-555-0181, 
Credit Card: 4567-8910-1112-1356, 
Time: 9:50
"""

result = extract_data(sample_text)
print(result)