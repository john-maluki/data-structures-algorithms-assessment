from questions.question_2 import remove_duplicates

def test_remove_duplicate():
    result = remove_duplicates([5,6,7,6,8,9,3,5,6,7,3,2,1,3,4])

    assert result == [5,6,7,8,9,3,2,1,4]