import param_sweep
import run_nhls 
import json

param_sweep_config = {
    "nhls_params": {
        "cli_path": ["/Users/russell/projects/stencil_research/nhls/target/release/examples/heat_2d_ap_fft"],
        "output_dir": ["output"],
        "domain_size": [8000],
        "steps": [8000],
        "images": [2],
        "threads": [4, 8],
        "chunk_size": [1000, 8000, 80000],
        "ratio": [0.5],
        "cutoff": [100],
        "wisdom_file": [True],
    }
}
sweep_params = param_sweep.generate(param_sweep_config)
print(f"{len(sweep_params)} sweep params")

n = 2
result = []
print("Starting Test Run")
for params in sweep_params:
    param_results = run_nhls.run_nhls_test(params["nhls_params"], n)
    result.append(param_results);
print("Done with tests, writing results")

with open('thread_test.json', 'w') as f:
    json.dump(result, f)
