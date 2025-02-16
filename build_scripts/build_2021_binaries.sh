set -euo pipefail

SRC_DIR="/home/rbentley/FFTStencils/FFT-Based-Implementation"
OUTPUT_DIR="/home/rbentley/2021_paper_binaries"

function build_2021_binary {
	EXEC_NAME=$1

  echo "BUILD SCRIPT: building exec: ${EXEC_NAME}"
  cd "${SRC_DIR}"
	icc \
	  -std=gnu++98 \
	  -O3 \
	  -qopenmp \
	  -xhost \
	  -ansi-alias \
	  -ipo \
	  -AVX512 \
	  -o "${EXEC_NAME}" \
	  "${EXEC_NAME}.cpp" \
	  -mkl

  echo "BUILD SCRIPT: cping exec: ${EXEC_NAME}"
	cp \
		"${EXEC_NAME}" \
    "${OUTPUT_DIR}/${EXEC_NAME}"
}

echo "BUILD SCRIPT: loading modules"
module add intel/19.1.3.304/6pv46so
module add intel-mkl/2020.4.304/vg6aq26

echo "BUILD_SCRIPT: building binaries"
build_2021_binary "mkl_1d_heat_fftw_NP-n-polylog-gen"
build_2021_binary "mkl_1d_heat_fftw_P"
build_2021_binary "mkl_2d_heat_fftw_NP-n-polylog-gen"
build_2021_binary "mkl_2d_heat_fftw_NP-n-polylog-gen"
build_2021_binary "mkl_2d_heat_fftw_P"
build_2021_binary "mkl_2d_heat_fftw_P"
build_2021_binary "mkl_2d_jacobi25_fftw_P"
build_2021_binary "mkl_2d_jacobi_fftw_NP-n-polylog-gen"
build_2021_binary "mkl_2d_seidel_fftw_NP-n-polylog-gen"
build_2021_binary "mkl_2d_seidel_fftw_P"
build_2021_binary "mkl_3d_heat_fftw_NP-n-polylog-gen"
build_2021_binary "mkl_3d_heat_fftw_P"
build_2021_binary "mkl_3d_poisson_fftw_NP-n-polylog-gen"
build_2021_binary "mkl_3d_poisson_fftw_P"
