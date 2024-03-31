#include <iostream>
#include <vector>
#include <stdexcept> // For std::invalid_argument

std::vector<std::vector<int>> inputMatrix() {
    int rows, cols;
    std::cin >> rows >> cols;
    if (rows <= 0 || cols <= 0) {
        throw std::invalid_argument("Invalid input: Matrix dimensions must be positive.");
    }
    std::vector<std::vector<int>> matrix(rows, std::vector<int>(cols));
    if (matrix.empty() || matrix[0].empty()) {
        throw std::invalid_argument("Invalid input: Matrix cannot be empty.");
    }
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (!(std::cin >> matrix[i][j])) {
                throw std::invalid_argument("Invalid input: Expected integer values.");
            }
        }
    }
    return matrix;
}



void printMatrix(const std::vector<std::vector<int>>& matrix) {
    for (const auto& row : matrix) {
        for (int element : row) {
            std::cout << element << " ";
        }
        std::cout << std::endl;
    }
}

bool canMultiply(const std::vector<std::vector<int>>& matrix1, const std::vector<std::vector<int>>& matrix2) {
    return matrix1[0].size() == matrix2.size();
}

std::vector<std::vector<int>> multiplyMatrices(const std::vector<std::vector<int>>& matrix1, const std::vector<std::vector<int>>& matrix2) {
    if (!canMultiply(matrix1, matrix2)) {
        throw std::invalid_argument("Matrices cannot be multiplied: Incompatible dimensions.");
    }

    int rows1 = matrix1.size();
    int cols1 = matrix1[0].size();
    int cols2 = matrix2[0].size();

    std::vector<std::vector<int>> result(rows1, std::vector<int>(cols2, 0));

    for (int i = 0; i < rows1; ++i) {
        for (int j = 0; j < cols2; ++j) {
            for (int k = 0; k < cols1; ++k) {
                result[i][j] += matrix1[i][k] * matrix2[k][j];
            }
        }
    }

    return result;
}

int main() {
    std::vector<std::vector<int>> matrix1, matrix2;
    try {
        matrix1 = inputMatrix();
        matrix2 = inputMatrix();
    }
    catch (const std::invalid_argument& e) {
        std::cerr << e.what() << std::endl;
        return 1;
    }

    try {
        auto result = multiplyMatrices(matrix1, matrix2);
        printMatrix(result);
    }
    catch (const std::invalid_argument& e) {
        std::cerr << e.what() << std::endl;
        return 1;
    }

    return 0;
}
