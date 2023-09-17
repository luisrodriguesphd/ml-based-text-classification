import numpy as np
from sklearn.datasets import fetch_20newsgroups

from text_classification.utils.data_prep import text_cleaner

# Load text dataset
n_samples = 600
newsgroups = fetch_20newsgroups(
    subset="test",
    categories=["rec.sport.baseball", "rec.sport.hockey", "talk.politics.guns"],
    shuffle=True,
    random_state=0,
    remove=("headers", "footers", "quotes"),
    return_X_y=False,
)
X = text_cleaner(np.array(newsgroups.data[:n_samples]))
y = np.array(newsgroups.target[:n_samples])
labels = np.unique(y)
label_encoder = dict(zip([str(label) for label in labels], range(len(labels))))
y_encoded = np.array([label_encoder[str(yi)] for yi in y])


data_test_train_model = [
    {
        "X": X,
        "y": y_encoded,
        "vec_name": "TfidfVectorizer",
        "clf_name": "XGBClassifier",
    }
]
