import requests 
import logging 

class APIError(Exception):
    pass 

def yes_or_no():
    try:
        response = requests.get('https://yesno.wtf/api/')
        response.raise_for_status()
    except Exception as e:
        logging.exception(e)
        raise APIError('Error connecting to API') 

    try: 
        data = response.json()
    except Exception as e:
        logging.exception(e)
        raise APIError('Data returned is not JSON') from e 

    try: 
        answer = data['answer']
    except Exception as e:
        logging.exception(e)
        raise APIError('JSON does not contain expected data') from e 

    return answer


def main():

    try:
        answer = yes_or_no()
        print(answer)
    except APIError as e:
        message, = e.args
        print(message)


if __name__ == '__main__':
    main()