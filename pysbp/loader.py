def load_from_octave(filename):
    with open(filename) as file:
        lines = file.readlines()
        matrix_lines = _split_matrices(lines)
        matrices = []
        for m in matrix_lines:
            matrices.append(_transpose(_read_matrix(lines[m[0]:m[1]])))
    return matrices


def _split_matrices(lines):
    matrices = []
    in_matrix = False
    for i, l in enumerate(lines):
        if l[0] != '#' and not in_matrix:
            in_matrix = True
            matrices.append([i, None])
        elif (l[0] == '#' or not l.strip()) and matrices and in_matrix:
            matrices[-1][1] = i
            in_matrix = False

    return matrices


def _read_matrix(matrix_lines):
    def _split_line(line):
        return map(float, line.strip().split())

    matrix = []
    for l in matrix_lines:
        matrix.append(_split_line(l))
    return matrix


def _transpose(matrix):
    return map(list, zip(*matrix))
