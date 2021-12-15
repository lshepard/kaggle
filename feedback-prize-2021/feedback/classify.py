


# Constants
class SentenceClassifier():

    """This handles generating and submitting the actual test set for kaggle.
    Used for any particular notebook."""

    def __init__(self, root_dir):
        self.TRAIN_CSV = root_dir + "/train.csv"
        self.SUBMISSION_CSV = root_dir + "/sample_submission.csv"
        self.TRAIN_PATH = root_dir + "/train/"
        self.TEST_PATH = root_dir + "/test/"

    def create_submission(self):
        """Generates a submission"""
        pass
    
