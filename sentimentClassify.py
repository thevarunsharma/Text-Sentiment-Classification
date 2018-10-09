import numpy as np
import re
from keras.models import load_model
from keras.preprocessing import sequence
from pickle import load

with open('tokenizer.dat', 'rb') as fh:
    tokenizer = load(fh)

sentiment_model = load_model('model.hdf5')
sentiment_model._make_predict_function()

def predict_sentiment(text):
    text = [re.sub('\d','0',text)]
    if 'www.' in text or 'http:' in text or 'https:' in text or '.com' in text:
        text = re.sub(r"([^ ]+(?<=\.[a-z]{3}))", "<url>", text)
    vec = tokenizer.texts_to_sequences(text)
    vec = sequence.pad_sequences(vec, maxlen=100)
    pred = sentiment_model.predict(vec)
    return int(pred.round())
