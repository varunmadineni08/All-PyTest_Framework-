import pytest
import sys

########Skip Marker in pytest#########################
@pytest.mark.skip(reason="feature not yet ready")
def test_sample_five():
    assert True

############SkipIf Marker in pytest############################
login_enabled=False
@pytest.mark.skipif(not login_enabled,reason="feature is disabled")
def test_skip_if():
    assert True
##########################################################

@pytest.mark.skipif(sys.version_info < (3, 9), reason="Needs Python 3.9 or higher")
def test_new_language_feature():
    assert True
##############################################################

@pytest.mark.skipif(sys.platform == "win32", reason="Not supported on Windows")
def test_linux_only_feature():
    assert True

####################OR##################
@pytest.mark.skipif(sys.platform.startswith("win"), reason="Not supported on Windows")
def test_linux_only():
    assert True
