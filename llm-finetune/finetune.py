from pathlib import Path
import sys

sys.path.append("llm-finetune/lit-gpt")
sys.path.append("llm-finetune/lit-gpt/finetune")

import generate
import lora

def finetune(
    model_name: str = "stabilityai/stablelm-base-alpha-7b",
    dataset: str = "alpaca"
):
    lora.setup(
        checkpoint_dir = Path("llm-finetune/lit-gpt/checkpoints") / model_name,
        data_dir = Path("data") / dataset,
        out_dir = Path("out/lora") / dataset,
        precision = "16-true",
        quantize = "bnb.nf4-dq",
    )


if __name__ == "__main__":
    from jsonargparse import CLI

    CLI(finetune)
