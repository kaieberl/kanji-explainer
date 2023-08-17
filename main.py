import io
import os
import sys

import openai
from google.cloud import texttospeech
import pygame.mixer
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up your OpenAI API key
openai.api_key = open('openai.txt', 'r').read()
project_dir = os.path.dirname(os.path.abspath(__file__))
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = project_dir + "/texttospeech-396212-983639b54ad0.json"


def get_kanji_explanation(kanji: str) -> str:
    """
    use the OpenAI GPT-3.5-Turbo model with 16KB context length to generate a short explanation of a kanji

    Args:
        kanji: a single kanji character

    Returns:
        a short explanation of the kanji
    """
    prompt = f"'{kanji}'の漢字の読み、意味と例文を短く小学６年生のレベルで示しなさい。ふりがなはいらない"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )

    return response.choices[0].message.content.strip().replace('\n', '。\n')


def text_to_speech(text: str) -> None:
    """
    use Google cloud text to speech to convert text to speech
    Args:
        text: text in Japanese
    """
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        language_code="ja-JP",
        name="ja-JP-Wavenet-B",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    audio_stream = io.BytesIO(response.audio_content)

    # play the audio automatically in the background
    pygame.mixer.init()
    pygame.mixer.music.load(audio_stream)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python main.py <kanji>')
        sys.exit(1)
    kanji_input = sys.argv[1]
    explanation = get_kanji_explanation(kanji_input)
    logger.info(explanation)

    text_to_speech(explanation)
