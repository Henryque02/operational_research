"""AMPL instance factory shared by every model in this repository.

Centralizes solver setup so each script only worries about the model itself.
"""

from amplpy import AMPL


def setup_ampl(solver: str = "cbc") -> AMPL:
    """Create an AMPL instance configured with the given solver.

    The AMPL engine and solvers (CBC, HiGHS) are installed as the
    ``ampl-module-*`` packages declared in ``pyproject.toml``, so amplpy
    locates their binaries automatically — no PATH tweaking needed.
    """
    ampl = AMPL()
    ampl.option["solver"] = solver
    print(f"AMPL configured with solver {solver.upper()}")
    return ampl
