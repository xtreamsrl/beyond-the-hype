"""Provide functions for data imports and management."""

from pathlib import Path

import polars as pl


def get_movies_dataset(sample: int = 0, *, local: bool = False) -> pl.DataFrame:
    """Retrieve a dataset of movies with embeddings vectors.

    Args:
        sample: number of rows to sample from the dataset.
        local: whether to load the dataset from a local file or from the web.

    Returns:
        A dataset of movies with their plots.

    """
    file_name = "movies_plots_dataset_embd_minilm.parquet"
    if local:
        here = Path(__file__)
        source = here.parent.parent.parent / "data" / file_name
    else:
        source = f"https://raw.githubusercontent.com/xtreamsrl/beyond-the-hype/main/data/{file_name}"

    if sample:
        return pl.read_parquet(source).sample(sample)

    return pl.read_parquet(source)
