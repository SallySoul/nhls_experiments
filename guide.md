Debug job with 1 task for 30 minutes.
```
srun \
  --partition=debug  \
  --pty \
  --account=sun127 \
  --nodes=1 \
  --ntasks=1 \
  --mem=8G \
  -t 00:30:00 \
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
  -t 02:00:00 \
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
