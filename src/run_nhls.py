import time
import os

def run_nhls_test(params, n):
    cli_path = params["cli_path"]
    output_dir = params["output_dir"]
    domain_size = params["domain_size"]
    steps = params["steps"]
    images = params["images"]
    threads = params["threads"]
    chunk_size = params["chunk_size"]
    ratio = params["ratio"]
    cutoff = params["cutoff"]

    # Build command
    command = ""
    command += f"{cli_path}"
    command += f" --output-dir {output_dir}"
    command += f" --domain-size {domain_size}"
    command += f" --steps-per-image {steps}"
    command += f" --images {images}"
    command += f" --threads {threads}"
    command += f" --chunk-size {chunk_size}"
    command += f" --ratio {ratio}"
    command += f" --cutoff {cutoff}"

    if params["wisdom_file"]:
        command += f" --wisdom-file wisdom_file"
        wisdom_command = command
        wisdom_command += " --plan-type measure"
        wisdom_command += " --gen-only"
        command += " --plan-type wisdom-only"

        # Run command
        print(f"Running Wisdom command: {wisdom_command}")
        exit_status = os.system(wisdom_command);
        if exit_status != 0:
            print("    - Wisdom Call Failed " + str(exit_status))
            exit(1)
        else:
            print("    - Wisdom Call Successful")
  
    result = []
    print(f"Test Command: {command}")
    for i in range(0, n):
        print(f" - test {i}")
        start = time.time()
        exit_status = os.system(command);
        end = time.time()
        if exit_status != 0:
            print("    - Command Failed " + str(exit_status))
            exit(1)
        else:
            print("    - Command Successful")
        result.append(end - start)

    return result




