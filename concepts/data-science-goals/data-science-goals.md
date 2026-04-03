# Model Learning Approach/Process

Define the goal first, check the data constraint, and select the algorithm based on the selected learning approach and weigh-in the performance, complexity, and resources.

```
Exploratory Data Analayiss
    |
    |-> Understand the data and how to clean, transform, wrangle it properly.

Descriptive Analysis
    |
    |-> Business Intelligence / Data Analysis.

Diagnostic Analysis
    |
    |-> Business Intelligence / Data Analysis.
    |-> Choose Model with Unsupervised Learning Approach if the goal is understanding the structure, relationship, or hidden patterns or behaviors.

Predictive Analysis
    |
    |-> Choose Model with Supervised Learning Approach (Semi-Supervised Learning if the data is not fully labeled or expensive/time-consuming).

Prescriptive Analyis
    |
    |-> Choose Model with Supervised Learning Approach if the goal is static output (Semi-Supervised Learning if the data is not fully labeled or expensive/time-consuming).
    |-> Choose Model with Reinforcement Learning Approach if the goal is continuous/real-time adaptation, sequential decision, involves learning through trial-and-error.

Recommendation System
    |
    |-> Choose Model with Supervised Learning Approach if the goal is static output (Semi-Supervised Learning if the data is not fully labeled or expensive/time-consuming).
    |-> Choose Model with Reinforcement Learning Approach if the goal is continuous/real-time adaptation, sequential decision, involves learning through trial-and-error.

Classification
    |
    |-> Choose Model with Supervised Learning Approach if the goal is static output (Semi-Supervised Learning if the data is not fully labeled or expensive/time-consuming).
    |-> Choose Model with Unsupervised Learning Approach if the goal is understanding the structure, relationship, or hidden patterns or behaviors.

Clustering
    |
    |-> Choose Model with Unsupervised Learning Approach if the goal is understanding the structure, relationship, or hidden patterns or behaviors.
```