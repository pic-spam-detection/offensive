import yaml
import subprocess


def run_pipeline(config_file):
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)

    for step in config["pipeline"]:
        print(f"Running {step['step']}:")

        command = ["python", step["script"]]
        command.extend(step["args"])

        for key, value in step["params"].items():
            command.extend([f"--{key}", str(value)])

        subprocess.run(command, check=True)


if __name__ == "__main__":
    run_pipeline("pipeline_config.yaml")
