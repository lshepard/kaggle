import defopt
import numpy as np # linear algebra                                                                           
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)  

from sklearn.model_selection import train_test_split

import logging
import sys
logging.basicConfig(format="%(asctime)s - %(message)s", stream = sys.stdout, level = logging.INFO)
logger = logging.getLogger()


# Constants
class ClassifierTrainer():
    """This handles generating and submitting the actual test set for kaggle.
    Used for any particular notebook."""

    def __init__(self, input_dir, random_state):
        self.TRAIN_CSV = input_dir + "/train.csv"
        self.TRAIN_PATH = input_dir + "/train/"
        self.random_state = random_state
        
    def run_training(self):
        """Runs the training."""
        self.split_training_set()

    def split_training_set(self):
        """Splits the train into validation set for internal comparison"""
        raw_train_df = pd.read_csv(self.TRAIN_CSV)
        self.train, self.validation = train_test_split(raw_train_df, test_size=0.1, shuffle=True, random_state=self.random_state)
        logger.info(f"Split training and validation set into {len(self.train)} train and {len(self.validation)} validation")



class SubmissionPredictor():
    """Having trained using the ClassifierTrainer, generate predictions using the Predictor"""

    def __init__(self, input_dir):
        self.TEST_PATH = input_dir + "/test/"
        self.SUBMISSION_CSV = input_dir + "/sample_submission.csv"
        self.submission_ids = pd.read_csv(self.submission_csv).id.unique()

    def generate_submission(self):
        """Generates a submission file."""
        pass
    

def main(input_dir: str ="/kaggle/input", random_state:int =0):
    """Runs the main classifier and generates output for kaggle.
    
    :param input_dir
    :param random_state
    """
    c = ClassifierTrainer(input_dir, random_state)
    c.run_training()

    p = SubmissionPredictor(input_dir)
    p.generate_submission()


if __name__ == '__main__':
    defopt.run(main)
