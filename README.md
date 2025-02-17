# ⚔️ Équipe Offense : Génération de Spams

## **Objectif**

Ce repository contient les travaux de l’équipe Offense pour :

- Générer automatiquement des **emails frauduleux indétectables** à l’aide d’IA générative (LLMs).
- Tester nos attaques face au modèle défensif de l’équipe adverse.

## **Installation**

Cloner le dépôt `git`:

```bash
git clone git@github.com:pic-spam-detection/offensive.git
cd offensive
```

Installer les librairies nécessaires :

```bash
pip install torch transformers datasets click
```

## **Usage**

```bash
python spam_generation.py --model <model_name>
```

Il faut spécifier le modèle à utiliser pour génerer les mails. Options :

- `llm`. Un modèle qui se base sur un LLM. **Attention** : ce modèle peut prendre un temps important d'installation. À utiliser avec GPU.
- `dataset`. Un modèle qui effectue un tirage au sort à partir d'un dataset spécialisé (https://huggingface.co/datasets/TrainingDataPro/email-spam-classification).

Le nombre de mails à génere peut être spévifié via `--n_samples` (5 par défaut). Par exemple :

```bash
python spam_generation.py --model "dataset" --n_samples 10
```

D'autres modèles seront ajouter dans l'avenir.

Si multiples versions de Python sont disponibles sur votre ordinatuer, utilisez Python 3:

```bash
python3 spam_generation.py --model <model_name>
```

## **Known issues**

- In case if auto-formatting does not work in VS Code, it can be run manually (reference: https://github.com/microsoft/vscode-python/issues/6495):

```bash
autopep8 --max-line-length 60 --in-place --aggressive --aggressive <your_file>.py
```
