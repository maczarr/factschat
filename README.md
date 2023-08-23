# factsChat

factsChat lets you ask questions about content provided by you. It uses the OpenAI API.

## Requirements

You need at least Python 3.11 installed on your system and virtualenv. To use this tool you'll need an OpenAI API-Key: https://platform.openai.com/account/api-keys

## Installation

```bash
git clone https://github.com/maczarr/factschat.git
cd factschat
virtualenv ./venv
source venv/bin/activate
pip install -r requirements.txt
```

## Configuration

Copy the `.env.example` and adjust the content: `cp .env.example .env`

| name | description |
| ---- | ----------- |
| OPENAI_API_KEY | **This is the only required entry.** Get your API-Key at https://platform.openai.com/account/api-keys |
| OPENAI_MODEL | Name the model you want to use and have access to. Default is `gpt-3.5-turbo` |
| OPENAI_TEMPERATURE | Controls how deterministic the answer are. Has to be a floating number, default is `0.0`. |
| ANSWER_LANGUAGE | Tries to fix the language of the answer, despite the given context. It's more a hack in the system prompt, but works in most cases. |
| DB_FOLDER | Folder where the FAISS databases are stored. Default is `db`. |
| CONTENT_FOLDER | Folder from where the files are being read. Default is `content`. |
| URLS_FILENAME | Name of the text file from where to read in URLs if you want to make a database of website content. Default is `urls.txt`. |

## Usage

Assuming you are in the `factschat` folder and have the virtualenv activated.

### Retrieve data...

#### ...from files like a PDF

Put your PDF in the `content` folder. Afterwards:

```bash
python create_embeddings.py
```

Type `2` and press enter. In the end provide a database name and you're ready.

#### ...from websites

Create a `urls.txt` file in the root directory of the repository. Put one URL per line in the file, nothing more. It can be as much from one line to dozens. Afterwards:

```bash
python create_embeddings.py
```

Type `1` and press enter. In the end provide a database name and you're ready.

### Ask questions

```bash
python chat.py
```

At first you have to choose to which database you want to chat. Choose by answering with the number in front of the file name (e.g. `1`).

Now you can state your question. Depending on how busy the API is at the moment, the answer may take some time.

To leave the conversation, simply type "exit" or "bye".

## Known issues

Sometimes there are no sources provided with the answer. There is an [open issue on the langchain project](https://github.com/langchain-ai/langchain/issues/3592).

## Disclaimer

This repository isn't "a product", it's just a bit of fiddling around with the API and try out what's possible with LLMs.

There are no tests for the software and not much failsafes, it will likely fall apart if it's not used as intended.
