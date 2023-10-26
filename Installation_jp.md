# インストール手順： macOS の場合
0. 準備  
Python 3.8 以上をインストールしてください。[こちら](https://www.python.org/downloads/release/python-3918/)からダウンロードできます。conda でインストールすることもできます。  
git をインストールしてください。[こちら](https://git-scm.com/downloads)からダウンロードできます。
1. このプロジェクトをクローンしてください。そのためには、ターミナルを開き、以下のコマンドを実行してください。your/path は、プロジェクトを保存したい場所に置き換えてください。
```bash
cd your/path
git clone https://github.com/kaieberl/kanji-explainer.git
cd kanji-explainer
```
アップデートはいつでも、以下のコマンドでできます。
```bash
cd your/path/kanji-explainer
git pull
```
2. 以下のコマンドを実行してください。
```bash
python3 -m venv kanji-explainer-env
source kanji-explainer-env/bin/activate
pip install -r requirements.txt
```
3. OpenAI API キーを取得してください。[こちら](https://platform.openai.com/account/api-keys)から取得できます。  
`openai.txt` というファイルを作成し、その中に API キーを書き込んでください。
4. Google Cloud API キーを取得してください。[こちら](https://cloud.google.com/api-keys/docs/create-manage-api-keys)から取得できます。  
ダウンロードした json ファイルを、`texttospeech.json` という名前で main.py と同じディレクトリに保存してください。

これで、プロジェクトの準備は完了です。

## キーボードショートカットを作る手順
Automator を開き、以下のようにスクリプトを作成してください。
path/to/kanji-explainer は、ダウンロードしたプロジェクトのパスに置き換えてください。
パスは、ターミナルで `pwd` と入力することで確認できます。
```bash
source path/to/kanji-explainer/kanji-explainer-env/bin/activate
python3 path/to/kanji-explainer/main.py $1
```
conda 環境を使った場合は、以下のようにしてください。
```bash
source ~/opt/miniconda3/etc/profile.d/conda.sh
conda activate kanji-explainer
python3 ~/Documents/Code/kanji-explainer/main.py $1
```

# インストール手順： Windows の場合

0. **準備**
   - Python 3.8 以上をインストールしてください。[こちら](https://www.python.org/downloads/)からダウンロードできます。conda でインストールすることもできます。
   - git をインストールしてください。[こちら](https://git-scm.com/downloads)からダウンロードできます。

1. **このプロジェクトをクローンしてください**
   - コマンドプロンプトを開き、以下のコマンドを実行してください。
   `your\path` は、プロジェクトを保存したい場所に置き換えてください。
   ```cmd
   cd your\path
   git clone https://github.com/kaieberl/kanji-explainer.git
   cd kanji-explainer
   ```
    - アップデートはいつでも、以下のコマンドでできます。
    ```cmd
    cd your\path\kanji-explainer
    git pull
    ```
2. **以下のコマンドを実行してください**
    ```cmd
    python -m venv kanji-explainer-env
    kanji-explainer-env\Scripts\activate
    pip install -r requirements.txt
    ```
  
3. **OpenAI API キーを取得してください**
   - [こちら](https://platform.openai.com/account/api-keys)から取得できます。
   - `openai.txt` というファイルを作成し、その中に API キーを書き込んでください。

4. **Google Cloud API キーを取得してください**
   - [こちら](https://cloud.google.com/api-keys/docs/create-manage-api-keys)から取得できます。
   - ダウンロードした json ファイルを、`texttospeech.json` という名前で `main.py` と同じディレクトリに保存してください。

これで、プロジェクトの準備は完了です。

## キーボードショートカットを作る手順
0. **準備**  
    PowerShellがインストールされていることを確認してください。コマンドプロンプトを開き、`powershell`と入力して確認できます。インストールされていない場合は、[こちら](https://docs.microsoft.com/ja-jp/powershell/scripting/install/installing-powershell?view=powershell-7.1)からダウンロードできます。
1. `kanji-explainer.ps1`ファイルを右クリックし、`編集`を選択します。`kanji-explainer-env`フォルダへのパスを、コンピュータ上の`kanji-explainer-env`フォルダへのパスに置き換えます。
2. **ショートカットを作成**:
    - デスクトップで右クリックし、`新規 > ショートカット`を選択します。
    - 位置フィールドに、`powershell.exe -File "C:\path\to\kanji-explainer.ps1"`と入力し、`C:\path\to\kanji-explainer.ps1`を`kanji-explainer.ps1`ファイルへのパスに置き換えます。

3. **キーボードショートカットを設定**:
    - 新しく作成されたショートカットを右クリックし、`プロパティ`を選択します。
    - `ショートカット`タブで、`ショートカットキー`フィールドをクリックし、使用するキーの組み合わせを押します。例: `Ctrl + Alt + K`。
    - `OK`をクリックして変更を保存します。

これで、漢字をコピーしてキーボードショートカットを押すと、スクリプトが実行されます。