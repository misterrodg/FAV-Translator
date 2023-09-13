# FAV-Translator

A simple Python-based Fixed Airspace Volume translator.

## Requirements

Python 3.8 or Later (Tested with Python 3.9.13)

Only imports are `argparse`, `csv` and `os`, so it should run on a standard Python implementation.

## Instructions for use

1. Copy or move (the original file will not be overwritten) the file into the `source` directory.
2. Run the following command:

```
python3 translate.py --filename=[FAV Filename]
```

Example:

```
python3 translate.py --filename=2201_FAV.csv
```

3. The resulting files will be found in the `output` directory.

# Contributions

Want to contribute? Check out the [Open Issues](https://github.com/misterrodg/FAV-Translator/issues), fork, and open a [Pull Request](https://github.com/misterrodg/FAV-Translator/pulls).

Additional contributors will be listed here.

# License

This is licensed under [GPL 3.0](./LICENSE).
