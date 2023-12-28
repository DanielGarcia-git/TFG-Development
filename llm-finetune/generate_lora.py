from pathlib import Path
import sys

sys.path.append("llm-finetune/lit-gpt")
sys.path.append("llm-finetune/lit-gpt/generate")

import lora


def generate(
    model_name: str = "meta-llama/Llama-2-7b-hf",
    prompt: str = ""
):
    lora.main(
        prompt = prompt,
        checkpoint_dir = Path("llm-finetune/lit-gpt/checkpoints") / model_name,
        lora_path = Path("out/lora/dolly/lit_model_lora_finetuned.pth"),
        precision = "16-true",
        quantize = "bnb.nf4",
    )


if __name__ == "__main__":
    from jsonargparse import CLI

    CLI(generate)