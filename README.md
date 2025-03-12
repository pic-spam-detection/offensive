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

### Environment variables

Create a file in the root of this project and name it `.env`. In this file you can safely store access tokens and other confidential data. It will be ignored by `git`.

#### GPT API key

Before running any scripts that use GPT model, put the following content in the `.env` file:

```
// .env
GPT_API_KEY=<put-api-key-here>
GPT_ENDPOINT=<put-gpt-url-endpoint-here>
```

#### Hugging Face token

To access Hugging Face models, add your HF token into the `.env` file:

```
// .env
HF_TOKEN={your access token}
```

## **Usage**

@TODO Update usage

### Generate

```bash
python main.py generate --n_samples <n_samples> --output <output_filepath> --model <model_name>
```

The results will be saved in a CSV file in the format used by Enron dataset (https://github.com/MWiechmann/enron_spam_data).

| Column   | Explanation                                                                                                                                                                                                                        |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Subject  | The subject line of the e-mail                                                                                                                                                                                                     |
| Message  | The content of the e-mail. Can contain an empty string if the message had only a subject line and no body. In case of forwarded emails or replies, this also contains the original message with subject line, "from:", "to:", etc. |
| Spam/Ham | Has the values "spam" or "ham". Whether the message was categorized as a spam message or not.                                                                                                                                      |
| Date     | The date the e-mail arrived. Has a YYYY-MM-DD format.                                                                                                                                                                              |

### Evaluate

```bash
python main.py evaluate --
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

- Update pipeline
- Run LLM on enron dataset to get summaries of each email (include this in a dataset to analyse common themes of spam emails)
