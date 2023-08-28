from questions.question_3 import word_frequency

def test_word_frequency():
    result = word_frequency("This is a test sentence. This sentence is a test.")

    assert result == {"this": 2, "is":2, "a":2, "test": 2, "sentence":2} 