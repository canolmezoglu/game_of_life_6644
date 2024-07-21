import numpy as np
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
from game_engine import update_grid
from pattern_generator import random_grid


def run_experiment(grid_size, iterations, p_alive_values):
    results = []
    for p_alive in p_alive_values:
        initial_grid = random_grid(grid_size, p_alive)
        grid = initial_grid.copy()

        for _ in range(iterations):
            grid = update_grid(grid)

        final_live_percentage = np.sum(grid == 255) / grid.size
        results.append((p_alive, final_live_percentage))

    return results


# Experiment parameters
grid_size = 100
iterations = 400
p_alive_values = np.linspace(0.01, 0.99, 2000)  # 200 values from 1% to 99%

# Run the experiment
results = run_experiment(grid_size, iterations, p_alive_values)

# Extract data for correlation analysis
p_alive_list, final_percentages = zip(*results)

# Calculate correlation
correlation, p_value = pearsonr(p_alive_list, final_percentages)

# Plot results
plt.figure(figsize=(12, 8))
plt.scatter(p_alive_list, final_percentages, alpha=0.6)
plt.xlabel('Initial p_alive')
plt.ylabel('Final Live Cell Percentage')
plt.title(
    f'Correlation between p_alive and Final Live Cell Percentage\nCorrelation: {correlation:.4f}, p-value: {p_value:.4e}')
plt.grid(True)

# Add trend line
z = np.polyfit(p_alive_list, final_percentages, 1)
p = np.poly1d(z)
plt.plot(p_alive_list, p(p_alive_list), "r--", alpha=0.8)

# Add color gradient
plt.scatter(p_alive_list, final_percentages, c=p_alive_list, cmap='viridis', alpha=0.6)
plt.colorbar(label='Initial p_alive')

plt.tight_layout()
plt.savefig('random_grid_correlation_200.png', dpi=300)
plt.close()

print(f"Correlation: {correlation:.4f}")
print(f"p-value: {p_value:.4e}")

# Calculate additional statistics
mean_final_percentage = np.mean(final_percentages)
std_final_percentage = np.std(final_percentages)
max_final_percentage = np.max(final_percentages)
min_final_percentage = np.min(final_percentages)

print(f"\nAdditional Statistics:")
print(f"Mean Final Live Cell Percentage: {mean_final_percentage:.2f}%")
print(f"Standard Deviation of Final Live Cell Percentage: {std_final_percentage:.2f}%")
print(f"Maximum Final Live Cell Percentage: {max_final_percentage:.2f}%")
print(f"Minimum Final Live Cell Percentage: {min_final_percentage:.2f}%")

# Calculate and print the difference between initial and final percentages
initial_percentages = np.array(p_alive_list) * 100
differences = np.array(final_percentages) - initial_percentages
mean_difference = np.mean(differences)
std_difference = np.std(differences)

print(f"\nDifference between Initial and Final Percentages:")
print(f"Mean Difference: {mean_difference:.2f}%")
print(f"Standard Deviation of Difference: {std_difference:.2f}%")

# Plot the differences
plt.figure(figsize=(12, 8))
plt.scatter(p_alive_list, differences, alpha=0.6)
plt.xlabel('Initial p_alive')
plt.ylabel('Difference (Final % - Initial %)')
plt.title('Difference between Final and Initial Live Cell Percentages')
plt.grid(True)
plt.axhline(y=0, color='r', linestyle='--')
plt.colorbar(label='Initial p_alive')
plt.tight_layout()
plt.savefig('random_grid_differences_200.png', dpi=300)
plt.close()