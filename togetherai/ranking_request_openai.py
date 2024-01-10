from typing import List
import asyncio
import json

from togetherai.log_factory import logger
from togetherai.config import cfg

from openai.types.chat.chat_completion import ChatCompletion

from togetherai.prompt_provider import ranking_prompt


async def create_completion(
    system_message: str, user_message: str, function_spec: dict = {}
) -> ChatCompletion:
    logger.info("completion user message: %s", user_message)
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ]
    kwargs = {}
    completion = await cfg.open_ai_client.chat.completions.create(
        model=cfg.together_model,
        temperature=cfg.temperature,
        messages=messages,
        functions=[function_spec],
        stream=False,
        **kwargs,
    )
    return completion


def extract_ranking(
    chat_completion: ChatCompletion
) -> List[str]:
    choices = chat_completion.choices
    if len(choices) > 0:
        first_choice = choices[0]
        return json.loads(first_choice.content)
    return []



if __name__ == "__main__":
    system_message = "You are a helpful JSON coder, that replies always using JSON"
    completion = asyncio.run(create_completion(system_message, ranking_prompt))
    logger.info(extract_ranking(completion))
