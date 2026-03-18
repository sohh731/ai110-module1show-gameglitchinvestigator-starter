from logic_utils import check_guess

def test_winning_guess():
    # FIX: Updated test to unpack tuple and check message, using Copilot's guidance on pytest best practices.
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct!" in message

def test_guess_too_high():
    # FIX: Updated test to verify hint message correctness, targeting the bug fixed with Copilot's help.
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "Go LOWER!" in message

def test_guess_too_low():
    # FIX: Updated test to check "Go HIGHER!" hint, ensuring fix with Copilot's debugging.
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "Go HIGHER!" in message
