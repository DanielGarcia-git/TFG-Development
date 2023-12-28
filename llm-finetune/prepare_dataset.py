from pathlib import Path
import sys

sys.path.append("llm-finetune/lit-gpt")
sys.path.append("llm-finetune/lit-gpt/scripts")

import prepare_alpaca
import prepare_dolly
import prepare_csv

# Extend with more dataset, own dataset

def prepare_dataset(
    model_name: str = "stabilityai/stablelm-base-alpha-7b",
    dataset: str = "",
    csv_path: str = ""
):
    checkpoint_dir = Path("llm-finetune/lit-gpt/checkpoints") / model_name

    if not dataset:
        print("Please provide the name of the dataset (alpaca | dolly | csv).")

    if dataset == "alpaca":
        prepare_alpaca.prepare(checkpoint_dir = checkpoint_dir)
    elif dataset == "dolly":
        prepare_dolly.prepare(checkpoint_dir = checkpoint_dir)
    elif dataset == "csv":
        if not csv_path:
            print("Please provide a CSV file with fine-tuning data as the csv_path argument.")
            print("The CSV file must contain three columns: instruction, input and output.")
            return
        prepare_csv.prepare(checkpoint_dir = checkpoint_dir, csv_path=csv_path)


if __name__ == "__main__":
    from jsonargparse import CLI

    CLI(prepare_dataset)
