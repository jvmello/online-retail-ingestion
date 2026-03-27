import sys

from jobs.constants import STEPS


def run_step(step_name: str, step_func) -> None:
    print(f"\n=== START: {step_name} ===")
    try:
        step_func()
        print(f"=== SUCCESS: {step_name} ===\n")
    except Exception as exc:
        print(f"=== FAILED: {step_name} ===")
        print(f"Error: {exc}")
        raise


def main() -> None:
    print("Starting full lakehouse pipeline...")

    try:
        for step_name, step_func in STEPS:
            run_step(step_name, step_func)
    except Exception:
        print("Pipeline aborted due to failure.")
        sys.exit(1)

    print("Pipeline finished successfully.")


if __name__ == "__main__":
    main()