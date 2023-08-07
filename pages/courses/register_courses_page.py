import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _search_box = "//input[@id='search']"
    _click_search = "//i[@class='fa fa-search']"
    _course = "//a[@href='/courses/javascript-for-beginners']"
    _all_courses = "//a[normalize-space()='ALL COURSES']"
    _enroll_button = "//button[@class='dynamic-button btn btn-default btn-lg btn-enroll']"
    _cc_num = "//input[@placeholder='Card Number']"
    _cc_exp = "//input[@placeholder='MM / YY']"
    _cc_cvv = "//input[@placeholder='Security Code']"
    _submit_enroll = "//button[@class='zen-subscribe sp-buy btn btn-default btn-lg btn-block btn-gtw btn-submit checkout-button dynamic-button']"  # need to do better
    _enroll_error_msg = "//div[@role='alert']//p[@class='dynamic-text']"

    ############################
    ### Element Interactions ###
    ############################

    def enterCourseName(self, name):
        self.sendKeys(name, locator=self._search_box , locatorType="xpath")

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button ,locatorType="xpath")

    def enterCardNum(self, num):
        self.sendKeys(num, locator=self._cc_num)

    def enterCardExp(self, exp):
        self.sendKeys(exp, locator=self._cc_exp)

    def enterCardCVV(self, cvv):
        self.sendKeys(cvv, locator=self._cc_cvv)

    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv)
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        messageElement = self.waitForElement(self._enroll_error_message, locatorType="xpath")
        result = self.isElementDisplayed(element=messageElement)
        return result
