R = 8.31


def compute_rm(list_of_tuples):  # (concentration, vemp)
    rm = 0
    for t in list_of_tuples:
        rm += t[0] / t[1]

    return rm


def compute_cmp(list_of_tuples):  # (concentration, temps)
    c_moy = 0
    total_time = 0
    for t in list_of_tuples:
        c_moy += t[0] * t[1]  # concentration * temps
        total_time += t[1]
    c_moy = c_moy / total_time
    return c_moy


def mgm3_to_ppm(c_mgm3, masse_molaire, temperature, pression):
    vol_mol = R * temperature / pression

    return c_mgm3 * vol_mol / masse_molaire


def ppm_to_mgm3(c_ppm, masse_molaire, temperature, pression):
    vol_mol = R * temperature / pression

    return c_ppm * masse_molaire / vol_mol


def compute_vema(vemp, fa):
    return vemp * fa


if __name__ == "__main__":
    c1 = 100
    c2 = 50
    c3 = 75
    t1 = 150
    t2 = 250
    t3 = 150
    rm = compute_rm([(c1, t1), (c2, t2), (c3, t3)])