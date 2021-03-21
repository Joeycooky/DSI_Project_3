# Project 3 - iPhone VS Android : reddit posts classification


## Problem Statement
As a data scientist at Apple, I have discussed with product development teams and found out that they are currently processing the customer feedback only from the query from Apple official websites. They feel that reports collected from forums and feedback channels are mainly about serious malfunctions containing lots of technical stuff. However, they would like to get sentiment from non-technical users for further development i.e., 'I really love the new function in iOS 13.2.1', 'New version of Siri is fantastic!' for following purposes ...
- to see whether the users love their new function or not?
- Which aspect need improvement?
- What do general users expect to see in the future?

To address their problem, I suggested the team to get non-technical comments from the reddit websites. Manual Collection seems to be a safe approach since I can directly go to 'iPhone' subreddit and read through each single posts. Nevertheless, it is extremely labor intensive and inefficient. So in this project, I'll build a classifier to automatically distinguish iPhone posts from other kind of smartphone posts and send them to product development teams.

In the foreseeable future, I'll try to conduct a sentiment analysis on iPhone posts I got to separate positive and negative comment and hand it over to each responsible parties.
The project will compares ...

2 words to vectors converter (Vectorizers):
1. CountVectorizer
1. TfidfVectorizer

and 3 classifiers:
1. LogisticRegression
1. Naive Bayes (Multinomial variance)
1. KNearestNeighbors
The candidate model must not only yield high accuracy, but it must also be highly interpretable

**Evaluation metrics:**  
For this occasion, **Accuracy** will be used as an evaluation metrics

**Baseline performance:**  
The performance of our model will be compared against the baseline performance (the ratio of the majority class)

## About the dataset
Data will be collected using reddit api with "r/android" and "r/iphone" endpoints.
Detailed data collection scripts are located in separated .py files named **'get_android.py' and 'get_iphone.py'**.
Below code block is a snippet from one of the mentioned file

## Executive Summary

Thanks to the data pulled from reddit API, we discovered the preliminary insight since our Exploratory Data Analysis section that post containing comment about two giant smartphone operating systems (and also major manufacturers) have their own characteristics such as

- Obviously, the most frequent word in iPhone corpus is 'iPhone' itself, followed by apple and different iPhone models such as '12', 'pro', 'max'
- The same fashion have also been observed for android phone. The most frequent word in Android corpus is 'Android' itself, followed by different smartphone manufacturers such as 'Samsung', 'Google' and their flagship model like 'Galaxy', 'Note', 'Pixel'

![intersection](https://github.com/Joeycooky/DSI_Project_3/blob/main/images/intersection.png)

It's hard to detect whether the post is about iPhone or Android by its simple features such as text length and title length. However, after develop and comparing several models, we can build a classifier with relatively high accuracy. The best among 6 models is the model with **TfidfVectorizer with LogisticRegression** in which it achieved 86% accuracy on the testing set.

![ROC](https://github.com/Joeycooky/DSI_Project_3/blob/main/images/ROC.png)


After iterating with different decision threshold, **the optimal value for our production is 0.7.** This threshold allow the model to filter out iPhone related posts with minimal number of android posts leaked in. Therefore allow our product development team to further work with the data with minimal difficulty. The output of the model (Cleaned dataset containing mostly iPhone related post) can be feed into a sentiment analysis algorithm to analyze the user feedback accordingly.

![CM@0.5](https://github.com/Joeycooky/DSI_Project_3/blob/main/images/CM%400.5.png)
![CM@0.7](https://github.com/Joeycooky/DSI_Project_3/blob/main/images/CM%400.7.png)
