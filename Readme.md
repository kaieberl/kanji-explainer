# Kanji Explainer

日本語のインストラクションは[こちら](https://github.com/kaieberl/kanji-explainer/blob/main/Installation_jp.md)。

## Description

When I learn new words in Japanese, I can either look them up in a Japanese dictionary, or use a translator.
However, the explanations in the Japanese dictionary are often complicated and use Kanji that I don't know yet.
The translator only gives me one particular meaning and does not link to words I already know and use in Japanese.

The aim of this project is to help memorize Kanji by linking them to commonly used words in easy to understand Japanese.
The result is spoken out loud.

Sample output for `論`: [play audio](https://github.com/kaieberl/kanji-explainer/assets/84288341/a1bd5b65-8bd4-440a-960c-115c9b759054)
```
「論文を書く」の「ろん」とか「論争になる」の「ろん」に使われている。
```

Sample output for `送信`: [play audio](https://github.com/kaieberl/kanji-explainer/assets/84288341/e58dcc14-8051-42f3-bd1f-025ca293867b)
```
 送信という言葉は「友達を家まで送る」の「おく」と「彼を信じる」の「しん」でできている。
```

## API Keys

The script uses OpenAI's GPT API to generate example use cases for the kanji, and the Google Cloud Text-to-Speech API to speak the output.
To use the script, you need to have an OpenAI API key and a Google Cloud API key.
The OpenAI key should be stored in a file called `openai_api_key.txt` in the same directory as the main.py file.
It can be generated [here](https://platform.openai.com/account/api-keys) and costs 0.002$ per 1000 output Tokens for gpt-3.5-turbo-16k, and 0.01$ for gpt-4.
To use gpt-4, you need a prepaid credit balance of at least 0.50$, else you will get an API error.
The Google cloud authentication json file should be in the same directory as the main.py file. It can be downloaded from the Google Cloud Console, as described [here](https://cloud.google.com/api-keys/docs/create-manage-api-keys).

TLDR: On [https://cloud.google.com](https://cloud.google.com), create a new project. In your project, in the upper right corner, click on the 3 dots > project settings > service accounts > choose one or create service account > create key > json > create.
The resulting json file should be downloaded automatically.
Google TTS is free for the first 1 million characters per month, then $4 per 1 million characters.

You can set the model inside the `config.yaml` settings file.

## Customization

Currently the following instruction is used for single characters:
```
For the given kanji, I want the 2 most common usages in everyday language. Find a common phrase that contains the word. Without using the internet, write out your chain of thought like this: 
This kanji is used in the words 景色, 景気, 景観, 景品, 風景. The most common words in daily life are: 景色, 景気.
Finally write your answer as follows, enclosed in triple quotes:
"""
「景色がきれい」とか「景気がいい」の「け」に使われている。
"""
```
For multiple characters (words), the following instruction is used:
```
I will give you a Japanese word. For each kanji, I want the most common usage in everyday language, but not the input word. Find a common phrase that contains the word. Without using the internet, write out your chain of thought like this: 
kanji: 景
This kanji is used in the words 景色, 景気, 景観, 景品, 風景. The most common word in daily life is 景色.
Finally write your answer in a sentence, enclosed in triple quotes like this:
"""
背景という言葉は「背中が痛い」の「せ」と「景色がきれい」の「け」でできている。
"""
```
The content of the triple quotes is then parsed and read out loud.

You can customize the output by editing the system_prompt in the `config.yaml` file.

## Instructions for invoking via keyboard shortcut in macOS

1. Create the following automator script to make sure the script is invoked with the conda environment:
```bash
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

## Instructions for invoking via keyboard shortcut in Windows
0. **Preparation**  
    Make sure you have PowerShell installed. You can check by opening the command prompt and typing `powershell`. If it is not installed, you can download it [here](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.1).
1. **Edit the PowerShell Script**:
   Right-click on the `kanji-explainer.ps1` file and select `Edit`. Replace the path to the `kanji-explainer-env` folder with the path to the `kanji-explainer-env` folder on your computer.
2. **Create a Shortcut**:
    - Right-click on the desktop, go to `New > Shortcut`.
    - In the location field, enter: `pwsh.exe -File "C:\path\to\kanji-explainer.ps1"`, replacing `C:\path\to\kanji-explainer.ps1` with the path to the `kanji-explainer.ps1` file.
3. **Set a Keyboard Shortcut**:
    - Right-click on the newly created shortcut and select `Properties`.
    - In the `Shortcut` tab, click in the `Shortcut key` field and press the key combination you want to use, e.g. `Ctrl + Alt + K`.
    - Click `OK` to save your changes.

Now, if you copy a kanji and press the keyboard shortcut, the script will be run.