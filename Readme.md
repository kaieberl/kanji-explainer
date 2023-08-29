# Kanji Explainer

## Motivation

When I learn new Kanji, I can either look them up in a Japanese dictionary, or use a translator.
However, the explanations in the Japanese dictionary are often complicated and use Kanji that I don't know yet.
The translator only gives me one particular meaning and does not link to words I already know and use in Japanese.

The aim of this project is to help memorize Kanji by linking it to commonly used words in easy to understand Japanese.
The result is spoken out loud.

Sample output for '禁': [output.mp3](https://github.com/kaieberl/kanji-explainer/assets/84288341/91235cf6-1bb4-417e-af0c-bd95a8fb2658)
```
「禁」の漢字は、何かを止める、ないし許さないことを示します。
例えば、「禁止」は、「止」まることを「許さない」という意味ですね。
「禁煙」は、「煙」を出すことを「許さない」、つまりタバコを吸わないことを意味します。
また、「禁じる」は、何かをすることを許さない、または許可しないという動詞です。
いつも両親が使う「宿題をやらないとテレビは禁止だよ」などのフレーズにも出てくるよね。
```

## API Keys

The script uses OpenAI's GPT API to generate an example use cases for the kanji, and the Google Cloud Text-to-Speech API to speak it.
To use the script, you need to have an OpenAI API key and a Google Cloud API key.
The OpenAI key should be stored in a file called `openai_api_key.txt` in the same directory as the main.py file.
It can be generated [here](https://platform.openai.com/account/api-keys) and costs 0.003$ / 1000 Tokens for gpt-3.5-turbo-16k, and 0.06$ for gpt-4.
To use gpt-4, you need a prepaid credit balance of at least 0.50$, else you will get an API error.
The Google cloud authentication json file should be in the same directory as the main.py file. It can be downloaded from the Google Cloud Console, as described [here](https://cloud.google.com/api-keys/docs/create-manage-api-keys).
It is free for the first 1 million characters per month.

You can set the model inside the `config.yaml` settings file.

## Instructions for invoking via keyboard shortcut in macOS

1. Create the following automator script to make sure the script is invoked with the conda environment:
```
source ~/opt/miniconda3/etc/profile.d/conda.sh
conda activate kanji-explainer
python3 ~/Documents/Code/kanji-explainer/main.py $1
```
Make sure the input is passed as arguments.

2. In settings, go to Security & Privacy -> Privacy -> Full Disk Access and add the app that should invoke the script, e.g. Safari. 
Else macOS will throw the error "Operation not permitted".

3. In settings, go to Keyboard -> Shortcuts -> Services -> Text -> "Kanji Explainer" and set a keyboard shortcut, e.g. cmd+shift+K.

4. In your browser / pdf viewer etc., mark a kanji and press the keyboard shortcut. After ~3s, a description should be played with commonly used vocabularies and their meanings.

You can try it out on the kanji tables provided [here](https://xn--fdk3a7ctb5192box5b.com/es/4nen_jp_kanji_hyo_002.html).
