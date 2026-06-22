# Detective Game

A polished murder mystery detective game with both a console interface and a Streamlit web UI.

## Features

- Four suspects with unique personalities, motives, and clues
- Interrogation system that records evidence and suspect status
- Limited accusations for suspense and replay value
- Streamlit interface with a detective journal and evidence tracker

## Run the console game

1. Make sure Python is installed.
2. Run:

```bash
python3 main.py
```

## Run the Streamlit app

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Start the app:

```bash
streamlit run streamlit_app.py
```

## Deploy with Streamlit Cloud

1. Push your code to GitHub.
2. In Streamlit Cloud, create a new app and connect it to this repository.
3. Set the main file path to `streamlit_app.py`.
4. Confirm `requirements.txt` includes `streamlit`.

The app will be published at your Streamlit Cloud URL.
