"""Utilities to generate synthetic data."""


def build_eval_dataset_builder_system_message(
    system_message: str,
    features: list[str],
    scenarios: list[str],
    personas: list[str],
) -> str:
    """Build a system message given features, scenarios and personas."""
    features = ", ".join(features)
    scenarios = ", ".join(scenarios)
    personas = ", ".join(personas)

    return system_message.format(
        features=features,
        scenarios=scenarios,
        personas=personas,
    )
