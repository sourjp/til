import os

import pytest
import calcuration

class TestCal(object):

    @classmethod
    def setup_class(cls):
        cls.cal = calcuration.Cal()
        cls.test_dir = '/tmp/test_dir'
        cls.test_file_name = 'test.txt'

    @classmethod
    def teardown_class(cls):
        import shutil
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)
        del cls.cal

    def test_save_no_dir(self):
        self.cal.save(self.test_dir, self.test_file_name)
        test_file_path = os.path.join(
            self.test_dir, self.test_file_name)
        assert os.path.exists(test_file_path) is True

    def test_add_num_add_double1(self, request):
        os_name = request.config.getoption('--os-name')
        print(os_name)
        if os_name == 'mac':
            print('ls')
        elif os_name == 'windows':
            print('dir')
        assert self.cal.add_num_add_double(1, 1) == 4

    def test_add_num_add_double2(self, csv_file):
        print(csv_file)
        csv_file.write('test')
        # csv_file.close()
        # yeildで渡してあげればclose処理をこっちでする必要がない


    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(
            tmpdir, self.test_file_name)
        assert os.path.exists(test_file_path) is True

    def test_add_num_add_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_add_double('1', '1')

'''
pip3 install pytest-cov pytest-xdist

pytest pytest_test_fixture.py --cov=calcuration
pytest pytest_test_fixture.py --cov=calcuration --cov-report term-missing
'''


