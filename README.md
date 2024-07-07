# Stock Market Decision Making LLM App

This is an AI program that provides **real-time** trading decisions for Nifty 50 stocks, as well as financial information about those stocks. The project exposes an HTTP REST endpoint to respond to user queries about what the **price-action decision** for a stock for that day will be or which stocks have the specific price-action decision for the day, as well as explain why the decision is made, taking into account various financial aspects of the stock. It builds a real-time LLM (Large Language Model)-enabled data pipeline in Python using Pathway's [LLM App features](https://github.com/pathwaycom/llm-app) and generates AI assistant responses using OpenAI API [Embeddings](https://platform.openai.com/docs/api-reference/embeddings) and [Chat Completion](https://platform.openai.com/docs/api-reference/completions).

This trading prediction application's core is built on **machine learning classifiers** that make buy, sell, or hold recommendations based on technical indicators generated from historical OHLCV (Open, High, Low, Close, Volume) data for financial assets. The program preprocesses data, creates features, trains several classifiers, and generates predictions about fresh data.

The **prediction model** runs whenever the app is launched, and the yfinance library aids in obtaining daily stock prices. The predicted decision dataframes for each of the Nifty 50 stocks are then aggregated and compiled into a csv file, which is then transformed to Jsonlines, with each line expecting a 'doc' object as in. We now have another json file that has information on each of the indicators and columns, as well as their implications for the choice. This jsonl file is merged with the previous jsonl file to produce the final jsonl file, which is used as input for the embedding process. 

- Input data in the form of Jsonlines is utilized to increase the overall efficiency of the operation.


## Features

- Provides stock decisions and insights powered by a model with high accuracy. 
- Provides a user-friendly UI with [Streamlit](https://streamlit.io/).
- Filters and provides stock decisions and insights in response to user questions. 
- Data and code reuse. 
- Extend data sources by using Pathway's built-in connectors for JSONLines, CSV, Kafka, Redpanda, Debezium, streaming APIs, and more.


## How the project works

The sample project does the following procedures to achieve the above output:

1. Prepare search data:
    1. Generate: When the app runs , the [prediction model](/examples/predictionmodel/stock_prediction.py) runs and computes stock decisions for the day and compiles all data including the indicators explanation jsonl file into one jsonl file ready to be given as input to the embedding process
    2. Chunk: Documents are split into short, mostly self-contained sections to be embedded.
    3. Embed: Each section is [embedded](https://platform.openai.com/docs/guides/embeddings) with the OpenAI API and retrieve the embedded result.
    4. Indexing: Constructs an index on the generated embeddings.
2. Search (once per query)
    1. Given a user question, generate an embedding for the query from the OpenAI API.
    2. Using the embeddings, retrieve the vector index by relevance to the query
3. Ask (once per query)
    1. Insert the question and the most relevant sections into a message to GPT
    2. Return GPT's answer


## How to run the project

Example only supports Unix-like systems (such as Linux, macOS, BSD). If you are a Windows user, we highly recommend leveraging Windows Subsystem for Linux (WSL) or Dockerize the app to run as a container.

### Run with Docker

1. [Set environment variables](#step-2-set-environment-variables)
2. From the project root folder, open your terminal and run `docker compose up`.
3. Navigate to `localhost:8501` on your browser when docker installion is successful.

### Prerequisites

1. Make sure that [Python](https://www.python.org/downloads/) 3.10 or above installed on your machine.
2. Download and Install [Pip](https://pip.pypa.io/en/stable/installation/) to manage project packages.
3. Create an [OpenAI](https://openai.com/) account and generate a new API Key: To access the OpenAI API, you will need to create an API Key. You can do this by logging into the [OpenAI website](https://openai.com/product) and navigating to the API Key management page.

Then, follow the easy steps to install and get started using the sample app.

### Step 1: Clone the repository

This is done with the `git clone` command followed by the URL of the repository:

```bash
git clone https://github.com/CodeAceKing382/Stocks-Insight-App
```

Next,  navigate to the project folder:

```bash
cd Stocks-Insight-App
```

### Step 2: Set environment variables

Create `.env` file in the root directory of the project, copy and paste the below config, and replace the `{OPENAI_API_KEY}` configuration value with your key. 

```bash
OPENAI_API_TOKEN={OPENAI_API_KEY}
HOST=0.0.0.0
PORT=8080
EMBEDDER_LOCATOR=text-embedding-ada-002
EMBEDDING_DIMENSION=1536
MODEL_LOCATOR=gpt-3.5-turbo
MAX_TOKENS=200
TEMPERATURE=0.0
```

### Step 3: Install the app dependencies

Install the required packages:

```bash
pip3 install --upgrade -r requirements.txt
```
### Step 4 (Optional): Create a new virtual environment

Create a new virtual environment in the same folder and activate that environment:

```bash
python3 -m venv pw-env && source pw-env/bin/activate
```

### Step 5: Run and start to use it

You start the application by navigating to `llm_app` folder and running `main.py`:

```bash
python3 main.py
```

### Step 6: Run Streamlit UI for file upload

You can run the UI separately by navigating to `cd examples/ui` and running Streamlit app
`streamlit run app.py` command. It connects to the Discounts backend API automatically and you will see the UI frontend is running http://localhost:8501/ on a browser:
