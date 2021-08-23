import requests
import json

url="https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&hl=es-ES&ie=UTF-8&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e"

def translate(text,to="en",src='auto'):
    if text.strip() == "":
        return "OOps: string is empty "

    data={'sl':src,'tl':to,'q':text}
    headers={
            'User-Agent': 'AndroidTranslate/5.3.0.RC02.130475354-53000263 5.1 phone TRANSLATE_OPM5_TEST_1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Encoding': 'gzip, deflate',
            }
    try:
        reponse=requests.post(url,data=data,headers=headers)
        data=json.loads(reponse.text)
        result=[data['sentences'][i]['trans'] for i in range(len(data['sentences']))]
        return "".join(result)

    except requests.exceptions.HTTPError as errh:
        return f"Http Error: {errh}"  

    except requests.exceptions.ConnectionError as errc:
        return f"Error Connecting: {errc}"  

    except requests.exceptions.Timeout as errt:
        return f"Timeout Error: {errt}" 

    except requests.exceptions.RequestException as err:
        return f"OOps: Something Else {err}"

    