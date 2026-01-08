def lagrange_interpolate_zero(points, field):
    """
    Reconstructs f(0) using Lagrange interpolation.

    points: list of (x, y) tuples
    field: prime modulus
    """
    secret = 0

    for i, (xi, yi) in enumerate(points):
        num = 1
        den = 1

        for j, (xj, _) in enumerate(points):
            if i != j:
                num = (num * (-xj)) % field
                den = (den * (xi - xj)) % field

        inv_den = pow(den, -1, field)
        li = num * inv_den % field
        secret = (secret + yi * li) % field

    return secret
