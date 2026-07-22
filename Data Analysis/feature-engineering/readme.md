# NumPy: Feature Engineering

Hands-on practice applying NumPy fundamentals to a real feature engineering task.

---

## Learned
- NumPy array creation and manipulation
- Broadcasting — applying operations across arrays without explicit loops
- Difference between NumPy arrays and Python lists (fixed dtype, vectorized speed)

## Built
- **Ratio feature:** price-per-sqft, calculated by dividing two columns of a house price dataset
- **Min-max normalization:** implemented manually using NumPy (`(x - min) / (max - min)`), instead of relying on `sklearn`, to understand the transformation at the array level

---

## Key Concept: Broadcasting

Broadcasting lets NumPy apply an operation (like subtracting the minimum or dividing by range) across an entire array in one step, without writing a loop. This same pattern shows up constantly later in ML/GenAI code — normalizing data, batch operations, and beyond.

```python
def min_max_normalize(column):
    arr = column.to_numpy()
    return (arr - arr.min()) / (arr.max() - arr.min())
```

---

## Files
- `feature_engineering.ipynb` — full working code
- `README.md` — this file

---

*Part of my [GenAI Engineering Journey](../../README.md)*