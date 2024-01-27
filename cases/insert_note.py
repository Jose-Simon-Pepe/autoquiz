from noteintroducer.format_selector import FormatSelector

def select_format(format:str=None,
                  format_storage=None,
                  note_reader_config=None,
                  format_selector = None):
    if None in [format,format_storage,note_reader_config]:
        raise ValueError()
    form_sel = FormatSelector(format_storage=format_storage,
                              note_reader_config=note_reader_config)
    form_sel.select_expected_note_format(format)
