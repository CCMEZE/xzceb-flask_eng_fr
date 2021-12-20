"""Module to test and translate the watson translator"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']
VERSION='2021-11-01'

def translator_instance():
    """authenticate and create a translator instance"""
    authenticator = IAMAuthenticator(APIKEY)
    language_translator = LanguageTranslatorV3(
        version=VERSION,
        authenticator=authenticator
    )
    language_translator.set_service_url(URL)
    return language_translator


#languages=language_translator.list_languages().get_result()
#print(json.dumps(languages, indent=2))

## english code = en
## french code = fr
def english_to_french(english_text=None):
    """function that translates english to french """
    french_text=None
    if english_text is not None:
        language_translator=translator_instance()
        french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()['translations'][0]['translation']


    return french_text


def french_to_english(french_text=None):
    """function that translates french to english """
    english_text=None
    if french_text is not None:
        language_translator=translator_instance()
        english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()['translations'][0]['translation']
    return english_text


def run_test():
    """run the test case"""
    print(english_to_french('Hello'))
    print(french_to_english('Bonjour'))
if __name__ == '__main__':
    run_test()
