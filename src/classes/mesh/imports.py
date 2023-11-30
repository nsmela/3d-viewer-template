from OCC.Extend.DataExchange import read_step_file, read_stl_file

from pathlib import Path


def read_3d_file(filename: str, *args, **kwargs):
    """import a model file and generate a shape for it"""
    filepath = Path(filename)

    # make sure the path exists otherwise OCE get confused
    if not filepath.exists():
        raise FileNotFoundError(f"file does not exist: {filepath}")

    file_type = filepath.suffix.lower()

    if file_type != ".stl" and file_type != ".step" and file_type != ".stp":
        raise AssertionError(f"cannot read files of type {file_type} need to be .stl, .step or .stp")

    file = filepath._str
    
    try:
        if file_type == ".stl":
            return read_stl_file(filepath._str)
        else:
            return read_step_file(filepath._str)
    except AssertionError as error_message:
        raise AssertionError(error_message)
