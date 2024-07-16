# Food Recommendation App

## Overview

The Food Recommendation App is a web-based application that leverages Generative AI and Large Language Models (LLMs) to provide personalized recipe suggestions. Users can input ingredients they have, specify the type of recipe they want (vegetarian, vegan, non-vegetarian, eggetarian), and choose their desired cuisine. The app then generates tailored recipes using the Llama3 model by Meta.

## Features

- **User Input**: Accepts ingredients, recipe type, and cuisine preferences.
- **Generative AI**: Utilizes the Llama3 LLM to generate customized recipe recommendations.
- **User Interface**: Built with Streamlit, offering an interactive and user-friendly experience.

## Technologies Used

- **Llama3 Model (Meta)**: For natural language processing and recipe generation.
- **Streamlit**: For building the web-based user interface.
- **Ollama**: Local setup for running the Llama3 model.
- **Python**: Core programming language used for development.

## Installation and Setup

To set up and run the Food Recommendation App locally, follow these steps:
1. Downlad the python file and requirements.txt file in one folder.
2. You need to create a virtual env and install the packages listed in requirements.txt.
3. Run the follwoing commands:
           to Activate Ollama :  ollama serve
           to create New env : python3 -m venv myenv
           to Activate the virtual python environment : source venv/bin/activate
           to Start the Streamlit application : streamlit run app.py --server.enableCORS=false
