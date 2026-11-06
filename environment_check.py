"""Check the project Python environment and optional learning packages."""

import importlib.util
import sys


OPTIONAL_PACKAGES = {
    "numpy": "numpy",
    "pandas": "pandas",
    "matplotlib": "matplotlib",
    "seaborn": "seaborn",
    "requests": "requests",
    "scikit-learn": "sklearn",
    "jupyter": "jupyter",
}


def main():
    """Print environment checks and return a status code."""
    print("AIN7301 Python environment check")
    print(f"Python version: {sys.version.split()[0]}")
    print(f"Python executable: {sys.executable}")

    checks_passed = True
    try:
        import pip
    except ImportError:
        print("[FAIL] pip is not available in this environment.")
        print("       Resolve with: python -m ensurepip --upgrade")
        checks_passed = False
    else:
        print(f"[PASS] pip {pip.__version__} is available.")

    print("\nOptional learning libraries:")
    missing_packages = []
    for package_name, module_name in OPTIONAL_PACKAGES.items():
        if importlib.util.find_spec(module_name) is None:
            print(f"[INFO] {package_name} is not installed (optional for now).")
            missing_packages.append(package_name)
        else:
            print(f"[PASS] {package_name} is installed.")

    if missing_packages:
        print(
            "\nWhen a course activity needs an optional package, install it "
            "inside .venv with:"
        )
        print(f"  python -m pip install {' '.join(missing_packages)}")

    if checks_passed:
        print("\n[PASS] Python fundamentals are ready; no optional packages are required.")
        return 0

    print("\n[FAIL] Fix the required environment check(s) above.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
