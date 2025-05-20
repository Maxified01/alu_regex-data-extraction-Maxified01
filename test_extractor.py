import unittest
from data_extractor import extract_data

class TestDataExtractor(unittest.TestCase):
    def setUp(self):
        self.sample_text = """
        Email: a.emoh@alu.student.com, 
        URL: https://www.cryptoWrld.com, 
        Phone numbers: +2348124559142, +1202-555-0181, 
        Credit Card: 4567-8910-1112-1356, 
        Time: 9:50
        """
        self.result = extract_data(self.sample_text)

    def test_emails(self):
        expected = ["a.emoh@alu.student.com"]
        self.assertCountEqual(self.result["emails"], expected)

    def test_urls(self):
        expected = ["https://www.cryptoWrld.com"]
        self.assertCountEqual(self.result["urls"], expected)

    def test_phone_numbers(self):
        expected = ["+2348124559142", "+1202-555-0181"]
        self.assertCountEqual(self.result["phone_numbers"], expected)

    def test_credit_cards(self):
        expected = ["4567-8910-1112-1356"]
        self.assertCountEqual(self.result["credit_cards"], expected)

    def test_times(self):
        expected = ["9:50"]
        self.assertCountEqual(self.result["times"], expected)

if __name__ == "__main__":
    unittest.main()