import json
import os
import numpy as np
import matplotlib.pyplot as plt

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_path = os.path.join(project_root, 'data', 'output.json')

with open(json_path) as f:
    data = json.load(f)

results = []
for bench in data['benchmarks']:
    if 'array_performance' in bench['name']:
        size = int(bench['name'].split('[')[1].rstrip(']'))
        results.append({
            'size': size,
            'time': bench['stats']['mean']
        })
results.sort(key=lambda x: x['size'])

sizes = np.array([r['size'] for r in results])
times = np.array([r['time'] for r in results]) * 1e6  # Convert to microseconds

plt.figure(figsize=(12, 8))

x = np.logspace(np.log10(sizes[0]), np.log10(sizes[-1]), 100)
scale = times[0] / np.log2(sizes[0])
plt.plot(x, np.log2(x) * scale, 'r--', label='O(log n)', alpha=0.7)

scale_linear = times[0] / sizes[0]
plt.plot(x, x * scale_linear, 'g--', label='O(n)', alpha=0.7)

scale_quad = times[0] / (sizes[0]**2)
plt.plot(x, (x**2) * scale_quad, 'm--', label='O(n²)', alpha=0.7)

plt.plot(sizes, times, 'bo-', label='Gamble Search', linewidth=2, markersize=8)

plt.xscale('log')
plt.yscale('log')

plt.xlabel('Input Size (n) - Logarithmic Scale', fontsize=12)
plt.ylabel('Time (microseconds) - Logarithmic Scale', fontsize=12)
plt.title('Gamble Search Time Complexity', fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, which='both', alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(project_root, 'data', 'big_o_logarithmic_chart.png'),
           dpi=300, bbox_inches='tight')
plt.show()