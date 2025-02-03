import param_sweep
import run_nhls 
import json

param_sweep_config = {
    "nhls_params": {
        "cli_path": ["/home/rbentley/heat_2d_execs/heat_2d_ap_fft_avx2_singleunit"],
        "output_dir": ["output"],
        "domain_size": [4000],
        "steps": [4000],
        "images": [2],
        "threads": [32],
        "chunk_size": [4000],
        "ratio": [0.5, 0.7, 0.9],
        "cutoff": [40, 100, 400, 500],
        "wisdom_file": [True],
    }
}
sweep_params = param_sweep.generate(param_sweep_config)
print(f"{len(sweep_params)} sweep params")

n = 4
result = []
print("Starting Test Run")
for params in sweep_params:
    param_results = run_nhls.run_nhls_test(params["nhls_params"], n)
    result.append(param_results);
print("Done with tests, writing results")

with open('params_tests_results.json', 'w') as f:
    json.dump(result, f)
