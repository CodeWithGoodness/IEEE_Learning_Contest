import twtrr


#from twtrr import shorten


def test_shorten():
    assert twtrr.shorten("jexeuse") == "jxs"
    assert twtrr.shorten("gooOdness") == "gdnss"
    assert twtrr.shorten("giant") == "gnt"


