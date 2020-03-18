import unittest
from unittest.mock import MagicMock
import salary


class TestSalary(unittest.TestCase):
    '''
    def setUp(self):
        self.patcher = unittest.mock.patch('salary.ThirdPartyBonusRestApi.bonus_price')
        self.mock_bonus = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()
    '''


    def test_calcuration_salary(self):
        s = salary.Salary(year=2017)
        s.bonus_api.bonus_price = MagicMock(return_value=1)        
        self.assertEqual(s.calcuration_salary(), 101)

        s.bonus_api.bonus_price.assert_called()
        s.bonus_api.bonus_price.assert_called_once()
        s.bonus_api.bonus_price.assert_called_with(year=2017)
        s.bonus_api.bonus_price.assert_called_once_with(year=2017)
        self.assertEqual(s.bonus_api.bonus_price.call_count, 1)

    def test_calcuration_no_salary(self):
        s = salary.Salary(year=2050)
        s.bonus_api.bonus_price = MagicMock(return_value=0)        
        self.assertEqual(s.calcuration_salary(), 100)
        s.bonus_api.bonus_price.assert_not_called()

    @unittest.mock.patch('salary.ThirdPartyBonusRestApi.bonus_price', 
                        return_value=1)
    def test_calcuration_salary_patch(self, mock_bonus):
        s = salary.Salary(year=2017)
        self.assertEqual(s.calcuration_salary(), 101)
        mock_bonus.assert_called()


    def test_calcuration_salary_patch_with(self):
        with unittest.mock.patch(
            'salary.ThirdPartyBonusRestApi.bonus_price') as mock_bonus:
            mock_bonus.return_value = 1

            s = salary.Salary(year=2017)
            salary_price = s.calcuration_salary()

            self.assertEqual(salary_price, 101)
            mock_bonus.assert_called()


    def test_calcuration_salary_patcher(self):
        patcher = unittest.mock.patch('salary.ThirdPartyBonusRestApi.bonus_price')
        mock_bonus = patcher.start()
        mock_bonus.return_value = 1

        s = salary.Salary(year=2017)
        salary_price = s.calcuration_salary()

        self.assertEqual(salary_price, 101)
        mock_bonus.assert_called()        
        patcher.stop()


    def test_calcuration_salary_side_effect(self):
        def f(year):
            return 1

        patcher = unittest.mock.patch('salary.ThirdPartyBonusRestApi.bonus_price')
        mock_bonus = patcher.start()        
        #mock_bonus.side_effect = f   
        #mock_bonus.side_effect = lambda year: 1
        mock_bonus.side_effect = [
            1,
            2,
            3,
            ValueError('Bankrupt!!!')]

        s = salary.Salary(year=2017)
        salary_price = s.calcuration_salary()
        self.assertEqual(salary_price, 101)

        s = salary.Salary(year=2018)
        salary_price = s.calcuration_salary()
        self.assertEqual(salary_price, 102)

        s = salary.Salary(year=2019)
        salary_price = s.calcuration_salary()
        self.assertEqual(salary_price, 103)

        s = salary.Salary(year=200)
        with self.assertRaises(ValueError):
            s.calcuration_salary()

        patcher.stop()

    @unittest.mock.patch('salary.ThirdPartyBonusRestApi', spec=True) 
    def test_calcuration_salary_class(self, mock_rest):
        mock_rest = mock_rest.return_value
        #mock_rest = MockRest()
        mock_rest.bonus_price.return_value = 1
        mock_rest.get_api_name.return_value = 'Money'

        s = salary.Salary(year=2017)
        salary_price = s.calcuration_salary()

        self.assertEqual(salary_price, 101)
        mock_rest.bonus_price.assert_called()