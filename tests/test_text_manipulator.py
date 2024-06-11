from text_manipulation.text_manipulator import TextManipulator

def test_tokenize():
    text = "This is a test sentence."
    tm = TextManipulator(text)
    assert tm.tokenize() == ['This', 'is', 'a', 'test', 'sentence', '.']