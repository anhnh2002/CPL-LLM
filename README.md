### ChatGPT
You need to first apply for an [OpenAI account](https://platform.openai.com/), and then buy the OpenAI API to get your own **API key**. Then set your key in `config.ini`.

## Steps
 ```
  git clone https://github.com/nguyenhoanganh2002/CPL-LLM.git
  cd CPL-LLM
  pip install -r requirements.txt
  
  python mistral-train.py --task_name FewRel --num_k 5 --num_gen 2
  python mistral-train.py --task_name Tacred --num_k 5 --num_gen 5
  python train-mmi.py --task_name FewRel --num_k 5 --num_gen 2
  python train-mmi.py --task_name Tacred --num_k 5 --num_gen 5
```
