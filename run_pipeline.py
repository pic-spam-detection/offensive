import yaml
import subprocess


def run_pipeline(config_file):
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)

    n_steps = len(config["pipeline"])
    i = 0

    for step in config["pipeline"]:
        i += 1
        print(f"\nRunning {step['step']} [{i} / {n_steps}]:\n")

        command = ["python", step["script"]]
        command.extend(step["args"])

        for key, value in step["params"].items():
            command.extend([f"--{key}", str(value)])

        subprocess.run(command, check=True)


if __name__ == "__main__":
    run_pipeline("pipeline_config.yaml")
