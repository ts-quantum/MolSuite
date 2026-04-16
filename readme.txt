MoleculeSuite for Linux (x86_64 & ARM64)
This repository provides standalone, pre-packaged bundles of MolVista and OrbVista for Linux systems. 
These bundles include a fully isolated Python environment to ensure stability across different 
distributions (Fedora, Ubuntu, etc.) and architectures.
Included Tools
MolVista: 3D Molecule and Trajectory Viewer.
OrbVista: Quantum Chemistry Orbital & Isosurface Visualizer (powered by PySCF).

For a more detailed documentation as well as examples so the orignal github repositories.
There you can also find macOS releases.
MolVista: https://github.com/ts-quantum/MolVista
OrbVista: https://github.com/ts-quantum/OrbVista

## System Requirements (Linux)

Even when using the provided conda environment, ensure your host system has the necessary X11/XCB libraries installed. On Debian-based systems (Ubuntu, Mint, etc.), run:

```bash
sudo apt update
sudo apt install libxcb-cursor0 libx11-xcb1 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-render-util0 libxcb-xinerama0 libxcb-xkb1 libxkbcommon-x11-0 libdbus-1-3

Installation

1. Download the appropriate archive for your architecture from the Releases page:
MolSuite_Linux_x86_64.tar.xz (for standard PCs/Intel/AMD)
MolSuite_Linux_ARM64.tar.xz (for ARM64 devices, e.g., Raspberry Pi, Pinebook, Fedora ARM)

2.Extract the archive:
tar -xzvf MolSuite_Linux_ARCH.tar.gz
cd MolSuite_Linux_ARCH

3. Run the Setup:
This script creates desktop shortcuts and registers the apps in your application menu.
(edit path *.desktop files!!)
bash setup_all.sh

Usage

From Desktop: Launch MolVista or OrbVista directly from your application menu (Launcher).
From Terminal:

./MolVista_run
./OrbVista_run

Troubleshooting (Remote / Legacy Graphics)
If you are using a Remote Desktop (VNC/RDP) or encounter graphics issues, you can force software rendering by setting the following variable before launch:

export LIBGL_ALWAYS_SOFTWARE=1
./MolVista_run

Alternative Option: Manual Setup (Lightweight Option)
If you want to avoid downloading the full pre-packaged bundle (~600 MB), you can perform a 
manual installation. This approach is much more lightweight as you only download the source 
files and let Conda/Mamba handle the dependencies locally.


    1. Install Miniconda3 and start a new conda session.
    2. Create the environment from the provided environment.yml file:
    mamba env create --prefix ./env -f environment.yml
    3. Run the application:
    Activate the environment and start the main script: 
    conda activate ./env
    python main.py
    4. Optional: Package for portability (requires conda-pack):
    To create a portable archive of your environment, run:  
    conda install conda-pack
    conda-pack -p ./env -o "your_env.tar.gz"


Credits & License
These tools are built using an open-source stack including PySide6, PyVista, VTK, and PySCF.
The suite is bundled using Conda-forge to ensure reproducible scientific environments.
For detailed license information for all bundled libraries, see the CREDITS.html or the env/share/licenses directory.
