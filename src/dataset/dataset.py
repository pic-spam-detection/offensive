from torch.utils.data import Dataset
import pandas as pd


class SpamDataset(Dataset):
    def __init__(
        self,
        csv_file="enron_spam_data.csv",
        split="train",
        test_split_ratio=0.1,
        max_n_rows=1_000,
        content_max_length=200,
    ):
        self.content_max_length = content_max_length
        self.data_frame = pd.read_csv(csv_file).dropna()
        self.data_frame = self.data_frame[: min(len(self.data_frame), max_n_rows)]

        n_rows = len(self.data_frame)

        if split == "train":
            self.data_frame = self.data_frame.iloc[
                0 : int(n_rows * (1 - test_split_ratio))
            ]
        else:
            self.data_frame = self.data_frame.iloc[
                int(n_rows * (1 - test_split_ratio)) :
            ]

    def __len__(self):
        return len(self.data_frame)

    def __getitem__(self, idx):
        label = 0 if self.data_frame.iloc[idx]["Spam/Ham"] == "ham" else 1
        text = self.data_frame.iloc[idx]["Message"]
        title = self.data_frame.iloc[idx]["Subject"]

        return {"label": label, "message": text, "subject": title}
