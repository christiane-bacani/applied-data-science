# Generative AI Fundamentals

Machine Learning has been around for many decades which leads you to a question about what led to the emergence of *Generative AI*? The answer is simple and straightforward. Companies are willing to invest more in computing resources and hiring large team that is willing to invest in generating and implementing new ideas. This are all contributors to the emergence of Generative AI.

## Foundational Model

![Foundational Model Image](foundational_model.png)

*Foundational Model* serves as a foundation or engine to empower Generative AI. Foundational Models are pre-trained on massive amount of data to perform multiple task such as text generation/summarization, information extraction, image generation, chatbot, and question answering. This is useful because compared to traditional ML Model that you train multiple models for different task, Foundational Model can perform this multiple task in a single unified model.

## FM Lifecycle

The FM Lifecycle covers multiple stages or steps on developing reliable foundational model that empowers almost all Generative AI today.

1. **Data Selection**: The model is needed to be train on massive volume and diverse sources of dataset. It is more common to use *Unlabeled data* for pre-training because it is more abundant and easier to collect than *Labeled Data*.

2. **Pre-training**: The model is now needed to perform on a process called *Pre-training*. Unlike traditional ML that has three learning approach: Supervised Learning, Unsupevised Learning, and Reinforcement Learning; The model model uses a learning approach called *Self-Supervised Learning* where it uses the structure of the dataset to auto-generate labels. For example, the model can discover or learn that the image dataset about drinks is a beverage (noun) or needed to be swallowed as a liquid (verb). After performing pre-training, the model can further continue doing this but in new data and context and it is called *Continuous Pre-Training* where the model will learn new data to perform task in different domain.

3. **Optimization**: After performing pre-training, the model can be optimize using different techniques such as *Fine-Tuning*, *Prompt Engineer*, and *Retrieval-Augmented Generation (RAG)*. This technique will be further discuss later on for this lesson or chapter.

4. **Evaluation**: Whether or not you use a pre-trained model off the shelf or fine-tune a model, the next step of the FM Lifecycle is to evaluate the performance of the model using multiple metrics or benchmark in order to assess if the model meets the business needs.