# ⚔️ Équipe Offense : Génération des Spams

## **Objectif**

Ce repository contient les travaux de l’équipe Offense pour :

- Générer automatiquement des **emails frauduleux indétectables** à l’aide d’IA générative (LLMs).
- Tester nos attaques face au modèle défensif de l’équipe adverse.

## **Quick start**

Clone `git` repo:

```bash
git clone git@github.com:pic-spam-detection/offensive.git
cd offensive
```

Install necessary dependencies:

```bash
pip install -r requirements.txt
```

### GPT API key

Before running any scripts that use GPT model, create a file in the root of this project and name it `.env`.
Then put the following content in the file:

```
GPT_API_KEY=<put-api-key-here>
```

## **Usage**

@TODO Update usage

### Generate

```bash
python main.py generate --n_samples <n_samples> --output <output_filepath> --model <model_name>
```

### Evaluate

```bash
python main.py evaluate --model <model_name>
```

---

If mutliple versions of Python are available, use Python 3. For example:

```bash
python3 main.py evaluate --model <model_name>
```

## **Known issues**

- In case if auto-formatting does not work in VS Code, it can be run manually (reference: https://github.com/microsoft/vscode-python/issues/6495):

```bash
autopep8 --max-line-length 60 --in-place --aggressive --aggressive <your_file>.py
```

## TODO

- Try different LLMs
- Run LLM on enron dataset to get summaries of each email (include this in a dataset to analyse common themes of spam emails)
- Add visualizaion
- Generate in the format of enron
