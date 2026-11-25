# Business document assistant

A small experiment in finding useful information in PDF and text files. Start with TF-IDF retrieval because it runs on an ordinary laptop, then optionally pass the retrieved passages to a local Ollama model. Without Ollama the app returns passages rather than pretending to generate an answer.

## Run

```sh
pip install -r requirements.txt
streamlit run app.py
```

Use non-sensitive documents for testing. Retrieval is lexical and may miss paraphrases. Model answers need checking against the original document.
