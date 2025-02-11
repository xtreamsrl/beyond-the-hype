# Beyond the Hype: Building and Evaluating Robust RAG Systems

Building a Retrieval-Augmented Generation (RAG) system that actually works is harder than it looks. Great retrieval?
Not enough. Fancy prompts? Still not enough. Without rigorous evaluation, you're just guessing.

This workshop is all about evaluation-driven development—a structured way to measure, diagnose, and improve
your RAG system without the trial-and-error chaos.
We’ll see a pragmatic, effective and relatively easy way of bootstrapping an evaluation system, show how to fix what’s
broken, and give you a clear roadmap to iterate with confidence.

By the end, you’ll know how to go beyond the hype and build a RAG system that truly delivers. 🚀

**name** | **open in**
:-----: | :-------:
[Embed Movies into Vectors](./notebooks/00-datasets_builder.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/movies-buddy/blob/main/notebooks/00-dataset_builder.ipynb)
[Simple RAG Pipeline](./notebooks/01-first-rag.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/movies-buddy/blob/main/notebooks/01-first-rag.ipynb)
[You Need a Domain Expert](./notebooks/02-domain-expert.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/movies-buddy/blob/main/notebooks/02-domain-expert.ipynb)
[LLM-As-a-Judge](./notebooks/03-llm-as-a-judge.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/movies-buddy/blob/main/notebooks/03-llm-as-a-judge.ipynb)
[HyDE: Hypothetical Document Embeddings](./notebooks/04-HyDE.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/movies-buddy/blob/main/notebooks/04-HyDE.ipynb)
[Leverage Metadata To Enanche Retrieval](./notebooks/05-improve-metadata-search.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/movies-buddy/blob/main/notebooks/05-improve-metadata-search.ipynb)


## 🤗 How to contribute

1. Clone the repo.

> [!NOTE]
> The project uses Python 3.12

2. Install `uv`, following the [official docs](https://docs.astral.sh/uv/getting-started/installation/)

3. Run the following:

```bash
uv sync
```

4. It is highly recommended to use `nbstripout` to avoid pushing the output of Jupyter Notebooks.
   Install it with:

```bash
uv run pre-commit install --install-hooks
```
