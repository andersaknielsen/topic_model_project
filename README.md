# BERTopic Topic Modeling Project 👋

Welcome to the BERTopic Topic Modeling Project!  
This project explores the use of BERTopic for topic modeling.

## Getting Started

To get started with this project, follow the steps below to set up your environment and run the initial analysis.

### Prerequisites

Make sure you have the following installed:
- [uv](https://github.com/astral-sh/uv)  
Text cleaning also makes use of Spacy, so install a requirement for that with `python -m spacy download en_core_web_sm`

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/andersaknielsen/topic_model_project.git
    cd topic_model_project
    ```

2. Create a virtual environment:
    ```bash
    uv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    uv pip install -r requirements.txt
    ```

### Running the Project

1. Prepare your dataset and place it in the `data` directory.
2. Run the topic modeling script:
    ```bash
    python run_topic_modeling.py
    ```

## Project Structure

- `data/`: Directory to store your datasets.
- `notebooks/`: Jupyter notebooks for exploratory data analysis and experiments.
- `scripts/`: Python scripts for data processing and modeling.
- `results/`: Directory to save the results of the topic modeling.

## Initial setup
Just for reference, this was how I set up the initial project, from scractch.
```bash
# Install uv if needed
# powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
# More on uv: https://github.com/astral-sh/uv
uv init topic_model_project --python 3.10
cd topic_model_project
uv venv --python 3.12
# Get a .gitignore suitable for a Python project
(Invoke-WebRequest -Uri "https://www.toptal.com/developers/gitignore/api/python,jupyternotebooks").Content | Out-File .gitignore
.venv\Scripts\activate
git init
uv pip install llvmlite
uv pip install pynndescent
uv pip install umap-learn
uv pip install bertopic==0.16.4
uv pip install spacy
uv pip install pip
uv pip install ipykernel
uv pip install tqdm
uv pip install ipywidgets
uv pip install nbformat
uv pip install fastparquet
uv pip freeze > requirements.txt
uv add -r requirements.txt
mkdir notebooks
mkdir src
python -m spacy download en_core_web_sm

code .
```