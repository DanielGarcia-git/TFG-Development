MODEL=stabilityai/stablelm-base-alpha-7b
CHECKPOINT_PATH=$1

if [ ! -d lit-gpt ]; then
  git clone https://github.com/Lightning-AI/lit-gpt.git
fi

$HOME/soft/bin/pip install -r requirements.txt
$HOME/soft/bin/pip install huggingface_hub tokenizers sentencepiece safetensors
$HOME/soft/bin/pip install scipy bitsandbytes

pushd lit-gpt
$HOME/soft/bin/python scripts/download.py --repo_id $MODEL
$HOME/soft/bin/python scripts/convert_hf_checkpoint.py --checkpoint_dir checkpoints/$MODEL
