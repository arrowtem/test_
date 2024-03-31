import subprocess

def test_multiplication(matrix1, matrix2):
    input_data = f"{len(matrix1)} {len(matrix1[0])}\n"
    for row in matrix1:
        input_data += " ".join(map(str, row)) + "\n"
    input_data += f"{len(matrix2)} {len(matrix2[0])}\n"
    for row in matrix2:
        input_data += " ".join(map(str, row)) + "\n"

    process = subprocess.Popen(
        ['matrix_multi'],
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=input_data)

    return stdout.strip(), stderr.strip()

# Test Cases
test_cases = [
    # Test cases with expected output
    ([[1, 2], [3, 4]], [[5, 6], [7, 8]], [[19, 22], [43, 50]]),
    ([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]], [[58, 64], [139, 154]]),
    ([[1, 2, 3]], [[4], [5], [6]], [[32]]),
    ([[1, 2], [3, 4]], [[5], [6]], [[17], [39]]),
    # Test cases with zero matrices
    ([[0, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]),
    ([[0, 0], [0, 0]], [[1, 2], [3, 4]], [[0, 0], [0, 0]]),  # First matrix is zero
    ([[1, 2], [3, 4]], [[0, 0], [0, 0]], [[0, 0], [0, 0]]),  # Second matrix is zero
    # Test cases where exception is expected
    ([[1, 2], [3, 4]], [[5, 6], [7, 8], [9, 10]], None),
    ([[1, 2], [3, 4]], [[5], [6], [7]], None),
    ([], [[]], None),
    # Overflow
    ([[1000000000, 1000000000], [1000000000, 1000000000]], [[1000000000, 1000000000], [1000000000, 1000000000]], None)

]

for idx, test_case in enumerate(test_cases, start=1):
    print(f"Test Case {idx}:")
    matrix1, matrix2 = test_case[:2]
    print("Matrix 1:")
    for row in matrix1:
        print(" ".join(map(str, row)))
    print("Matrix 2:")
    for row in matrix2:
        print(" ".join(map(str, row)))

    if len(matrix1) == 0 or len(matrix2) == 0:
        print("One or both matrices are empty. Skipping test.")
        print("-" * 50)
        continue

    expected_result = test_case[2] if len(test_case) == 3 else None

    try:
        stdout, stderr = test_multiplication(matrix1, matrix2)
        if expected_result is not None:
            actual_result = [list(map(int, row.split())) for row in stdout.split("\n")]
            if actual_result == expected_result:
                print("Test Passed! Output matches expected result.")
            else:
                print("Test Failed! Output does not match expected result.")
                print("Expected Result:")
                for row in expected_result:
                    print(" ".join(map(str, row)))
                print("Actual Result:")
                for row in actual_result:
                    print(" ".join(map(str, row)))
        else:
            print("Test Passed! Exception thrown as expected.")
            if stderr:
                print(f"Exception: {stderr}")
    except subprocess.CalledProcessError as e:
        if e.returncode != 0:
            print("Test Passed! Exception thrown as expected.")
            if stderr:
                print(f"Exception: {stderr}")
        else:
            print("Test Failed! No exception thrown as expected.")
    print("-" * 50)
