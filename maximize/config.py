def setup_ampl():
    import os, sys, subprocess
    from amplpy import AMPL

    caminho_mod = subprocess.check_output([sys.executable, "-m", "amplpy.modules", "path"]).decode().strip() 
    os.environ["PATH"] += os.pathsep + caminho_mod

    ampl = AMPL()
    ampl.eval("option solver cbc;")
    return ampl