# Cover Letter Generator App
![Screenshot at 2023-09-15 22-58-09](https://github.com/Tuning-AI/Cover-Letter-Generator-App/assets/145156896/d929da57-3df8-48c4-9fe7-b78098fc7fd8)

## Overview
The Cover Letter Generator App is a powerful tool that leverages the capabilities of the Llama2_7B_Cover_letter_generator model. 
This model has been fine-tuned using advanced techniques Parameter-Efficient Fine-Tuning (PEFT) and a custom dataset to excel at 
generating personalized cover letters tailored to specific job descriptions. **https://huggingface.co/TuningAI/Llama2_7B_Cover_letter_generator**

## Base Model:
This model is based on the Meta's **meta-llama/Llama-2-7b-hf** architecture, making it a highly capable foundation for generating human-like text responses.

## Fine-Tuning Technique (QLoRA):
The model has been fine-tuned using **QLoRA**, an extension of **LoRA** that incorporates 4-bit NormalFloat (NF4) quantization and Double Quantization techniques.
This enhances parameter efficiency during fine-tuning, making the model resource-friendly while maintaining high performance.**https://arxiv.org/abs/2305.14314**

## Custom Dataset:
We've carefully curated and manually created a custom dataset to ensure that the model understands the nuances of cover letter generation for various job positions.
**https://huggingface.co/datasets/TuningAI/Cover_letter_v2**

## Use Cases:
* Automating Cover Letter Creation: **Llama2_7B_Cover_letter_generator** can be used to rapidly generate cover letters for a wide range of job openings, saving time and effort for job seekers.
## Limitations:
* While the model excels in generating cover letters, it may occasionally produce text that requires minor post-processing for perfection.
* It may not fully capture highly specific or niche job requirements, and some manual customization might be necessary for certain applications.
* **Llama2_7B_Cover_letter_generator**'s performance may vary depending on the complexity and uniqueness of the input prompts.
* Users should be mindful of potential biases in the generated content and perform appropriate reviews to ensure inclusivity and fairness.
## Frameworks
+ **Langchain**: We've integrated Langchain to facilitate smooth and interactive conversations with the assistant. Langchain streamlines the chat functionality, ensuring a user-friendly experience.

+ **Transformers**: The Transformers library serves as the foundation for fine-tuning advanced language models. It empowers the assistant with the ability to generate high-quality responses.

+ **Streamlit**: We've implemented Streamlit to create a user-friendly web interface for easy access to the assistant's features. Streamlit enables a responsive and intuitive user experience.

## How To Run This APP
```
pip install -r requirements.txt
streamlit run app.py
```
