import requests
import json
from typing import Union, List

from togetherai.prompt_provider import ranking_prompt
from togetherai.log_factory import logger
from togetherai.config import cfg


def rank_topics(prompt) -> List[str]:
    endpoint = "https://api.together.xyz/inference"
    res = requests.post(
        endpoint,
        json={
            "model": cfg.together_model,
            "max_tokens": 1024,
            "prompt": f"[INST]{prompt}[/INST]",
            "request_type": "language-model-inference",
            "temperature": 0.0,
            "top_p": 0.7,
            "top_k": 50,
            "repetition_penalty": 1,
            "stop": ["[/INST]", "</s>"],
            "negative_prompt": "",
            "repetitive_penalty": 1,
            "update_at": "2024-01-10T11:16:19.767Z",
        },
        headers={
            "Authorization": f"Bearer {cfg.together_api_key}",
        },
    )
    text = res.text
    parsed_dict = json.loads(text)
    res = []
    try:
        if "output" in parsed_dict:
            output = parsed_dict["output"]
            if "choices" in output:
                choices = output["choices"]
                for choice in choices:
                    if "text" in choice:
                        ranked = json.loads(choice["text"])
                        for q in ranked:
                            res.append(q)
    except:
        logger.exception("Could not rank files with togetherai")
    return res


if __name__ == "__main__":
    ranked_topics = rank_topics(ranking_prompt)
    for rt in ranked_topics:
        print(rt)
