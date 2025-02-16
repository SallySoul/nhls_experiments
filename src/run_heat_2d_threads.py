import param_sweep
import run_nhls
import lab
import json

name = "heat_2d_threads"
n = 4
cli_path = "/home/rbentley/nhls_binaries/heat_2d_ap_fft"
param_sweep_config = {
    "nhls_params": {
        "domain_size": [4000],
        "steps": [4000],
        "images": [2],
        "threads": [1, 32, 60],
        "chunk_size": [10000],
        "ratio": [0.5],
        "cutoff": [10],
        "wisdom_file": [True],
    }
}
data_dir = "/home/rbentley/nhls_experiments/data"

def main():
    print("SCRIPT: Starting")
    work_dir = lab.make_work_dir(name, data_dir)
    results_path = f"{work_dir}/data.json"
    wisdom_path = f"{work_dir}/wisdom"
    output_dir = f"{work_dir}/output_dir"
    param_sweep_config["nhls_params"]["output_dir"] = [output_dir]
    param_sweep_config["nhls_params"]["cli_path"] = [cli_path]

    print("SCRIPT: Getting Build Report")
    build_report = run_nhls.build_report(cli_path)

    param_instances = param_sweep.generate(param_sweep_config)
    print(f"*** SWEEP INSTANCES N: {len(param_instances)}")

    runtime_data = []
    for params in param_instances:
        param_results = run_nhls.run_nhls_test(params["nhls_params"], n, wisdom_path)
        runtime_data.append(param_results);
    
    print("*** Done with tests, writing results")
    result = {
            "build_info": build_report,
            "param_sweep_config": param_sweep_config,
            "runtime_data": runtime_data,
    }
    with open(results_path, 'w') as f:
        json.dump(result, f, indent=4)   

main()
