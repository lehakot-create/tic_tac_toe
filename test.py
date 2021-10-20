import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_print_table(self):
        self.table = '-' * 13 + '\n'\
                    '| 1 | 2 | 3 |' + '\n' +\
                    '-' * 13 + '\n' +\
                    '| 4 | 5 | 6 |' + '\n' +\
                    '-' * 13 + '\n' +\
                    '| 7 | 8 | 9 |' + '\n' +\
                    '-' * 13 + '\n'
        self.assertEqual(main.print_table(list(range(1, 10))), self.table)

    def test_init_table(self):
        self.table = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(main.init_table(), self.table)

    def test_check_win(self):
        self.lst = [['X', 'X', 'X', 4, 5, 6, 7, 8, 9],
                    [1, 2, 3, 'X', 'X', 'X', 7, 8, 9],
                    [1, 2, 3, 4, 5, 6, 'X', 'X', 'X'],
                    ['X', 2, 3, 'X', 5, 6, 'X', 8, 9],
                    [1, 'X', 3, 4, 'X', 6, 7, 'X', 9],
                    [1, 2, 'X', 4, 5, 'X', 7, 8, 'X'],
                    ['0', 2, 3, 4, '0', 6, 7, 8, '0'],
                    [1, 2, '0', 4, '0', 6, '0', 8, 9]]
        for el in self.lst:
            with self.subTest(case=el):
                self.assertEqual(main.check_win(el), True)

    def test_free_cell(self):
        self.table = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.table2 = [1, 2, 3, 'X', 5, '0', 7, 8, 9]
        self.assertEqual(main.free_cell(self.table), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(main.free_cell(self.table2), [1, 2, 3, 5, 7, 8, 9])

    def test_comp_step(self): # возвращает номер позиции с макс колвом комбинаций
        self.lst = [{4: ['X', 2, 3, 4, 5, 6, 7, 8, 9]},
                    {4: [1, 'X', 3, 4, 5, 6, 7, 8, 9]},
                    {4: [1, 2, 'X', 4, 5, 6, 7, 8, 9]},
                    {4: [1, 2, 3, 'X', 5, 6, 7, 8, 9]},
                    {0: [1, 2, 3, 4, 'X', 6, 7, 8, 9]},
                    {4: [1, 2, 3, 4, 5, 'X', 7, 8, 9]},
                    {4: [1, 2, 3, 4, 5, 6, 'X', 8, 9]},
                    {4: [1, 2, 3, 4, 5, 6, 7, 'X', 9]},
                    {4: [1, 2, 3, 4, 5, 6, 7, 8, 'X']}]
        for el in self.lst:
            with self.subTest(case=el):
                self.assertEqual(main.comp_step(list(el.values())[0]), list(el.keys())[0])

if __name__ == '__main__':
    unittest.main()
