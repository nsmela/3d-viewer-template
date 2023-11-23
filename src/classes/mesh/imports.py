from OCC.Extend.DataExchange import read_step_file, read_stl_file

from pathlib import Path

def read_3d_file(filename: str, *args, **kwargs):
    """import a model file and generate a shape for it"""
    filepath = Path(filename)

    # make sure the path exists otherwise OCE get confused
    if not filepath.exists():
        raise AssertionError(f"file does not exist: {filepath}")

    file_type = filepath.suffix

    if file_type == ".stl":
        return read_stl_file(filepath)
    elif file_type == ".step" or file_type == ".stp":
        return read_step_file(filepath)
    else:
        print(f"Invalid model file! {filepath} : {filepath.suffix}")

    return None
