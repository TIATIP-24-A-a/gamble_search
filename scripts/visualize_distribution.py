import json
import os
import numpy as np
import matplotlib.pyplot as plt

# Load the benchmark data
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
json_path = os.path.join(project_root, 'data', 'output.json')

with open(json_path) as f:
    data = json.load(f)

# Get the largest array benchmark
largest_benchmark = None
largest_size = 0

for bench in data['benchmarks']:
    if 'array_performance' in bench['name']:
        size = int(bench['name'].split('[')[1].rstrip(']'))
        if size > largest_size:
            largest_size = size
            largest_benchmark = bench

# Extract individual runs (data is already in seconds)
runs = np.array(largest_benchmark['stats']['data'])
mean = largest_benchmark['stats']['mean']
median = largest_benchmark['stats']['median']

plt.figure(figsize=(12, 6))

# Create jittered x-positions for the dots
x = np.random.normal(1, 0.1, size=len(runs))

# Plot individual points
plt.scatter(x, runs, alpha=0.5, color='blue', s=50, label='Individual Runs')

# Add mean and median lines across the plot width
plt.axhline(y=mean, color='red', linestyle='-', label=f'Mean: {mean:.3f}s', alpha=0.7)
plt.axhline(y=median, color='green', linestyle='--', label=f'Median: {median:.3f}s', alpha=0.7)

# Customize the plot
plt.xlabel(f'Array Size: {largest_size:,} elements', fontsize=12)
plt.ylabel('Runtime (seconds)', fontsize=12)
plt.title(f'Individual Run Times for Gamble Search\n{len(runs)} runs on {largest_size:,} elements', fontsize=14)

# Remove x-axis ticks since they're meaningless (just for spread)
plt.xticks([])

# Add grid for better readability
plt.grid(True, axis='y', alpha=0.3)

# Add legend
plt.legend()

# Add statistics box
stats_text = (
    f"Min: {np.min(runs):.3f}s\n"
    f"Max: {np.max(runs):.3f}s\n"
    f"Std Dev: {np.std(runs):.3f}s\n"
    f"Range: {np.max(runs) - np.min(runs):.3f}s"
)
plt.text(1.4, np.median(runs), stats_text,
         bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

plt.tight_layout()

# Save the plot
output_path = os.path.join(project_root, 'data', 'runtime_distribution_largest.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.show()