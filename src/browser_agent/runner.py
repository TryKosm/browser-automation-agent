from .steps import Step


def run_steps(steps: list[Step]) -> list[str]:
    return [f"{s.action}:{s.target}" for s in steps]
