import io
import os
import sys
from typing import Union

import openai
from google.cloud import texttospeech
import pygame.mixer
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up your OpenAI API key
project_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = project_dir + '/out'
openai.api_key = open(project_dir + '/openai.txt', 'r').read()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = project_dir + "/texttospeech.json"

SAVE_TO_MP3 = True


def get_kanji_explanation(kanji: str) -> str:
    """
    use the OpenAI GPT-3.5-Turbo model with 16KB context length to generate a short explanation of a kanji

    Args:
        kanji: a single kanji character

    Returns:
        a short explanation of the kanji
    """
    prompt = f"'{kanji}'の漢字の読み、意味とよく使う例文を小学６年生のレベルで示しなさい。ひらがなはいらない"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )

    return response.choices[0].message.content.strip().replace('\n\n', '。\n')


def text_to_speech(text: str, kanji: str = 'output') -> None:
    """
    use Google cloud text to speech to convert text to speech
    Args:
        text: text in Japanese
        kanji: kanji character to use as the output file name
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

    if SAVE_TO_MP3:
        # create out directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Save the audio stream to a file
        output_filename = f"/{kanji}.mp3"
        with open(output_dir + output_filename, "wb") as f:
            f.write(audio_stream.read())

        logger.info(f"Saved to {output_filename}")

    play_audio(output_dir + output_filename if SAVE_TO_MP3 else audio_stream)


def play_audio(audio_stream: Union[str, io.BytesIO]) -> None:
    """
    play audio stream in the background

    Args:
        audio_stream: audio stream to play (either a file path or a BytesIO object)
    """
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

    # if explanation is already in out directory, play the existing file
    if os.path.exists(output_dir + f'/{kanji_input}.mp3'):
        play_audio(output_dir + f'/{kanji_input}.mp3')
        sys.exit(0)

    explanation = get_kanji_explanation(kanji_input)
    logger.info(explanation)

    text_to_speech(explanation, kanji_input)
