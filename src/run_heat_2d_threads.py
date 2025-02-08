import param_sweep
import run_nhls
import lab

name = "heat_2d_threads"
n = 4
cli_path = "path_to_cli"
data_dir = "path_to_data"
output_dir = "path_to_output"

param_sweep_config = {
    "nhls_params": {
        "domain_size": [4000],
        "steps": [4000],
        "images": [2],
        "threads": [60],
        "chunk_size": [10000],
        "ratio": [0.5],
        "cutoff": [100],
        "wisdom_file": [True],
    }
}

def main():
    data_dir = lab.make_work_dir(data_dir, name)
    results_path = f"{data_dir}/data.json"
    wisdom_path = f"{data_dir}/wisdom"
    output_dir = f"{data_dir}/output_dir"
    param_sweep_config["output_dir"] = [output_dir]
    param_sweep_config["cli_path"] = [cli_path]

    build_report = run_nhls.build_report(cli_path)

    param_instances = param_sweep.generate(param_sweep_config)
    print(f"*** SWEEP INSTANCES N: {len(sweep_params)}")

    runtime_data = []
    for params in sweep_params:
        param_results = run_nhls.run_nhls_test(params["nhls_params"], n, wisdom_path)
        result.append(param_results);
    
    print("*** Done with tests, writing results")
    result = {
            "build_info": build_report,
            "param_sweep_config": param_sweep_config,
            "runtime_data": runtime_data,
    }
    with open(results_path, 'w') as f:
        json.dump(result, f)   

main()
