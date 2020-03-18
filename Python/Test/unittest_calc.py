import unittest

import calcuration

release_name = 'lesson'

class CalTest(unittest.TestCase):

    # Unit Testのセットアップを毎回作る
    def setUp(self):
        print('setup')
        self.cal = calcuration.Cal()
    
    # Unit Testの毎回終了処理、テストファイルの削除など。
    def tearDown(self):
        print('clean up')
        del self.cal

    def test_add_num_add_double(self):
        self.assertEqual(
            self.cal.add_num_add_double(1, 1), 4)

    #@unittest.skip('skip reason is skip test')
    @unittest.skipIf(release_name == 'lesson', 'skip!!')
    def test_add_num_add_double2(self):
        self.assertEqual(
            self.cal.add_num_add_double(2, 2), 8)

    def test_add_num_and_double_raise(self):
        with self.assertRaises(ValueError):
            self.cal.add_num_add_double('1', '1')

if __name__ == '__main__':
    unittest.main()