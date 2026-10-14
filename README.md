# RSA Benchmark Report

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.9+](https://img.shields.io/badge/python-3.9%2B-success.svg)](https://www.python.org/)

A lightweight benchmark suite comparing two hand‑crafted RSA implementations: a straightforward naive version and a mathematically optimized variant.

---

## Table of Contents
- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Theoretical Background](#theoretical-background)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Benchmark Results](#benchmark-results)
- [Testing](#testing)
- [Limitations](#limitations)
- [Roadmap](#roadmap)
- [License](#license)

---

## Overview

This repository provides two self‑contained RSA implementations written from first principles. The **naive** variant follows textbook algorithms directly, while the **optimized** variant employs the binary exponentiation method and a fast GCD algorithm. A small harness runs both implementations on identical inputs, measures execution time, and records key sizes and operation counts.

---

## Tech Stack

- Python 3.9+
- Standard library only (random, math, time, pathlib)

---

## Architecture

```text
rsa-benchmark/
├─ implementations/
│  ├─ naive.py          # Straightforward RSA implementation
│  └─ optimized.py      # Binary exponentiation & Euclidean GCD
├─ harness/
│  └─ runner.py         # Benchmark driver, writes results/comparison.md
├─ tests/
│  ├─ test_naive.py
│  └─ test_optimized.py
├─ examples/
│  └─ demo.py           # Runs the benchmark and prints a summary
├─ results/
│  └─ comparison.md     # Auto‑generated benchmark table
├─ requirements.txt
└─ README.md
```

---

## Theoretical Background

RSA relies on the difficulty of factoring a large composite modulus *n = p·q* where *p* and *q* are distinct primes. Key generation consists of:
1. Selecting two large random primes *p* and *q*.
2. Computing *n = p·q* and Euler's totient *φ(n) = (p‑1)(q‑1)*.
3. Choosing a public exponent *e* coprime to *φ(n)*.
4. Deriving the private exponent *d* as the modular multiplicative inverse of *e* modulo *φ(n)*.

Modular exponentiation, the core of encryption/decryption, computes *c = m^e mod n* (or *m = c^d mod n*). The naive approach uses repeated multiplication, yielding *O(e)* operations. The optimized version applies the square‑and‑multiply algorithm, reducing complexity to *O(log e)*. Both variants also require a reliable GCD algorithm; the Euclidean method is far more efficient than a naïve subtraction loop.

---

## Installation

```bash
git clone https://github.com/yourorg/rsa-benchmark.git
cd rsa-benchmark
pip install -r requirements.txt
```

---

## Usage

Run the benchmark demo:

```bash
python examples/demo.py
```

The script generates a 512‑bit RSA key pair for each implementation, encrypts a sample message, decrypts it, and writes a timing summary to `results/comparison.md`.

---

## API Reference

### implementations.naive
- `class NaiveRSA(key_size: int = 512)`
  - `generate_keys() -> Tuple[Tuple[int, int], Tuple[int, int]]`
  - `encrypt(message: int, pub_key: Tuple[int, int]) -> int`
  - `decrypt(cipher: int, priv_key: Tuple[int, int]) -> int`

### implementations.optimized
- `class OptimizedRSA(key_size: int = 512)`
  - Same public methods as `NaiveRSA` but internally uses binary exponentiation and Euclidean GCD.

---

## Benchmark Results

See the automatically generated `results/comparison.md` for a detailed table of execution times and operation counts.

---

## Testing

```bash
pytest -q
```

---

## Limitations

- Only supports modest key sizes (up to 1024 bits) suitable for demonstration; larger keys would require a big‑integer library for performance.
- No side‑channel protections; this is purely educational.

---

## Roadmap

- Add a third implementation using Montgomery multiplication.
- Extend benchmarks to include key generation throughput.
- Provide a CLI wrapper for easy parameter tuning.

---

## License

MIT License


---
**Last updated:** 2026-10-14
