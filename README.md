# Mini Project 27: Number Grid Analyzer

This Python project uses **NumPy** to analyze and manipulate a user-defined 2D number grid.

## 🔧 Features

- Accepts custom grid dimensions (rows × columns)
- Takes input numbers from the user
- Displays the grid using NumPy
- Provides grid summary:
  - Total elements
  - Shape, dimensions, data type
- Performs statistical analysis:
  - Sum, mean, min, max
- Filters even and odd numbers from the grid
- Displays a reshaped version of the original grid

## 🧪 Example Output

```
📊 Welcome to Grid Analyzer 📊

Enter number of rows: 3
Enter number of columns: 4

Enter 12 numbers separated by space:
>> 1 2 3 4 5 6 7 8 9 10 11 12

📈 Your Grid:
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]

🔢 Grid Summary:
- Total Elements     : 12
- Grid Shape         : (3, 4)
- Grid Dimensions    : 2
- Data Type          : int64

📊 Statistical Info:
- Sum of All Values  : 78
- Mean Value         : 6.5
- Minimum Value      : 1
- Maximum Value      : 12

🔍 Filtered Views:
- Even Numbers       : [2 4 6 8 10 12]
- Odd Numbers        : [1 3 5 7 9 11]

🔁 Reshaped Grid (4x3):
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
```

## 📦 Dependencies
- Python 3.x
- NumPy

Install NumPy with:
```bash
pip install numpy
```

---

Created as part of **Day 31** of the Data Science + AI Roadmap.
