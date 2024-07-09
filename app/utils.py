import openai
import os
from sqlalchemy.orm import Session
from crud import update_translation_task
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
openai.api_key = OPENAI_API_KEY

def perform_translation(task_id: int, text: str, languages: list, db: Session):
    translations = {}
    for lang in languages:
        try:
            response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = [
                    {"role": "system", "content": f"Translate the following text to {languages}:"},
                    {"role": "user", "content": text},
                ]
            )
            translated_text = response['choices'][0]['message']['content'].strip()
            translations[lang] = translated_text
        except Exception as e:
            print(f"Error translating to {lang}: {e}")
            translations[lang] = f"Error: {e}"
            
    update_translation_task(db, task_id, translations)

#

# def perform_translation(task_id: int, text: str, languages: list, db: Session) -> dict:
#     """Translates text into the target language.

#     Target must be an ISO 639-1 language code.
#     See https://g.co/cloud/translate/v2/translate-reference#supported_languages
#     """

#     from google.cloud import translate_v2 as translate
#     translate_client = translate.Client()

#     if isinstance(text, bytes):
#         text = text.decode("utf-8")
    
#     translations = {}
    
#     for lang in languages:
        
#         try:
#             translation_result = translate_client.translate(text, target_language=lang)
#             languages[lang] = translation_result["translatedText"]

#             print("Text: {}".format(translation_result["input"]))
#             print("Translation: {}".format(translation_result["translatedText"]))
#             print("Detected source language: {}".format(translation_result["detectedSourceLanguage"]))
            
#         except Exception as e:
#             translations[lang] = f"Error: {e}"
            
#     update_translation_task(db, task_id, translations)

            