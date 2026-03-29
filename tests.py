import unittest
from Sensor_Quality_Check import calculate_results


class TestSensorData(unittest.TestCase):

    def test_min_max(self):
        sample = [60, 80, 120, 100]

        min_v, max_v, _, _ = calculate_results(sample)

        self.assertEqual(min_v, 60)
        self.assertEqual(max_v, 120)

    def test_critical_values(self):
        sample = [95, 101, 150, 80]

        _, _, _, critical = calculate_results(sample)

        self.assertEqual(critical, 2)


if __name__ == "__main__":
    unittest.main()
