"""AMPL instance factory shared by every model in this repository.

Centralizes solver setup so each script only worries about the model itself.
"""

import os
import subprocess
import sys

from amplpy import AMPL


def setup_ampl(solver: str = "cbc") -> AMPL:
    """Create an AMPL instance configured with the given solver.

    Adds the amplpy solver modules to PATH (required for the bundled
    open-source solvers such as CBC and HiGHS), then returns a ready-to-use
    AMPL instance.
    """
    modules_path = subprocess.check_output(
        [sys.executable, "-m", "amplpy.modules", "path"]
    ).decode().strip()
    os.environ["PATH"] += os.pathsep + modules_path

    ampl = AMPL()
    ampl.option["solver"] = solver
    print(f"AMPL configured with solver {solver.upper()}")
    return ampl
