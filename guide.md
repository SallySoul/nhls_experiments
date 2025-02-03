Debug job with 1 task for 30 minutes.
```
srun \
  --partition=debug  \
  --pty \
  --account=sun127 \
  --nodes=1 \
  --ntasks=1 \
  --mem=8G \
  -t 01:00:00 \
  --wait=0 \
  --export=ALL \
/bin/bash
```


```
srun \
  --partition=compute  \
  --pty \
  --account=sun127 \
  --nodes=1 \
  --ntasks=1 \
  --cpus-per-task=32 \
  --mem=128G \
  -t 01:00:00 \
  --wait=0 \
  --export=ALL \
/bin/bash
```

Job gets `$TMPDIR` env variable for working directory.

```
cd $TMPDIR
cp ~/nhls/target/release/examples/heat_2d_p_fft .
./heat_2d_p_fft \
  --output-dir output \
  --images 2 \
  --steps-per-image 100000 \
  --domain-size 8000 \
  --rand-init \
  --plan-type measure \
  --wisdom-file "${TMPDIR}/wisdom" \
  --threads 32
```

```
./heat_2d_p_fft \
  --output-dir output \
  --images 2 \
  --steps-per-image 100000 \
  --domain-size 8000 \
  --rand-init \
  --plan-type wisdom-only \
  --wisdom-file "${TMPDIR}/wisdom" \
  --threads 32
```

10k or larger and it segfaults?
```
module add intel/19.1.3.304/6pv46so
module add intel-mkl/2020.4.304/vg6aq26
time ./mkl_2d_heat_fftw_P 8000 100000 32
```

Don't forget
```
RUSTFLAGS='-C target-cpu=native
RUSTFLAGS='-C target-feature=+avx2'
export RUSTFLAGS='-C target-feature=+avx2 -C codegen-units=1'
export RUSTFLAGS='-C target-feature=+sse3,+avx,+avx2 -C codegen-units=1'
```

```
time ./heat_2d_ap_fft_noavx \
  --output-dir output \
  --images 2 \
  --steps-per-image 5000 \
  --domain-size 2500 \
  --threads 32

time ./heat_2d_ap_fft_avx2_singleunit \
  --output-dir output \
  --images 2 \
  --steps-per-image 5000 \
  --domain-size 2500 \
  --threads 32

time ./heat_2d_ap_fft_avx2_singleunit \
  --output-dir output \
  --images 2 \
  --steps-per-image 5000 \
  --domain-size 2500 \
  --wisdom-file wisdom_2d \
  --plan-type wisdom-only \
  --threads 32

module add intel/19.1.3.304/6pv46so
module add intel-mkl/2020.4.304/vg6aq26
export OMP_NUM_THREADS=32
export MKL_NUM_THREADS=32
icc -std=gnu++98 -O3 -qopenmp -xhost -ansi-alias -ipo -qopt-prefetch=5 -AVX512 mkl_2d_heat_fftw_NP-n-polylog-gen.cpp -o mkl_2d_heat_fftw_NP-n-polylog-gen -lm -mkl

time ./mkl_2d_heat_fftw_NP-n-polylog-gen 2500 2500 5000 64 32768 32 0

```

