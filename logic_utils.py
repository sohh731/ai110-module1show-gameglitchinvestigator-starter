def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # FIX: Refactored check_guess from app.py to logic_utils.py using Copilot to organize code and enable testing.
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            # FIX: Corrected reversed hint for "Too High" from "Go HIGHER!" to "Go LOWER!" based on Copilot's analysis of the FIXME comments.
            return "Too High", "📉 Go LOWER!"
        else:
            # FIX: Corrected reversed hint for "Too Low" from "Go LOWER!" to "Go HIGHER!" based on Copilot's step-by-step debugging guidance.
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        # FIX: Fixed hints in TypeError branch (string comparison) using Copilot's identification of the issue during live testing.
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "� Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
