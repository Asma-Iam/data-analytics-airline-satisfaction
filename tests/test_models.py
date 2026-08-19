from nbresult import ChallengeResultTestCase


class TestModels(ChallengeResultTestCase):

    def test_logistic_regression_trained(self):
        """Trained Logistic Regression model"""
        self.assertTrue(
            self.result.lr_trained,
            "Hint: Train the Logistic Regression model with .fit(X_train_preprocessed, y_train)")

    def test_random_forest_trained(self):
        """Trained Random Forest model"""
        self.assertTrue(
            self.result.rf_trained,
            "Hint: Create and train a RandomForestClassifier called 'forest_model'")

    def test_models_have_accuracy(self):
        """Both models achieve reasonable accuracy"""
        self.assertGreater(
            self.result.lr_accuracy,
            0.8,
            "Hint: Logistic Regression accuracy seems low - check your preprocessing steps")
        self.assertGreater(
            self.result.rf_accuracy,
            0.9,
            "Hint: Random Forest should achieve ~96% accuracy - verify your model is trained correctly")

    def test_lr_accuracy_not_suspiciously_perfect(self):
        """Check LR accuracy isn't suspiciously high (might indicate evaluation on training data)"""
        lr_acc = self.result.lr_accuracy
        self.assertLess(
            lr_acc,
            0.99,
            f"Logistic Regression accuracy is suspiciously high ({lr_acc:.1%}). Did you accidentally evaluate on the training data? "
            "Expected accuracy is around 87-89% on test data.")

    def test_rf_accuracy_not_suspiciously_perfect(self):
        """Check RF accuracy isn't suspiciously high (might indicate evaluation on training data)"""
        rf_acc = self.result.rf_accuracy
        self.assertLess(
            rf_acc,
            0.995,
            f"Random Forest accuracy is suspiciously high ({rf_acc:.1%}). Did you accidentally evaluate on the training data? "
            "Expected accuracy is around 95-97% on test data.")
