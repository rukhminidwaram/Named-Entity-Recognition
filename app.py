import streamlit as st 
from spacy import displacy
import en_core_web_sm
nlp = en_core_web_sm.load()
k=nlp.get_pipe("ner").labels
print(k)
import nltk
nltk.download('punkt')
HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""
def analyze_text(text):
	return nlp(text)
def main():
	"""Streamlit App"""
	st.title("Entity Checker")
	activities = ["NER Checker"]
	choice = st.sidebar.selectbox("Select Activity",activities)
	if choice == 'NER Checker':
		st.subheader("Named Entity Recog with Spacy")
		raw_text = st.text_area("Enter Text Here","Type Here")
		if st.button("Analyze"):
			docx = analyze_text(raw_text)
			html = displacy.render(docx,style="ent")
			html = html.replace("\n\n","\n")
			st.write(HTML_WRAPPER.format(html),unsafe_allow_html=True)		
if __name__ == '__main__':
	main()
