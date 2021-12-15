import pandas as pd
from spacy import displacy
 
def load_training_data():
    """Load the training data"""
    train = pd.read_csv("data/train.csv", index_col="id")
    return train

df = load_training_data()

def display_doc(id):
    """Given a doc id, display the entities using displacy."""
    
    text = open(f"data/train/{id}.txt").read()
    values = df.loc[id]
    ents = [{"start": int(row.discourse_start),
             "end": int(row.discourse_end), 
             "label": row.discourse_type}  for row in values.itertuples()]
    return displacy.render({"text": text, "ents": ents, "title": f"Doc {id}"}, 
                           manual=True,
                           style="ent",
                           options={"colors": {"Position": "#fef1d2", 
                                               "Claim": "#a9fdd8",
                                               "Lead": "#d7f8ff",
                                               "Evidence": "#cec5fa",
                                               "Counterclaim": "#feceea",
                                               "Concluding Statement": "#feceea"}})


