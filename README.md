Welcome to the PromptlyTech Repo dedicated to refining Language Models (LLMs) through advanced Prompt Engineering and the implementation of Retrieval Augmented Generation (RAG) techniques. This toolkit is designed to elevate prompt services, unlocking enhanced AI capabilities seamlessly.

## Core Services

### 1. Intelligent Prompt Generation:
Craft effective prompts effortlessly to maximize the potential of Language Models.

### 2. Automated Test Case Generation:
Streamline the creation of diverse test cases for comprehensive coverage and heightened reliability.

### 3. Prompt Evaluation and Ranking:
Assess and rank prompts based on their effectiveness, ensuring optimal outcomes from Language Models.

## Some Features

- Precise prompt engineering tailored for diverse business contexts.
- Integration with cutting-edge LLMs, including GPT-3.5 and GPT-4.
- Automated testing and ranking for heightened user engagement and satisfaction.

## Getting Started

**Clone the Repository:**
```bash
git clone https://github.com/birehan/PromptlyTech-Optimization-Hub.git
cd PromptlyTech-Optimization-Hub
```

**Set Up Environment Variables:**
Create a `.env` file in the root directory and add the following:
```ini
# Development environment
OPENAI_API_KEY=""
VECTORDB_MODEL="gpt-3.5-turbo"
```

## Installation

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Generate test data
make data_generate

# Evaluate user input data (probability, accuracy, confidence)
make data_evaluate
```

## Contribution Guidelines

I enthusiastically welcome contributions from the community. Feel free to open issues, submit pull requests, and collaborate with me to enhance this toolkit.

## License

This project is licensed under the MIT License.
