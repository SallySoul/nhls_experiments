set -euo pipefail

echo "BUILD SCRIPT: Building binaries"

export RUSTFLAGS='-C target-feature=+avx2 -C codegen-units=1' 
cargo build --release --example heat_1d_ap_fft
cargo build --release --example heat_2d_ap_fft
cargo build --release --example heat_2d_ap_direct
cargo build --release --example heat_3d_ap_fft

cp target/release/examples/heat_1d_ap_fft ~/nhls_binaries/
cp target/release/examples/heat_2d_ap_fft ~/nhls_binaries/
cp target/release/examples/heat_2d_ap_direct ~/nhls_binaries/
cp target/release/examples/heat_3d_ap_fft ~/nhls_binaries/
