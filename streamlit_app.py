import streamlit as st
import numpy as np

def main():
    st.title("Eigenvalue and Eigenvector Calculator")

    st.write("Enter a square matrix below:")

    size = st.number_input("Matrix size (n x n)", min_value=2, max_value=10, value=2, step=1)

    matrix_input = []
    for i in range(size):
        row = st.text_input(f"Row {i+1} (Enter {size} numbers separated by space)", key=f"row_{i}")
        matrix_input.append(row)

    if st.button("Calculate"):
        try:
            matrix = []
            for row in matrix_input:
                numbers = list(map(float, row.strip().split()))
                if len(numbers) != size:
                    st.error(f"Each row must have exactly {size} numbers.")
                    return
                matrix.append(numbers)

            matrix = np.array(matrix)
            eigenvalues, eigenvectors = np.linalg.eig(matrix)

            st.subheader("Input Matrix:")
            st.write(matrix)

            st.subheader("Eigenvalues:")
            st.write(eigenvalues)

            st.subheader("Eigenvectors:")
            st.write(eigenvectors)

        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()