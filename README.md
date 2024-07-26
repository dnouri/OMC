# Oh My Chatty (OMC)

Archived this project after the anyscale integration broke.  Looking
at contributing to either one of these instead:

- https://github.com/MindWorkAI/AI-Studio
- https://github.com/huggingface/chat-ui

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

### anyscale.com

To use a model hosted by [anyscale.com](https://anyscale.com),
register with anyscale.com and obtain an API key through their website
and place it into the `.env` file under `OPENAI_API_KEY`:

```
OPENAI_API_BASE=https://api.endpoints.anyscale.com/v1
OPENAI_API_KEY=esecret_531...
```

### vllm

You can also use the [vllm](https://docs.vllm.ai/) Python package to
install and serve a model locally.

In the following example, we'll assume that you want to run the
`NousResearch/Meta-Llama-3-8B-Instruct` model.  So let's download the
model weights first, which you can do like so:

```
git lfs install
git clone git@hf.co:NousResearch/Meta-Llama-3-8B-Instruct
```

Next, let's make sure yo install vllm, which is the software we use to
serve the model.  The [vllm
docs](https://docs.vllm.ai/en/latest/getting_started/installation.html)
details how to install vllm for different platforms.

Say you installed the [vllm CPU Docker
image](https://docs.vllm.ai/en/latest/getting_started/cpu-installation.html) by running something like this:

```
docker build -f Dockerfile.cpu -t vllm-cpu-env --shm-size=4g .
```

You would then proceed to run the image in a new terminal using the
following command:

```
docker run -it --rm \
   --network=host \
   -v /home/joe/omc/Meta-Llama-3-8B-Instruct:/app/model \
   vllm-cpu-env \
   --model /app/model \
   --dtype auto \
   --api-key "token-abc123"
```

Replace `/home/joe/omc/Meta-Llama-3-8B-Instruct` with the path to the
model that you downloaded previously.

Your configuration in `.env` might then look like this:

```
OPENAI_API_BASE=http://localhost:8000/v1
OPENAI_API_KEY=token-abc123
```

## You're now ready to start up the webapp

```bash
dotenv run -- streamlit run omc/st/app.py
```

## Project Future

- [ ] Support local models
- [ ] Support upload of database files (parquet and Excel) and querying those
- [ ] A desktop implementation of this app
