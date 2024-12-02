from langdetect import detect 
from googletrans import Translator
from streamlitUI import language , st
from Handler import response, user_input

translator = Translator()

if language == 'Arabic' and user_input:
    if detect(user_input) == "ar":
        user_input_translated = translator.translate(user_input, src="ar", dest="en").text
        response_translated = translator.translate(response, src="en", dest="ar").text
        st.write("**Response in Arabic:**")
        st.write(response_translated)