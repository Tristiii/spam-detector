# SpamDetector

## Introduction

This spam detector is trained on the SMS Spam Collection dataset, found in [this link](https://archive.ics.uci.edu/dataset/228/sms+spam+collection). This dataset contains 5574 text messages, each classified as spam or ham.

To use the model, run the main.py file. Here, you can fill in your text and the model will classify it as spam or not spam.

## Methods

A TF-IDF vectorizer is applied on the dataset. Then, the result is put into a naive Bayes classifier.

## Results

The model obtains an accuracy of 95.96%.