from questions.question_1 import is_balanced

def test_is_balanced_returns_true():
    result = is_balanced("([]{})")
    assert result == True

def test_is_balanced_returns_false():
    result = is_balanced("([)]")
    assert result == False