import matplotlib.pyplot as plt
import glob

from pwtools import io


def create_energy_volume_data_file():
    """
    Reads energy and volume data from '*.pwo' files and writes to 'energy_volume_data.txt'.

    This function searches for all '*.pwo' files in the current directory. For each file,
    it reads the total energy and volume using the `pwtools` library. If both energy and
    volume are available (non-None), the function writes them to 'energy_volume_data.txt'.
    In case of missing data (None values), an error message is written to 'error.txt'.

    Writes energy and volume data to 'energy_volume_data.txt' and logs errors in 'error.txt'.
    """

    pwo_files = glob.glob('*.pwo')
    error_occurred = False

    for pwo_file in pwo_files:
        out = io.read_pw_scf(pwo_file)

        if out.volume is not None and out.etot is not None:
            with open('energy_volume_data.txt', 'a') as file:
                file.write(f'{out.volume} {out.etot}\n')
        else:
            with open('error.txt', 'a') as file:
                file.write(f"Volume or energy is None for the file {pwo_file}.\n")
            error_occurred = True

    return not error_occurred


def plot_energy_vs_volume(file_pattern, output_graph):
    """
    Generates a plot of energy vs. volume from data files matching a specified pattern.

    Parameters:
    file_pattern (str): Pattern to match for input data files ('energy_volume_data.txt').
    output_graph (str): File name for the output graph image ('energy_volume_graph.png').
    """

    volume_energy_pairs = []

    # Gather volume-energy pairs from files
    for file_path in glob.glob(file_pattern):
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    volume, energy = map(float, line.split())
                    volume_energy_pairs.append((volume, energy))
                except ValueError:
                    print(f"Invalid data in file {file_path}, skipping line.")

    if not volume_energy_pairs:
        print("No valid volume-energy data found.")
        return

    # Sort pairs by volume
    volume_energy_pairs.sort(key=lambda pair: pair[0])

    # Unpack pairs into separate lists
    volume_lst, energy_lst = zip(*volume_energy_pairs)

    # Plotting
    plt.plot(volume_lst, energy_lst)
    plt.xlabel("Volume")
    plt.ylabel("Energy")
    plt.savefig(output_graph)
    plt.show()

    print(f"Graph saved as {output_graph}")


if __name__ == '__main__':
    success = create_energy_volume_data_file()

    if success:
        plot_energy_vs_volume(
            file_pattern='energy_volume_data.txt',
            output_graph='energy_volume_graph.png'
        )
