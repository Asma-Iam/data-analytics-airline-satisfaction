from nbresult import ChallengeResultTestCase


class TestPreprocessing(ChallengeResultTestCase):

    def test_target_encoded(self):
        """Created airline_target variable"""
        self.assertIsNotNone(
            self.result.target_exists,
            "Hint: Create 'airline_target' by encoding the 'satisfaction' column")

    def test_train_test_split(self):
        """Split data into train and test sets"""
        self.assertGreater(
            self.result.train_size,
            0,
            "Hint: Use train_test_split to create X_train and X_test")
        self.assertGreater(
            self.result.test_size,
            0,
            "Hint: Check that y_train and y_test were created from the split")

    def test_preprocessed_created(self):
        """Created X_train_preprocessed and X_test_preprocessed"""
        self.assertGreater(
            self.result.train_features,
            0,
            "Hint: Combine scaled numerical and encoded categorical features into X_train_preprocessed")
        self.assertGreater(
            self.result.test_features,
            0,
            "Hint: Don't forget to create X_test_preprocessed with the same transformations")
