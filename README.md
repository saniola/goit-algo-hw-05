# Search Algorithm Efficiency Comparison

## Overview
This project aims to compare the efficiency of three substring search algorithms: Boyer-Moore (BM), Knuth-Morris-Pratt (KMP), and Rabin-Karp (RK) based on two text files, `text_01.txt` and `text_02.txt`. The algorithms are tested for both a real substring that exists in the text and a fabricated substring.

## Experiment Results

### Text1:
- **Real Substring:**
  - BM: 0.09415 seconds
  - KMP: 0.13533 seconds
  - RK: 0.31806 seconds

- **Fabricated Substring:**
  - BM: 0.16600 seconds
  - KMP: 0.68628 seconds
  - RK: 1.90015 seconds

### Text2:
- **Real Substring:**
  - BM: 0.06225 seconds
  - KMP: 0.08449 seconds
  - RK: 0.19206 seconds

- **Fabricated Substring:**
  - BM: 0.22343 seconds
  - KMP: 0.99720 seconds
  - RK: 2.80832 seconds

## Conclusion

### Real Substring:
- For both text files, Boyer-Moore consistently demonstrated the fastest performance among the three algorithms.
- Knuth-Morris-Pratt exhibited competitive results, slightly slower than Boyer-Moore.
- Rabin-Karp consistently showed the slowest performance.

### Fabricated Substring:
- Boyer-Moore maintained its efficiency, outperforming the other algorithms.
- Knuth-Morris-Pratt exhibited variable performance but generally performed better than Rabin-Karp.
- Rabin-Karp consistently demonstrated the slowest performance, especially evident with fabricated substrings.

In conclusion, the choice of algorithm depends on the specific characteristics of the data and the nature of the substrings. Boyer-Moore is recommended for scenarios where high efficiency is crucial, especially for real substrings. Knuth-Morris-Pratt is a competitive alternative, while Rabin-Karp may be less suitable for certain scenarios due to its slower performance.

## Instructions for Replication
1. Ensure the text files `text_01.txt` and `text_02.txt` are in the same directory as the code.
2. Run the provided Python script for algorithm efficiency measurement.
3. Analyze the results to determine the most suitable substring search algorithm for your specific use case.
