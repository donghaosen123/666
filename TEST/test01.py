import allure,pytest


class TestSms:
    def test_sms1(self):
        print(111)

    @pytest.mark.parametrize("a", [1, 2, 3])
    @allure.step('我是测试步骤001')
    def test_al(self, a):
        assert a != 2
        allure.attach("描述",'啊哈哈哈')

