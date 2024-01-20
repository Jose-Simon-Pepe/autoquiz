from noteintroducer.format_selector import FormatSelector 
from noteintroducer.protocols.supported_formats_storage import SUPPORTEDFORMATSSTORAGE

"""Format Selector Component"""

class FormatStorageStub(SUPPORTEDFORMATSSTORAGE):
    def __init__(self):
        self.supported_formats = ['format1','format2']
    def get_all(self):
        return self.supported_formats


format_storage_stub = FormatStorageStub()


def test_sut_should_get_all_supported_formats():
    supported_formats = ['format1','format2']
    sut = FormatSelector(format_storage=format_storage_stub)
    assert sut.get_all_format() == supported_formats
    

def test_sut_should_load_all_supported_formats_up_on_start():
    assert FormatSelector(format_storage_stub).get_all_format() is not None