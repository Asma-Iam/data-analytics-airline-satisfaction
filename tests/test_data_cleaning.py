from nbresult import ChallengeResultTestCase


class TestDataCleaning(ChallengeResultTestCase):

    def test_data_loaded(self):
        """Data loaded successfully"""
        self.assertGreater(
            self.result.n_rows,
            100000,
            "Hint: Check that the CSV loaded correctly from the URL")

    def test_columns_dropped(self):
        """Removed Unnamed: 0 and id columns"""
        self.assertFalse(
            self.result.has_unnamed,
            "Hint: Remove 'Unnamed: 0' column, it's just an index from Excel")
        self.assertFalse(
            self.result.has_id,
            "Hint: Remove 'id' column, it has no predictive power")

    def test_missing_values_filled(self):
        """Filled missing values"""
        self.assertEqual(
            self.result.missing_count,
            0,
            "Hint: Fill missing values in 'Arrival Delay in Minutes' with median")
