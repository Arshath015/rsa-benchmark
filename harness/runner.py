import time
from pathlib import Path
from implementations.naive import NaiveRSA
from implementations.optimized import OptimizedRSA

def benchmark(rsa_class, label: str, message: int) -> dict:
    rsa = rsa_class()
    start = time.perf_counter()
    pub, priv = rsa.generate_keys()
    gen_time = time.perf_counter() - start

    start = time.perf_counter()
    cipher = rsa.encrypt(message, pub)
    enc_time = time.perf_counter() - start

    start = time.perf_counter()
    plain = rsa.decrypt(cipher, priv)
    dec_time = time.perf_counter() - start

    return {
        'label': label,
        'gen_time_s': gen_time,
        'enc_time_s': enc_time,
        'dec_time_s': dec_time,
        'match': plain == message,
    }

def main():
    msg = 42
    results = []
    results.append(benchmark(NaiveRSA, 'Naive', msg))
    results.append(benchmark(OptimizedRSA, 'Optimized', msg))

    out_path = Path('results/comparison.md')
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open('w') as f:
        f.write('# RSA Benchmark Comparison\n\n')
        f.write('| Implementation | KeyGen (s) | Encrypt (s) | Decrypt (s) | Correct? |\n')
        f.write('|---|---|---|---|---|\n')
        for r in results:
            f.write(f"| {r['label']} | {r['gen_time_s']:.4f} | {r['enc_time_s']:.4f} | {r['dec_time_s']:.4f} | {r['match']} |\n")
    print('Benchmark completed, results written to results/comparison.md')

if __name__ == '__main__':
    main()
