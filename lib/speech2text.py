import requests
import sys

url='https://stream.watsonplatform.net/speech-to-text/api/recognize'
user='5d44d48d-d5b8-4464-b7ad-96375f793780'
password='Xh6YAhe33VTR'

def speech_to_text(input_file):
    response = requests.post(url, auth=(user, password))
    return str(response.raw)

if __name__ == '__main__':
    print speech_to_text(sys.argv[1])
