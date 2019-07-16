"""Helpers for working with Tarfile archives."""

import fnmatch
import os
import tarfile

from typing import Generator


def read_archive(
        filename: str,
        sub_file_name: str = None,
        include_filename: bool = False
) -> Generator:
    """Iterate lines from files within a Tarfile archive.

    Args:
        filename: A TAR archive to generate lines from.
        sub_file_name: The name of a single file name within the archives.
        include_filename: Also include the filename with each sub-file read.

    Yield:
        A line from the archived file(s).
    """
    with tarfile.open(filename) as archive:
        archived_files = archive.getmembers()
        if sub_file_name:
            # Filter by file type in the basename of the file.
            sub_file_names = []
            included = fnmatch.filter([os.path.basename(archived.name) for archived in archived_files], sub_file_name)
            if not included:
                raise KeyError(f'Sub-file type "{sub_file_name}" not found in the archive.')
            for archived in archived_files:
                if os.path.basename(archived.name) in included:
                    sub_file_names.append(archived)
        else:
            # Include all archived files.
            sub_file_names = archived_files

        for sub_file in sub_file_names or []:
            filename_given = False
            if not sub_file.isfile():
                # Skip directories
                continue
            # Temporarily unpack the file for reading
            extracted = archive.extractfile(sub_file.name)
            if include_filename and filename_given is False:
                # First yield the archived filename for reference.
                yield sub_file.name
                filename_given = True

            # Iterate over lines and decode them from the unpacked file:
            for line in extracted:
                if include_filename:
                    if not filename_given:
                        yield sub_file.name
                        filename_given = True
                # Decode binary lines to UTF-8.
                if hasattr(line, 'decode'):
                    try:
                        line = line.decode('utf-8')
                    except UnicodeDecodeError:
                        continue
                yield str(line)

