<h1 align="center">⚗️ Molecular Weight Calculator</h1>

<p align="center">
    A lightweight command-line utility to parse chemical formulas and compute molecular mass from atomic weights.
</p>

<p align="center">
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License"></a>
</p>

A modular, zero-dependency Python CLI that parses molecular formula strings, tallies atom counts per element, and computes total molecular weight against a full periodic table of standard atomic weights.

## Install

Clone the repository directly:
```bash
git clone https://github.com/eben-vranken/molecular-weight-calc.git
cd molecular-weight-calc
```

## Usage

Pass a formula string with the `-f` / `--formula` flag. By default, it prints the total molecular weight.

```bash
python mol-weight-calc.py -f C6H12O6
```

### Verbose Breakdown

Use `-v` / `--verbose` for a detailed per-element table showing atom counts and mass contributions:

```bash
python mol-weight-calc.py -f C6H12O6 --verbose
```

## Configuration Matrix

| Argument | Option / Choices | Default | Description |
| --- | --- | --- | --- |
| `-f`, `--formula` | *Formula string* | *Required* | The chemical formula to parse and weigh. |
| `-v`, `--verbose` | *Flag* | `False` | Prints a detailed per-element breakdown table instead of just the total. |

## Feature Set

* **Full Periodic Table:** Atomic weights for all 118 elements, from hydrogen to oganesson.
* **Formula Parsing:** Reads one- and two-letter element symbols with optional atom counts (e.g. `C6H12O6`, `NaCl`).
* **Verbose Reporting:** Optional per-element table with unit mass and total mass contribution.

## License

MIT