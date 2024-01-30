from browser_agent.runner import run_steps
from browser_agent.steps import Step


def test_run_steps_serializes_actions() -> None:
    out = run_steps([Step("click", "#login")])
    assert out == ["click:#login"]


def test_run_steps_keeps_order() -> None:
    out = run_steps([Step("fill", "#email"), Step("click", "#submit")])
    assert out == ["fill:#email", "click:#submit"]
