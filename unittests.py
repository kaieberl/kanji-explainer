from main import KanjiExplainer, SpeechSynthesizer, Config, PROJECT_DIR
import unittest
from unittest.mock import patch, MagicMock


class TestGetKanjiExplanation(unittest.TestCase):
    def test_get_kanji_explanation(self):
        config = Config.from_yaml(PROJECT_DIR + '/config.yaml')
        kanji_explainer = KanjiExplainer()
        result = kanji_explainer.get_explanation('相', config)
        print(result)


class TestTextToSpeech(unittest.TestCase):
    def test_text_to_speech(self):
        config = Config.from_yaml(PROJECT_DIR + '/config.yaml')
        speech_synthesizer = SpeechSynthesizer()
        speech_synthesizer.convert_text_to_speech("""漢字: 相

読み方: あい

意味: 「相」という漢字は、二つのものが互いに関連していることを表す漢字です。また、顔や外見なども指すことがあります。

使い方:

二つのものが互いに関連している場合に使います。例えば、相手（あいて）は友達との関係を指すことができます。友達との間に相互のつながりがあることを表します。
また、相撲（すもう）という言葉もこの漢字を含んでいます。相撲は日本の伝統的な格闘技であり、二人の力士が対戦する姿が特徴です。この場合、「相」は二人の対戦が互いに関連していることを示しています。
「相」の漢字は、二つのものが関係を持っていることや、互いに影響を及ぼしていることを表す際に使用されます。
""", config)


if __name__ == '__main__':
    unittest.main()
