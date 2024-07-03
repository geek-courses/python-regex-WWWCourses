import unittest
from regex_module import regex_functions

class TestRegexFunctions(unittest.TestCase):
    def test_anonymize_emails(self):
        self.assertEqual(regex_functions.anonymize_emails("Contact us at support@example.com"), "Contact us at [email]")
        self.assertEqual(regex_functions.anonymize_emails("Email me at john.doe123@example.org for details."), "Email me at [email] for details.")
        self.assertEqual(regex_functions.anonymize_emails("No emails in this string."), "No emails in this string.")

    def test_format_date(self):
        self.assertEqual(regex_functions.format_date("Event on 12/05/2023"), "Event on 2023-05-12")
        self.assertEqual(regex_functions.format_date("Due date is 31-12-2023"), "Due date is 2023-12-31")
        self.assertEqual(regex_functions.format_date("The date 2023.01.01 marks a new year."), "The date 2023-01-01 marks a new year.")

    def test_standardize_phone(self):
        self.assertEqual(regex_functions.standardize_phone("Call +1-123-456-7890 for assistance"), "Call (123) 456-7890 for assistance")
        self.assertEqual(regex_functions.standardize_phone("My number is 123.456.7890"), "My number is (123) 456-7890")
        self.assertEqual(regex_functions.standardize_phone("Emergency number: 1234567890"), "Emergency number: (123) 456-7890")

    def test_normalize_whitespace(self):
        self.assertEqual(regex_functions.normalize_whitespace("This  text   has  extra   spaces"), "This text has extra spaces")
        self.assertEqual(regex_functions.normalize_whitespace("Line with\nnew line character"), "Line with new line character")
        self.assertEqual(regex_functions.normalize_whitespace("Tab\tcharacter\ttest"), "Tab character test")

    def test_remove_html_tags(self):
        self.assertEqual(regex_functions.remove_html_tags("<p>Some <b>bold</b> text</p>"), "Some bold text")
        self.assertEqual(regex_functions.remove_html_tags("No <a href='link'>HTML</a> tags!"), "No HTML tags!")
        self.assertEqual(regex_functions.remove_html_tags("<div><span>Nested <i>tags</i></span></div>"), "Nested tags")

if __name__ == '__main__':
    unittest.main()
