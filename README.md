# EV_Analysis

**Version:** 0.0.1

**Author:** J. Schaarschmidt

## Description

This script generates a plot of energy versus volume from a set of data files. This script is used for analyzing the relationship between energy and volume of a crystal structure after applying strain, and it visualizes the data in a graph format.

## Inputs
- `relax.pwo` file: The `relax.pwo` files are the output files from the `qe_run` script.

## Outputs
- Graph image: File name for the output graph image (e.g., `energy_volume_graph.png`).

## Dependencies
- Matplotlib
- Glob

## Notes
- The output graph provides a visual representation of how the energy of the structure varies with its volume, which is essential for understanding material properties.