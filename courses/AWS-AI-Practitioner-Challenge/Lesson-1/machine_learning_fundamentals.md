# Machine Learning Fundamentals

Building a model involves a process starting from data collection and preparation (data preprocessing), selecting an algorithm, training the model using the prepared data, evaluate the accuracy of the model through
testing and iteration.

## Training data

```
-----------------                     ----------------                     ---------
| Training Data | ------------------> | ML Algorithm | ------------------> | Model |
-----------------                     ----------------                     ---------
```

Data collection and preparation is the most crucial step when building a **Machine Learning Model** because good
data makes the whole model works, in opposite, bad data can ruin the model's performance. We called it *garbage in, garbage out* which defines that bad data produce bad output and good data produce good output. That's why data collection and preparation is the most crucial step even though it is a routine process or task.

There are two states or properties of data used in *training* a model:

1. **Labeled data**: A dataset that each instance provides a label or desired variable or output provided by human experts through a reliable process (e.g, An animal image annotated with the class of that animal such as dog, cat, or wolf).
2. **Unlabeled data**: A dataset that each instance does not provide a label or desired variable or output.

There are two types of data used in *training* a model also:

1. **Structured data**: Structured data have a predefined structure or format that does not change over time. This is suitable for a *Machine Learning Model* that needed a data with well-defined features and labels. Below are types of structured data:
   - **Tabular data**: A tabular data have consistent instances defined as a row and different properties or labels defined as a column. This type of structured data is commonly seen in CSV files, Tables, or Databases.
   - **Time-series data**: A type of structured data that provides a sequence of values at different points in time such as stock prices, sensor readings, weather data.

2. **Unstructured data**: This type of data lacks a predefined format and does not organize its attribute in a fixed structure. This type of data needed a more advance machine learning model to extract its insights and meaningful patterns. Below are types of unstructured data:
    - **Text data**: A type of unstructured data consisting of documents, social media post, articles, and any other textual data.
    - **Image data**: Consisting of images, photographs, or any other video frames.

## Machine Learning Process

```
-----------------                     ----------------                     ---------
| Training Data | ------------------> | ML Algorithm | ------------------> | Model |
-----------------                     ----------------                     ---------
```

The compiled training data is fed into the Machine Learning Model. The process of learning for the model typically divides into three types: *Supervised Learning*, *Unsupservised Learning*, and *Reinforcement Learning*.

1. **Supervised Learning**: A type of machine learning process that the algorithm are trained or fed using a *labeled data*, the goal of this process is to let the model learn or predict a new output to unforeseen data.

2. **Unsupervised Learning**: A type of ML learning approach or process that the algorithm is trained using unlabeled data. The goal of this approach is to let the algorithm discover complex relationship, patterns, and structure of the input data.

3. **Reinforcement Learning**: In this approach, the model goes through trial and error and learn from feedback given naturally by the environment. The goal is to improve the model through feedback via rewards or penalties and the model will improve over time because of this. This will be chosen if the goal of the problem involves continuous adaptation, sequential decisions, or the model needs to learn through trial and error.

## Inferencing

```
-----------------                     ----------------                     ---------
| Training Data | ------------------> | ML Algorithm | ------------------> | Model |
-----------------                     ----------------                     ---------
```

After the model has been trained, the model performs predictions or decisions in *new or unforeseen data* and that is called *inference*. Below is the two types of inference use in machine learning.

1. **Batch Inference**: When the computer analyzes the dataset all at once or per batch in order to perform decisions or predictions. This type of inference is useful in task like data analysis where the speed of decision does not affect the performance of the model.
2. **Real-time Inference**: When the computer analyzes the dataset in real-time or as much as possible in order to make predictions, decisions, or actions. This type of inference is useful in certain scenarios or models such as self-driving cars that real-time data is crucial to perform any action and delayed latency will cause the car to crash.

Both type of inference have unique advantages and use cases. Your use case will determine which type of inference to use.