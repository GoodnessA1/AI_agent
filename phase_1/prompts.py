def zero_shot_prompt() -> tuple[str, str]:
    """No examples. Direct medical question from model base knowledge."""
    system, user = ..., ...
    return system, user

def few_shot_prompt() -> tuple[str, str]:
    """2–3 worked examples in system prompt defining the output format."""
    # YOUR TASK: Differential diagnosis formatting works well here.
    system, user = ..., ...
    return system, user

def chain_of_thought_prompt() -> tuple[str, str]:
    """Numbered reasoning steps enforced before the final answer."""
    # YOUR TASK: Model must not skip steps.
    system, user = ..., ...
    return system, user

def react_prompt() -> tuple[str, str]:
    """Thought → Action → Observation cycles. Pick a scenario needing multiple checks."""
    system, user = ..., ...
    return system, user

def negative_prompting_prompt() -> tuple[str, str]:
    """At least three Do NOT rules paired with matching DO rules."""
    system, user = ..., ...
    return system, user
