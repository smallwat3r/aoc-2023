from solver import solver

with open("test.txt") as f:
    data = f.readlines()


def test_solver():
    result = solver(data)
    assert result == 281
