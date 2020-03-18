import pytest

import calcuration
'''
> pytest FILE_NAME
> pytest FILE_NAME -rs   //appear skip reason
'''

# classなくても実行できる
#
#def test_add_num_add_double():
#    cal = calcuration.Cal()
#    assert cal.add_num_add_double(1, 1) == 4

is_release = True

class TestCal(object):

    # クラスの開始時に実行
    @classmethod
    def setup_class(cls):
        print('test_start')
        cls.cal = calcuration.Cal()

    # クラスの終了時に実行
    @classmethod
    def teardown_class(cls):
        print('test_end')
        del cls.cal

    # Unit Testのセットアップを毎回作る
    def setup_method(self, method):
        print('method_open={}'.format(method.__name__))
        #self.cal = calcuration.Cal()
    
    # Unit Testの毎回終了処理、テストファイルの削除など。
    def teardown_method(self, method):
        print('method_close={}'.format(method.__name__))
        #del self.cal

    def test_add_num_add_double(self):
        assert self.cal.add_num_add_double(1, 1) == 4

    #@pytest.mark.skip(reason='skip!')
    @pytest.mark.skipif(is_release==True, reason='skip!')
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_add_double('1', '1')
            #cal.add_num_add_double(1, 1)
