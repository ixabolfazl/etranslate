import requests
import json

__HEADER__={
        'User-Agent': 'AndroidTranslate/5.3.0.RC02.130475354-53000263 5.1 phone TRANSLATE_OPM5_TEST_1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate',
        }

__URL__ = "https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&hl=es-ES&ie=UTF-8&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e"

def __send_api_request__(data : dict) -> (dict | str):
    """
    Sends a POST request to the Google Translate API with the provided data.
    
    Args:
        data (dict): The data to be sent in the POST request.

    Returns:
        dict: Parsed JSON data if the request is successful.
        str: Error message if the request fails.
    """
    try:
        reponse=requests.post(__URL__,data=data,headers=__HEADER__)
        data=json.loads(reponse.text)
        return data

    except requests.exceptions.HTTPError as errh:
        return f"Http Error: {errh}"  

    except requests.exceptions.ConnectionError as errc:
        return f"Error Connecting: {errc}"  

    except requests.exceptions.Timeout as errt:
        return f"Timeout Error: {errt}" 

    except requests.exceptions.RequestException as err:
        return f"OOps: Something Else {err}"

def translate(text : str, to="en", src='auto') -> str:
    """
    Translates the given text to the specified language.
    Args:
        text (str): The text to be translated.
        to (str): The target language code name (Based on ISO 639).
        src (str): The source language code name (default is auto-detection).

    Returns:
        str: The translated text or an error message if translation fails.
    """
    if text.strip() == "":
        return "OOps: string is empty!"

    data={'sl':src,'tl':to,'q':text}

    result = __send_api_request__(data)

    if(type(result) == str):
        return result
    else:
        return "".join([sentence['trans'] for sentence in result['sentences']])


def detect_laguage(text : str) -> str:
    """
    Detects the language of the given text.

    Args:
        text (str): The text whose language is to be detected.

    Returns:
        str: The detected language name or an error message if detection fails.
    """
    if text.strip() == "":
        return "OOps: string is empty "

    data={'sl':'auto','q':text}

    result = __send_api_request__(data)

    if(type(result) == str):
        return result
    else:
        return result['src']
