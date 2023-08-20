import unittest
from unittest.mock import Mock, patch
import weather_tracker.py

class TestWeatherScript(unittest.TestCase):
    @patch('requests.get')
    def test_weather_report(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {
            'location': {
                'name': 'Boston',
                'region': 'Lincolnshire',
            },
            'current': {
                'temp_c': 15.0,
                'wind_mph': 4.3,
                'wind_dir': 'WSW',
                'humidity': 82,
                'condition': {
                    'text': 'Sunny',
                },
                'feelslike_c': 14.2,
            }
        }

        mock_get.return_value = mock_response

        report = your_script.get_weather_report()
        expected_report = "Good morning Boston! Today in Lincolnshire, the weather is Sunny. The temperature is currently 15.0 degrees Celsius, but it feels like 14.2 degrees. The wind is coming from the WSW at 4.3 miles per hour. The humidity level is at 82 percent."

        self.assertEqual(report, expected_report)

if __name__ == '__main__':
    unittest.main()
