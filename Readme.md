# Kanji Explainer

日本語のインストラクションは[こちら](https://github.com/kaieberl/kanji-explainer/blob/main/Installation_jp.md)。

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

The script uses OpenAI's GPT API to generate example use cases for the kanji, and the Google Cloud Text-to-Speech API to speak the output.
To use the script, you need to have an OpenAI API key and a Google Cloud API key.
The OpenAI key should be stored in a file called `openai_api_key.txt` in the same directory as the main.py file.
It can be generated [here](https://platform.openai.com/account/api-keys) and costs 0.002$ / 1000 output Tokens for gpt-3.5-turbo-16k, and 0.03$ for gpt-4.
To use gpt-4, you need a prepaid credit balance of at least 0.50$, else you will get an API error.
The Google cloud authentication json file should be in the same directory as the main.py file. It can be downloaded from the Google Cloud Console, as described [here](https://cloud.google.com/api-keys/docs/create-manage-api-keys).

TLDR: On [https://cloud.google.com](https://cloud.google.com), create a new project. In your project, in the upper right corner, click on the 3 dots > project settings > service accounts > choose one or create service account > create key > json > create.
The resulting json file should be downloaded automatically.
Google TTS is free for the first 1 million characters per month, then $4 per 1 million characters.

You can set the model inside the `config.yaml` settings file.

## Customization

You can customize the output by editing the system_prompt in the `config.yaml` file.
E.g., you might want to try the following prompt:
```
Give some vocabulary examples and example sentences containing the input kanji for commonly used words 
in a corporate or technology environment or everyday life. 
If a kanji has multiple readings, give examples for each. Use Japanese only, don't use furigana.
```

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