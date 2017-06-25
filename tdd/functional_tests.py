from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase): #1. 테스트는 unittest.TestCase 를 상속한 클래스로 구성된다.

    def SetUp(self):
        self.browser = webdriver.chrome() #2. setUp(), tearDown() 은 각 테스트 전후에 실행되는 메서드

    def tearDown(self):
        self.browser.quit() #3. 테스트를 하는 동안 오류가 발생해도 tearDown() 이 실행된다.

    # test_ 로 시작하는 메서드 : 테스트 러너가 실행하며 클래스 당 둘 이상의 test_ 로 시작하는 메서드를 가질 수 있다.
    # 테스트 메서드에 대한 설명적인 이름 선호
    def test_can_start_a_list_and_retrieve_it_later(self): #4. 테스트 본문
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        [...rest of comments as before]

if __name__ == '__main__': # 7. unittest.main() 을 호출하여 unittest 러너 시작, 파일에서 테스트 클래스와 메서드를 자동으로 찾아 실행함
    unittest.main(warnings='ignore') #8.
