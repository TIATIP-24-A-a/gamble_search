import json
import matplotlib.pyplot as plt
import pandas as pd

# Read the benchmark data
with open('output.json') as f:
    data = json.load(f)

# Extract the benchmarks
benchmarks = data['benchmarks']

# Create lists for visualization
names = []
times = []
errors = []

for bench in benchmarks:
    names.append(bench['name'].replace('test_', ''))  # Clean up test names
    times.append(bench['stats']['mean'])
    errors.append(bench['stats']['stddev'])

# Create bar plot
plt.figure(figsize=(10, 6))
plt.bar(names, times, yerr=errors)
plt.xticks(rotation=45, ha='right')
plt.ylabel('Time (seconds)')
plt.title('Gamble Search Performance')
plt.tight_layout()
plt.savefig('benchmark_results.png')

# Print detailed stats
for bench in benchmarks:
    print(f"\nTest: {bench['name']}")
    print(f"Mean time: {bench['stats']['mean']:.6f} seconds")
    print(f"Min time: {bench['stats']['min']:.6f} seconds")
    print(f"Max time: {bench['stats']['max']:.6f} seconds")
    print(f"Standard deviation: {bench['stats']['stddev']:.6f}")