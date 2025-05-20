# Alu_regex-data-extraction.

This project implements regular expressions to extract specific data types from text. The selected data types are emails, URLs, phone numbers, credit card numbers, and times (24-hour and 12-hour formats)

git clone git clone https://github.com/Maxified01/alu_regex-data-extraction-Maxified01.git

cd alu_regex-data-extraction-username

``

2. Install dependencies (Python 3 required)

```bash

pip install -r requirements.txt

```

## Usage

Import the `extract_data` function from `extract.py` and pass a string to it. The function returns a dictionary with the extracted data.

Example:

```python

from extract import extract_data

text = "Email: a.emoh@alu.student.com, URL: https://www.cryptoWrld.com , Phone: (+234, +1):['+2348124559142','+1202-555-0181'], Credit Cards:['4567-8910-1112-1356'], Hours: ['9:50'] 

result = extract_data(text)

print(result)

```

## Test

Run the tests with pytest:

```bash

pytest tests/

```

## Regex Patterns

- **Emails**: Standard email pattern with local-part and domain.

- **URLs**: URLs starting with http/https, with domains and optional paths.

- **Phone Numbers**: Supports various formats with different separators.

- **Credit Cards**: 16-digit numbers with optional hyphens or spaces.

- **Times**: Both 24-hour and 12-hour formats.

## Edge Cases Handled

- Email domains with multiple subdomains.

- URLs with query parameters.

- Phone numbers with mixed separators.

- Credit cards with varying separator characters.

- Time formats with/without leading zeros and AM/PM.

## Project Structure

- `extract.py`: Main module with extraction functions.

- `tests/`: Unit tests for each data type.

- `sample_inputs.txt`: Example text for testing.