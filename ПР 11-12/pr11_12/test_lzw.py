from hypothesis import given
from hypothesis.strategies import characters, text
import lzw

# only bytes strings supported!
@given(x=text(alphabet=characters(max_codepoint=255)))
def test_property(x):
    assert lzw.decompress(lzw.compress(x)) == x


test_property()
