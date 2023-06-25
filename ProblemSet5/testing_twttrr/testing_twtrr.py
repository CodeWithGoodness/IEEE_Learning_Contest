import twtrr


#from twtrr import shorten


def test_shorten():
    assert twtrr.shorten("jexeuse") == "jxs"
    assert twtrr.shorten("goodness") == "gdnss"
    assert twtrr.shorten("giant") == "gnt"


