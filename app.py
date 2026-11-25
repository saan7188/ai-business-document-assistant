import streamlit as st
from assistant_core.documents import read_document, chunks
from assistant_core.retrieval import DocumentIndex
from assistant_core.generation import generate

st.title("Business document assistant")
st.caption("Search document passages or try a local language model.")
file = st.file_uploader("Choose a document", type=["pdf", "txt"])
question = st.text_input("Question")
use_llm = st.checkbox("Generate an answer with Ollama")
model = st.text_input("Installed Ollama model", "llama3.2") if use_llm else ""
if st.button("Search") and file and question.strip():
    try:
        index = DocumentIndex(chunks(read_document(file.name, file.getvalue())))
        hits = index.search(question)
        if not hits:
            st.info("No matching passages found.")
        else:
            if use_llm:
                try:
                    st.write(generate(question, hits, model))
                except Exception as exc:
                    st.warning(f"Local model unavailable: {exc}")
            for page, passage, score in hits:
                st.markdown(f"**Page {page} · relevance {score:.2f}**")
                st.text(passage)
    except Exception as exc:
        st.error(str(exc))
