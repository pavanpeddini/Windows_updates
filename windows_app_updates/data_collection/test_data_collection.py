
import unittest
from data_collection import DataCollector

class TestDataCollection(unittest.TestCase):
    def setUp(self):
        self.data_collector = DataCollector()

    def test_fetch_historical_data(self):
        # Test fetch_historical_data function
        historical_data = self.data_collector.fetch_historical_data()
        self.assertIsNotNone(historical_data)
        self.assertIsInstance(historical_data, list)

    def test_process_data(self):
        # Test process_data function
        raw_data = [
        {"version": "Windows 1.0", "release_date": "November 1985", "description": "GUI Introduction"},
        {"version": "Windows 2.0", "release_date": "December 1987", "description": "Improved graphics"},
        {"version": "Windows 3.0", "release_date": "May 1990", "description": "Enhanced Performance"},
        {"version": "Windows 95", "release_date": "August 1995", "description": "Start menu Debut"},
        {"version": "Windows 98", "release_date": "June 1998", "description": "USB Support"},
        {"version": "Windows 2000", "release_date": "February 2000", "description": "Business Focus"},
        {"version": "Windows XP", "release_date": "October 2001", "description": "Stability Upgrade"},
        {"version": "Windows Vista", "release_date": "January 2007", "description": "Aero Glass "},
        {"version": "Windows 7", "release_date": "October 2009", "description": "Enhanced Usability"},
        {"version": "Windows 8", "release_date": "October 2012", "description": "Touch Optimization"},
        {"version": "Windows 10", "release_date": "July 2015", "description": "Unified Platform"},
        {"version": "Windows 11", "release_date": "Ocotber 2021", "description": "Modernized Interface"},
       
    ]
        processed_data = self.data_collector.process_data(raw_data)
        self.assertIsNotNone(processed_data)
        self.assertIsInstance(processed_data, dict)
        self.assertIn("Windows 1.0", processed_data)
        self.assertIsInstance(processed_data["Windows 1.0"], dict)
        self.assertIn("release_date", processed_data["Windows 1.0"])
        self.assertIn("description", processed_data["Windows 1.0"])

if __name__ == '__main__':
    unittest.main()
