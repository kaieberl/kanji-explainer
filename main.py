import io
import os
import sys
from typing import Union
from omegaconf import DictConfig

from omegaconf import OmegaConf
from openai import OpenAI
import pygame.mixer
from google.cloud import texttospeech
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(PROJECT_DIR, 'out')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(PROJECT_DIR, "texttospeech.json")
os.environ["OPENAI_API_KEY"] = open(os.path.join(PROJECT_DIR, 'openai.txt'), 'r').read().strip()


class KanjiExplainer:

    @staticmethod
    def get_explanation(kanji: str, config: DictConfig) -> str:
        client = OpenAI()
        response = client.chat.completions.create(
            model=config.model_name,
            messages=[
                {
                    "role": "system",
                    "content": config.kanji_message if len(kanji) == 1 else config.word_message
                },
                {"role": "user", "content": f"{kanji}"},
            ],
            max_tokens=500,
            temperature=0.1
        )
        # parse content of triple quotes
        return response.choices[0].message.content.strip().split('"""')[1]


class SpeechSynthesizer:

    @staticmethod
    def convert_text_to_speech(text: str, config: DictConfig, kanji: str = 'output') -> None:
        client = texttospeech.TextToSpeechClient()
        input_text = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code="ja-JP",
            name="ja-JP-Wavenet-B",
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
        )
        audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
        response = client.synthesize_speech(
            request={"input": input_text, "voice": voice, "audio_config": audio_config}
        )
        audio_stream = io.BytesIO(response.audio_content)
        if config.save_output:
            if not os.path.exists(OUTPUT_DIR):
                os.makedirs(OUTPUT_DIR)

            output_filename = f"/{kanji}_{config.model_name}.mp3"
            with open(OUTPUT_DIR + output_filename, "wb") as f:
                f.write(audio_stream.read())
            logger.info(f"Saved to {output_filename}")

        AudioPlayer.play(OUTPUT_DIR + output_filename if config.save_output else audio_stream)


class AudioPlayer:

    @staticmethod
    def play(audio_stream: Union[str, io.BytesIO]) -> None:
        pygame.mixer.init()
        pygame.mixer.music.load(audio_stream)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)


def main():
    if len(sys.argv) != 2:
        print('Usage: python main.py <kanji>')
        sys.exit(1)
    kanji_input = sys.argv[1]

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Parsing config data from YAML file
    config = OmegaConf.load(PROJECT_DIR + '/config.yaml')

    if os.path.exists(os.path.join(OUTPUT_DIR, f'{kanji_input}_{config.model_name}.mp3')):
        AudioPlayer.play(OUTPUT_DIR + f'/{kanji_input}_{config.model_name}.mp3')
        sys.exit(0)

    explanation = KanjiExplainer.get_explanation(kanji_input, config)
    logger.info(explanation)

    with open(OUTPUT_DIR + f'/{kanji_input}_{config.model_name}.txt', 'w', encoding='utf-8') as f:
        f.write(explanation)

    SpeechSynthesizer.convert_text_to_speech(explanation, config, kanji_input)


if __name__ == '__main__':
    main()