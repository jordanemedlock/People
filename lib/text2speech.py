import requests
import sys

url = 'https://stream.watsonplatform.net/text-to-speech/api/v1/synthesize'

def text_to_speech(text, output_file, output_type='file'):
    r = requests.get(url, params={'text': text, 'accept': 'audio/wav'}, auth=('67b67361-4aa6-4ce8-a3be-d89d64a7dd5f', '8HNPvldyGKbw'), stream=True)
    with open(output_file, 'wb') as f:
        for block in r.iter_content(1024):
            f.write(block)


if __name__ == '__main__':
    text_to_speech(sys.argv[1], 'output.wav')