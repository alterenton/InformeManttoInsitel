from pathlib import Path
import os
import subprocess
import sys


def main() -> None:
    project_dir = Path(__file__).resolve().parent
    base_dir = project_dir.parent

    azotea_dir = base_dir / "Azotea"
    sotano_dir = base_dir / "Sotano"

    aux_dir = project_dir / "auxiliares"
    out_dir = project_dir / "construido"
    main_tex = project_dir / "main.tex"

    aux_dir.mkdir(exist_ok=True)
    out_dir.mkdir(exist_ok=True)

    env = os.environ.copy()
    texinputs = os.pathsep.join([
        str(azotea_dir),
        str(sotano_dir),
        env.get("TEXINPUTS", "")
    ]).strip(os.pathsep)

    env["TEXINPUTS"] = texinputs

    cmd = [
        "lualatex",
        "--interaction=errorstopmode",
        f"--aux-directory={aux_dir}",
        f"--output-directory={out_dir}",
        str(main_tex),
    ]

    print("Ejecutando:", " ".join(cmd))
    print(f"Directorio de trabajo: {project_dir}")
    print("-" * 60)

    try:
        process = subprocess.Popen(
            cmd,
            cwd=project_dir,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
    except FileNotFoundError as exc:
        raise SystemExit(
            "No se encontró 'lualatex'. Verifica que TeX Live o MiKTeX esté instalado y en PATH."
        ) from exc

    assert process.stdout is not None
    for line in process.stdout:
        print(line, end="")
        sys.stdout.flush()

    return_code = process.wait()
    print("-" * 60)

    if return_code != 0:
        raise SystemExit(f"lualatex terminó con error (código {return_code})")


if __name__ == "__main__":
    main()