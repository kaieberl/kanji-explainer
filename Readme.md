# Kanji Explainer

## Description

This script takes a Japanese kanji as input and returns it with its meanings and readings, spoken in Japanese.

## API Keys

The script uses OpenAI's gpt-3.5-turbo-16k to generate an explanation for the kanji, and the Google Cloud Text-to-Speech API to speak the explanation.
To use the script, you need to have an OpenAI API key and a Google Cloud API key.
The OpenAI key should be stored in a file called `openai_api_key.txt` in the same directory as the main.py file.
It can be generated [here](https://platform.openai.com/account/api-keys) and costs 0.003$ / 1000 Tokens.
The Google cloud authentication json file should be in the same directory as the main.py file. It can be downloaded from the Google Cloud Console, as described [here](https://cloud.google.com/api-keys/docs/create-manage-api-keys).
It is free for the first 1 million characters per month.

## Instructions for invoking via keyboard shortcut in macOS

1. Create the following automator script:
```
source ~/opt/miniconda3/etc/profile.d/conda.sh
conda activate kanji-explainer
python3 ~/Documents/Code/kanji-explainer/main.py $1
```
Make sure the input is passed as arguments.

2. In settings, go to Security & Privacy -> Privacy -> Full Disk Access and add the app that should invoke the script, e.g. Safari. 
Else macOS will throw the error "Operation not permitted".

3. In settings, go to Keyboard -> Shortcuts -> Services -> General -> "Kanji Explainer" and set a keyboard shortcut, e.g. cmd+shift+K.

4. In Safari, mark a kanji and press the keyboard shortcut. A description should be played with the kanji and its meanings and readings.

You can try it out on the kanji tables provided [here](https://xn--fdk3a7ctb5192box5b.com/es/4nen_jp_kanji_hyo_002.html).
