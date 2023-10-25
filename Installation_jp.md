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

## キーボードショートカットを使る手順
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

## キーボードショートカットを使う手順
> [!WARNING]
> この手順はまだでき上がっていません
1. **ショートカットを作成する**:
    - デスクトップの空のスペースで右クリックし、"新規(N)"を選んでから"ショートカット(S)"を選びます。
    - 位置フィールドに`C:\Windows\System32\cmd.exe /c path/to/kanji-explainer/kanji-explainer.bat %1`と入力し、次へをクリックします。
2. kanji-explainer.bat ファイルを右クリックし、"編集"を選びます。
2行目、3行目の `path\to\kanji-explainer` は、ダウンロードしたプロジェクトのパスに置き換えてください。
パスは、エクスプローラーでプロジェクトのフォルダを開き、アドレスバーに表示されているパスをコピーすることで確認できます。

3. **ショートカットを修正する**:
    - ショートカットが作成されたら、それを右クリックし、"プロパティ"を選びます。
    - ショートカットタブで、"対象(T)"フィールドを探します。
    - "対象(T)"フィールドの最後には、先に入力したコマンドが表示されているはずです。コマンドが正しいことを確認してください。

   **ホットキーを割り当てる**:
    - 同じ"プロパティ"ダイアログで、"ショートカットキー"とラベル付けされたフィールドがあります。このフィールドをクリックし、ショートカット用のキーの組み合わせを押します。例えば、"Ctrl + Alt + K"を押すと、このキーの組み合わせは、押される
