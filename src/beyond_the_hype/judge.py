"""Collections of utils for LLM as a Judge."""

from collections.abc import Callable

import polars as pl
from openai import OpenAI
from pydantic import BaseModel


class EvaluationExample(BaseModel):
    """Contains an example for LLM as a judge."""

    question: str
    response: str
    outcome: str
    critique: str


class LLMJudgeDataset(BaseModel):
    """Contains the format for LLM as a Judge output."""

    critiques: list[EvaluationExample]


JUDGE_SYSTEM_MESSAGE = """You are a movie expert chatbot evaluator with
advanced capabilities to understand if the question response is good or not.
Follow some guidelines to evaluate the system:
{guidelines}

We provide you with some examples to give you an idea of how a good response should be.
Evaluation examples:
{examples}
"""


EXAMPLE_STRUCTURE = """<user_question>{question}</user_question>
<response>{response}</response>
<outcome>{outcome}</outcome>
<critique>{critique}</critique>"""


evaluation_guidelines = [
    'Provide a "pass" or "fail" outcome. No other category is admitted.',
    "Provide a comprehensive and clear explanation of "
    'why you gave that outcome. In particular for the "fail" one',
]


examples = [
    EvaluationExample(
        question="Could you suggest an action movie?",
        response='I recommend "The Thousand Faces of Dunjia" (2017), '
        "directed by Yuen Woo-ping. "
        "The film follows a group of swordsmen's adventures as they secretly "
        "protect humanity by hunting "
        "down mysterious creatures from outer space. It combines action "
        "and fantasy elements, "
        "making it an engaging watch for fans of the genre. Enjoy!",
        outcome="pass",
        critique="The system replied with an action movie correctly. "
        "The response is brief but well explained.",
    ),
    EvaluationExample(
        question="Give me a summary of DUNE II",
        response="I'm sorry, but I don't have information about \"Dune II.\" "
        "My expertise covers movie plots, metadata, and summaries of films, "
        "but it seems that title isn't available in my current context. "
        "If you have any questions about other movies, feel free to ask!",
        outcome="fail",
        critique="The system should reply to questions regarding movie summaries. "
        "It seems that can't find the movie in the context.",
    ),
]


def llm_as_a_judge(
    questions: pl.DataFrame,
    client: OpenAI,
) -> pl.DataFrame:
    """Evaluate a list of questions using the LLM as a judge.

    Args:
        questions: A dataset of questions.
        client: An OpenAI client.

    Returns:
        A dataset with the questions, the answers, and the critiques.

    """
    formatted_system_message = _build_evaluation_system_message(
        JUDGE_SYSTEM_MESSAGE,
        evaluation_guidelines,
        examples,
    )

    formatted_questions = (
        questions.select(
            pl.format(
                "Question: {}\nAnswer: {}\n\n",
                pl.col("question"),
                pl.col("rag_answer"),
            ),
        )
        .to_series(0)
        .str.join("\n")
        .item()
    )

    prompt = f"""Evaluate how our AI system answered the given questions.
    Here is the list of question and answer couples: {formatted_questions}"""

    chat_completion = client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": formatted_system_message},
            {"role": "user", "content": prompt},
        ],
        response_format=LLMJudgeDataset,
    )

    llm_judge_outcome = chat_completion.choices[0].message.parsed

    return pl.from_dicts(llm_judge_outcome.model_dump()["critiques"])


def answer_multiple_questions(questions: pl.DataFrame, ask: Callable) -> pl.DataFrame:
    """Utility function to answer multiple questions using the ask function.

    Args:
        questions: A dataset of questions.
        ask: A function that receives a question and returns an answer.

    Returns:
        A dataset with the questions and the ask answers.

    """
    return questions.with_columns(
        pl.col("question")
        .map_elements(
            lambda question: ask(question).choices[0].message.content,
            return_dtype=pl.String,
        )
        .alias("rag_answer"),
    )


def _build_evaluation_examples(example: EvaluationExample) -> str:
    return EXAMPLE_STRUCTURE.format(
        question=example.question,
        response=example.response,
        outcome=example.outcome,
        critique=example.critique,
    )


def _build_evaluation_system_message(
    system_message: str,
    guidelines: str,
    examples: list[EvaluationExample],
) -> str:
    formatted_guidelines = "\n".join(guidelines)
    formatted_examples = "\n\n".join(
        [_build_evaluation_examples(ex) for ex in examples],
    )
    return system_message.format(
        guidelines=formatted_guidelines,
        examples=formatted_examples,
    )
