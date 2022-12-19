# distance.py

## Notes

The `tabulate` and `haversine` modules may need to be installed prior to running this application. Your IDE may provide the option to install them by right-clicking the module name in the source code. If not, use the IDE terminal and run the commands:

* `pip install tabulate`

* `pip install haversine`

## Usage

Using the IDE terminal, or the command line, usage is as follows:

`distance.py` `[-h]` `[-n [N]]`

Using the `-h` argument provides a help message in the terminal.

The optional `-n` argument takes an integer. If no argument is provided, the default length of `places.csv` is used. If an integer is provided, `N` random places from `places.csv` are selected for use.

For example, valid inputs are:

`distance.py -h`

`distance.py -n 4`

`distance.py`

The program then outputs the pairs of places, and the corresponding air distance between all pairs. Finally, the average air distance and the pair with the distance closest to this average are given as output.
