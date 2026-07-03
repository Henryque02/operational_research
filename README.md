# Operations Research — Linear Programming Portfolio

Optimization problems modeled and solved during the Operations Research course at UFG (Universidade Federal de Goiás), using **AMPL** via [`amplpy`](https://amplpy.ampl.com/) with open-source solvers (**CBC** and **HiGHS**) — plus a **Simplex algorithm implemented from scratch** with NumPy.

Problem statements are kept in Portuguese (as given in class) inside each module's docstring; code, identifiers, and outputs are in English.

## Projects

| # | Project | OR technique demonstrated | Solver |
|---|---------|---------------------------|--------|
| 01 | [`product_mix.py`](01_lp_maximization/product_mix.py) · [`aluminum_production.py`](01_lp_maximization/aluminum_production.py) | LP **maximization** — production mix with resource, demand, and ratio constraints | CBC |
| 02 | [`electronic_components.py`](02_lp_minimization/electronic_components.py) · [`electronic_components_extended.py`](02_lp_minimization/electronic_components_extended.py) · [`hydroponics_crops.py`](02_lp_minimization/hydroponics_crops.py) | LP **minimization** — cost minimization under minimum-demand constraints; scaling a model from 2 to 5 variables and from 2 to 4 constraints | CBC |
| 03 | [`petroleum_blending.py`](03_blending/petroleum_blending.py) · [`crop_planning.py`](03_blending/crop_planning.py) | **Blending problem** (12 variables, composition specs) and **equivalent model formulations** — same problem modeled with two different decision variables | HiGHS |
| 04 | [`bus_scheduling.py`](04_scheduling/bus_scheduling.py) | **Shift scheduling** — classic overlapping-shift fleet coverage problem | CBC |
| 05 | [`team_production.py`](05_production_allocation/team_production.py) · [`repair_services.py`](05_production_allocation/repair_services.py) · [`sample_testing.py`](05_production_allocation/sample_testing.py) | **Production allocation** — assigning products to teams (12-variable assignment-style LP) | CBC |
| 06 | [`simplex.ipynb`](06_simplex_from_scratch/simplex.ipynb) | ⭐ **Simplex algorithm implemented from scratch** with NumPy — full tableau iterations, pivot selection analysis, and comparison with textbook examples (Taha) | — |

The highlight is **project 06**: rather than only calling a solver, the notebook implements the Simplex tableau method manually, traces every iteration, and investigates what happens when the entering-variable rule is changed (least-negative vs. most-negative coefficient) — comparing results against the graphical method.

## Project structure

```
├── src/operational_research/   # shared package (AMPL/solver setup)
├── 01_lp_maximization/
├── 02_lp_minimization/
├── 03_blending/
├── 04_scheduling/
├── 05_production_allocation/
├── 06_simplex_from_scratch/
└── pyproject.toml
```

Each numbered folder contains standalone, runnable models. Problem statements provided as images live in each folder's `assets/`. All models share a single AMPL configuration through the `operational_research` package — no duplicated setup code.

## Running

Requires Python ≥ 3.12 and [uv](https://docs.astral.sh/uv/).

```bash
uv sync                                        # installs deps + the local package
uv run 01_lp_maximization/product_mix.py       # run any model
uv run jupyter notebook 06_simplex_from_scratch/simplex.ipynb
```

The first run downloads the open-source solver modules (CBC/HiGHS) automatically through `amplpy`.

## What I learned

- Translating word problems into LP formulations: choosing decision variables, writing objective functions and constraints
- Why the *choice* of decision variable matters for model clarity (see the two equivalent formulations in `03_blending/crop_planning.py`)
- Handling blending/composition constraints and overlapping-shift coverage constraints
- How the Simplex method actually works under the hood — tableau construction, pivot selection, and convergence behavior
- Structuring reusable solver configuration instead of duplicating boilerplate across models
