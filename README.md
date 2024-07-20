# Oh My Chatty (OMC)

OMC is a somewhat privacy preserving chatbot that can run in the cloud
or locally.

- So you don't have to go to OpenAI every time and deal with them
- So you can switch between implementations

## Installation

You can install OMC in a local Python virtual environment with these simple steps:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

To install requirements for development, additionally run this:

```bash
pip install -e .[devel]
```

## Configuration

It's necessary to set some environment variables related to the model
and API to use before you can start using the webapp.

For this, create a file called `.env` in your working directory with
contents similar to this:

```
OPENAI_API_BASE=https://api.endpoints.anyscale.com/v1
OPENAI_API_KEY=esecret_531...
```

You can register with anyscale.com and obtain an API key through their
website and place it into the `.env` file under `OPENAI_API_KEY`.

## You're ready to start up the webapp

```bash
dotenv run -- streamlit run omc/st/app.py
```

## Project Future

- [ ] Support local models
- [ ] Support upload of database files (parquet and Excel) and querying those
- [ ] A desktop implementation of this app
