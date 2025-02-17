
# TOPSIS Package

**TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)** is a multi-criteria decision analysis method. This Python package implements TOPSIS, allowing users to rank alternatives based on weights and impacts of criteria.

## Features

- Handles datasets with numerical attributes.
- Supports user-defined weights and impacts.
- Generates a complete ranking of alternatives.
- Simple and intuitive interface for implementation.

---

## Installation

Install the package using pip:
```bash
pip install Topsis-ArnavAgarwal-102203985
```

---

## How to Use

### Input Format

The input dataset should be a CSV or Excel file containing numerical columns. The first column must uniquely identify the alternatives (e.g., names or IDs), and the remaining columns should represent the criteria.

Example `data.csv`:
| Alternative | Criterion 1 | Criterion 2 | Criterion 3 | Criterion 4 |
|-------------|-------------|-------------|-------------|-------------|
| Alt1        | 250         | 16          | 12          | 5           |
| Alt2        | 200         | 20          | 15          | 10          |
| Alt3        | 300         | 12          | 10          | 8           |
| Alt4        | 275         | 18          | 11          | 9           |

---

### Implementation

#### Step 1: Import the package
```python
from topsis import topsis
```

#### Step 2: Define inputs
- **Filepath**: Path to the input file (CSV or Excel).
- **Weights**: List of weights assigned to each criterion (must sum to 1).
- **Impacts**: List indicating whether a criterion has a positive or negative impact (`+` or `-`).

Example:
```python
file_path = 'data.csv'
weights = [0.4, 0.3, 0.2, 0.1]
impacts = ['+', '+', '-', '+']
```

#### Step 3: Execute the TOPSIS method
```python
result = topsis(file_path, weights, impacts)
```

#### Step 4: View results
```python
print(result)
# Output: DataFrame with alternatives ranked based on their performance
```

---

## Example Use Case

Imagine you're choosing the best laptop based on criteria like price, performance, battery life, and weight. Here’s how to decide using TOPSIS:

### Input Data
| Laptop   | Price (₹) | Performance (score) | Battery Life (hrs) | Weight (kg) |
|----------|-----------|---------------------|---------------------|-------------|
| Laptop A | 50000     | 8                   | 5                   | 1.5         |
| Laptop B | 60000     | 9                   | 6                   | 2.0         |
| Laptop C | 45000     | 7                   | 4                   | 1.3         |
| Laptop D | 55000     | 8                   | 7                   | 1.8         |

### Implementation
```python
from topsis import topsis

# Define inputs
file_path = 'laptops.csv'
weights = [0.3, 0.4, 0.2, 0.1]
impacts = ['-', '+', '+', '-']  # Lower price is better (-)

# Run TOPSIS
result = topsis(file_path, weights, impacts)

# Display the ranking
print(result)
```

### Output
| Laptop   | Rank |
|----------|------|
| Laptop D | 1    |
| Laptop B | 2    |
| Laptop A | 3    |
| Laptop C | 4    |

---

## Use Cases

1. **Business Decision-Making**: Rank suppliers or partners based on multiple criteria.
2. **Product Selection**: Choose the best product based on features, cost, and performance.
3. **Policy Analysis**: Evaluate alternatives for policy implementation.
4. **Academic Research**: Use as a ranking tool in multi-criteria decision analysis.

---

## License

This package is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements or feature additions.

---

## Authors

- Shrihan Tayal
- https://github.com/Shrihan-Tayal

