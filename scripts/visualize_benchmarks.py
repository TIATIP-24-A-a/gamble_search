import json
import os

import matplotlib.pyplot as plt
import numpy as np

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_path = os.path.join(project_root, 'data', 'output.json')

with open(json_path) as f:
    data = json.load(f)

results = []
for bench in data['benchmarks']:
    if 'array_performance' in bench['name']:
        if 'small' in bench['name']:
            size = 3
        elif 'medium' in bench['name']:
            size = 100
        elif 'large' in bench['name']:
            size = 10000
        elif 'very_large' in bench['name']:
            size = 1000000

        results.append({
            'size': size,
            'time': bench['stats']['mean']
        })

results.sort(key=lambda x: x['size'])

sizes = np.array([3, 100, 10000, 1000000])

measured_times = np.array([1.6, 12.5, 776.5, 101057.1])

plt.figure(figsize=(12, 8))
plt.style.use('bmh')

x = np.linspace(1, len(sizes), 100)
plt.plot(range(len(sizes)), measured_times / measured_times[0], 'bo-', label='Gamble Search', linewidth=2, markersize=8)
plt.plot(x, x, 'g--', label='O(n) - Linear', alpha=0.7)
plt.plot(x, x * np.log(x), 'r--', label='O(n log n)', alpha=0.7)
plt.plot(x, x**2, 'y--', label='O(n²) - Quadratic', alpha=0.7)

plt.grid(True, alpha=0.3)
plt.xlabel('Input Size', fontsize=12)
plt.ylabel('Relative Time', fontsize=12)
plt.title('Gamble Search Time Complexity', fontsize=14, pad=20)
plt.legend(fontsize=10)

plt.xticks(range(len(sizes)), [f'n={size}' for size in sizes], rotation=45)

for i, (size, time) in enumerate(zip(sizes, measured_times)):
    plt.annotate(f'{time:.1f}µs',
                (i, time / measured_times[0]),
                xytext=(0, 10),
                textcoords='offset points',
                ha='center',
                fontsize=9)

plt.tight_layout()
plt.savefig('data/big_o_comparison.png', dpi=300, bbox_inches='tight')

print("\nTime increase factors:")
for i in range(1, len(sizes)):
    size_factor = sizes[i] / sizes[i-1]
    time_factor = measured_times[i] / measured_times[i-1]
    print(f"When size increases by {size_factor:.1f}x (from {sizes[i-1]} to {sizes[i]})")
    print(f"Time increases by {time_factor:.1f}x (from {measured_times[i-1]:.1f}µs to {measured_times[i]:.1f}µs)\n")