
import unittest
from time import sleep
import pickle
import sys

sys.dont_write_bytecode=True

# Import the python file HTMLTestRunner contains script for creating HTML Report.
import HTMLTestRunner

# path of wd.pk file in the MTS System (needed only for running the scipt in MTS)
#PK_FILE_PATH = "../../Scripts/Data/wd.pk"
PK_FILE_PATH = "../../wd.pk"

# Opening the wd.pk file
f = open(PK_FILE_PATH, 'r')

# De-serializing or un pickling the webdriver object from wd.pk file.(which was already created by MTS, while running the test)
wd = pickle.load(f)
f.close()

""" Set Report generating details """
#set report name
REPORT_NAME = "HpCardTest_report"

#set path to save reports (in MTS)
REPORT_PATH = "../Reports/"
FILE_NAME = REPORT_PATH + REPORT_NAME + ".html"

FP = file(FILE_NAME, 'wb')

#create report in html
runner = HTMLTestRunner.HTMLTestRunner(stream = FP, title = REPORT_NAME, description = 'Report_decription')

# unit test class which implements the test cases for HPCards
class PrintTest(unittest.TestCase):

    def setUp(self):
        self.driver = wd
       
    def test_cardPrint(self):        
        sleep(10)
        el = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIACollectionView[1]/UIACollectionCell[1]/UIAStaticText[1]')
        el.click()
        
    def tearDown(self):
        sleep(10)
        self.driver.quit()
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PrintTest)
    runner.run(suite)
    
