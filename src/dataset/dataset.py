from torch.utils.data import Dataset
import pandas as pd


class SpamDataset(Dataset):
    def __init__(self, tokenizer, csv_file='enron_spam_data.csv', split='train', test_split_ratio=0.1, max_n_rows=1_000, content_max_length=200):
        self.content_max_length = content_max_length
        self.data_frame = pd.read_csv(csv_file).dropna()
        self.data_frame = self.data_frame[:min(len(self.data_frame), max_n_rows)]

        n_rows = len(self.data_frame)

        if split == 'train':
          self.data_frame = self.data_frame.iloc[0:int(n_rows * (1 - test_split_ratio))]
        else:
          self.data_frame = self.data_frame.iloc[int(n_rows * (1 - test_split_ratio)):]

        self.tokenizer = tokenizer

    def __len__(self):
        return len(self.data_frame)

    def __getitem__(self, idx):
        label = 0 if self.data_frame.iloc[idx]['Spam/Ham'] == 'ham' else 1
        text = self.data_frame.iloc[idx]['Message']
        title = self.data_frame.iloc[idx]['Subject']

        text_tokenized = self.tokenizer(text, padding='max_length', truncation=True, max_length=self.content_max_length, return_tensors='pt')
        title_tokenized = self.tokenizer(title, padding='max_length', truncation=True, max_length=self.content_max_length, return_tensors='pt')

        return {
            'label': label,
            'text': text,
            'title': title,
            'text_tokenized': text_tokenized['input_ids'].squeeze(0),  # Remove the batch dimension
            'title_tokenized': title_tokenized['input_ids'].squeeze(0),
            'text_tokenized_attention_mask': text_tokenized['attention_mask'].squeeze(0),
            'title_tokenized_attention_mask': title_tokenized['attention_mask'].squeeze(0)
        }
