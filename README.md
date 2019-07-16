# tartar_sauce
Tarfile iterators and helpers to read archived files without extracting them.

## Examples of Usage:
### Generate Lines from all files in the archive:
```python
In [1]: import tartar_sauce

In [2]: reader = tartar_sauce.read_archive('test/test_archive.tar.gz')

In [3]: for line in reader:
   ...:     print(line)
   ...:
Here is a line.

Here is another.

Yet another Line here.

01

23

abc

123
```

### Generate Lines from specific files (using fnmatch patterns) within the archive:
```python
In [1]: import tartar_sauce

In [2]: reader = tartar_sauce.read_archive('test/test_archive.tar.gz', sub_file_name='a', include_filename=True)

In [3]: next(reader)
Out[3]: 'temp/a'

In [4]: next(reader)
Out[4]: 'Here is a line.\n'
```
