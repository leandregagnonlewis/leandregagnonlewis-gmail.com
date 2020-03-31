import unittest
from SST import *


class SSTests(unittest.TestCase):
    def test_rm_ex1(self):
        c1 = 100
        c2 = 50
        c3 = 75
        t1 = 150
        t2 = 250
        t3 = 150
        rm = compute_rm([(c1, t1), (c2, t2), (c3, t3)])
        self.assertEqual(round(rm, 2), 1.37)

    def test_rm_ex2(self):
        c1 = 400
        c2 = 100
        c3 = 300
        t1 = 1190
        t2 = 713
        t3 = 1610
        rm = compute_rm([(c1, t1), (c2, t2), (c3, t3)])
        self.assertEqual(round(rm, 2), 0.66)

    def test_rm_ex3(self):
        c1 = compute_cmp([(25, 4), (33, 1.5), (12, 2.5)])
        c2 = compute_cmp([(225, 6), (560, 2)])
        c3 = compute_cmp([(20, 5), (40, 2), (60, 1)])
        t1 = 50
        t2 = 500
        t3 = 50
        rm = compute_rm([(c1, t1), (c2, t2), (c3, t3)])
        self.assertEqual(round(rm, 2), 1.67)

    def test_rm_ex4_method1(self):
        c1 = 1.8
        m2 = 28.085 + 15.999 * 2
        c2 = mgm3_to_ppm(20, m2, 30, 112.5)
        t1 = 3
        t2 = mgm3_to_ppm(53, m2, 30, 112.5)
        rm = compute_rm([(c1, t1), (c2, t2)])
        self.assertEqual(round(rm, 3), 0.977)

    def test_rm_ex4_method2(self):
        m1 = 14.007 + 15.999 * 2
        c1 = ppm_to_mgm3(1.8, m1, 30, 112.5)
        c2 = 20
        t1 = ppm_to_mgm3(3, m1, 30, 112.5)
        t2 = 53
        rm = compute_rm([(c1, t1), (c2, t2)])
        self.assertEqual(round(rm, 3), 0.977)

    def test_vema_ex2(self):
        fa = 0.67
        vemp = 67
        vema = compute_vema(vemp, fa)
        self.assertEqual(round(vema), 45)

    def test_vema_ex3(self):
        fa = 0.95
        vemp = 0.05
        vema = compute_vema(vemp, fa)
        self.assertEqual(round(vema, 3), 0.048)

    def test_vema_ex4(self):
        fa = 0.67
        vemp = 213
        vema = compute_vema(vemp, fa)
        self.assertEqual(round(vema), 143)


if __name__ == '__main__':
    unittest.main()
