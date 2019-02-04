# Text-Sentiment-Classification
A model for sentiment classification on text (positive or negative), trained and built using keras which uses a RNN with LSTM units. Dataset used was taken from Kaggle: Amazon Reviews for Sentiment Analysis dataset (https://www.kaggle.com/bittlingmayer/amazonreviews), which included 3.6M training examples(2.88M train and 0.72M validation) and 400k test examples. The model achieved test accuracy of 93.6% and training accuracy of 94.6%.

Based on this model created a web-user interface using Flask(Python) for backend, which takes as input a piece of text and returns the corresponding sentiment (positive/negative).
