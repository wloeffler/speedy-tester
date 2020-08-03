"""
This is the testing framework built upon unit test and Selenium
Picture Perfect 2020
"""


import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from choices import SessionInfo

#the driver class for DRIS testing
class DRISTestDriver:

    #ex only at first start up, sets up the whole shebang
    def __init__(cls,choiceContainer):
        location = r"C:\Users\wloeffler\PycharmProjects\DrisTest\venv\chromedriver.exe"
        #opens the webdriver
        cls.magicMaker = webdriver.Chrome(location)
        cls.magicMaker.implicitly_wait(10)
        #the url that will initally be navigated to; be sure to include the http:// or https://
        url = choiceContainer.drisSiteAddress
        #opens the inital window
        cls.magicMaker.get(url)
        cls.magicMaker.maximize_window()

        #login Info
        user = choiceContainer.userName
        pw = choiceContainer.userPassword
        MRN = choiceContainer.ptMrn
        #finds the element then sends the key to it, then submits everything
        #for staging
        username = cls.magicMaker.find_element_by_id("UserName").send_keys(user)
        #for test, gl, preprod, etc
       # username = cls.magicMaker.find_element_by_id("userNameInput").send_keys(user)
        #for staging
        supersecretPwField = cls.magicMaker.find_element_by_id("Password")
        # for test, gl, preprod, etc
       # supersecretPwField = cls.magicMaker.find_element_by_id("passwordInput")
        supersecretPwField.send_keys(pw)
        supersecretPwField.send_keys(Keys.RETURN)

        #opens the output file
        fileName = "DRIS_Functionality_Test_"+ str(MRN) + '_'+str(time.gmtime().tm_yday) + '_GMT'+str(time.gmtime().tm_hour) + 'h'+ str(time.gmtime().tm_min) + 'm' +str(time.gmtime().tm_sec) + 's.txt'
        cls.outputfile = open(fileName, 'w')

        #navigate to clinical module
        cls.magicMaker.find_element_by_id("PatientMenuItem").click()

        #inputs the test patient MRN
        ptInfo = cls.magicMaker.find_element_by_id("MRN")
        ptInfo.send_keys(MRN)
        ptInfo.send_keys(Keys.RETURN)

        #searches for patient, records error if pt is not present, aborts whole thing if cant find
        #only will select first in the list of patients if multiple return
        try:
            doesElementExist = cls.magicMaker.find_element_by_xpath("//a[starts-with(@href, '/Clinical/ClinicalSummary/CERNER/')]")
            doesElementExist.click()
        #stops the whole test, as there is no sense of going on if the pt cant be fount
        except NoSuchElementException as Exception:
            cls.outputfile.write("The MRN searched for of " + cls.MRN + " was not found\n")
            cls.outputfile.close()
            cls.magicMaker.close()
            #raise KeyboardInterrupt
            exit(1)
        #pauses execution so that DRIS can load... at time of writing its slowwwwwww
        time.sleep(10)
        print("setupclass done")
    # ex once at end of the end

    def tearDownClass(cls):
        time.sleep(3.0)
        cls.magicMaker.close()
        cls.outputfile.close()
        print("teardownCLassdone")

    def setUp(self):
        time.sleep(3.0)
        print("setup started")

#All Test cases listed below

    def test_ProblemListTab(self):
        #selects the tab
        self.magicMaker.find_element_by_id("tabProblemList").click()
        "problemlist tab clicked"

        #finds the number of rows to iterate through
        numRows = int(self.magicMaker.find_element_by_xpath("//*[@id='ProblemListGrid']/div[2]/span[1]/span/span/span[1]").text)
        print(numRows)
        #selects first row and expands, then loops on the rest of the rows
        for i in range(numRows,1, -1):
            #inserts the row number into the string
            rowOfInfo = self.magicMaker.find_element_by_xpath("//*[@id='ProblemListGrid']/table/tbody/tr[" + str(i) + "]/td[1]/a")
            rowOfInfo.click()
            print("clicked on row")
            print(i)
            #opens all the tabs
            tabsWithinRow = self.magicMaker.find_elements_by_xpath("//a[starts-with(@href, '#tabContentProblemList')]")
            for subTab in tabsWithinRow:
                subTab.click()
                time.sleep(1.0)
                print("within sub tab")


            #closes the row
            rowOfInfo.click()


            time.sleep(3.0)


"""
    def test_AllergiesTab(self):
        #selects the tab
        self.magicMaker.find_element_by_id("tabAllergies").click()



    def test_MedicationsTab(self):
        #selects the tab
        self.magicMaker.find_element_by_id("tabMedications").click()


    def test_ReconciliationsTab(self):
        # selects the tab
        self.magicMaker.find_element_by_id("tabImmunizations").click()


    def test_ImmunizationsTab(self):
        # selects the tab
        self.magicMaker.find_element_by_id("tabMedRecon").click()


    def test_VitalsTab(self):
        # selects the tab
        self.magicMaker.find_element_by_id("tabVitals").click()


    def test_Procedures(self):
        # selects the tab
        self.magicMaker.find_element_by_id("tabProcedures").click()


    def test_OrdersTab(self):
        # selects the tab
        self.magicMaker.find_element_by_id("tabOrders").click()


    def test_Results(self):
        # selects the tab
        self.magicMaker.find_element_by_id("tabResults").click()


    def test_PatientHistoryTab(self):
        # selects the tab
        self.magicMaker.find_element_by_id("tabPatientHistory").click()


    def test_DocumentsTab(self):
        # selects the tab
        self.magicMaker.find_element_by_id("tabDocuments").click()

    def test_TransfusionsTab(self):
        # selects the tab
        self.magicMaker.find_element_by_id("tabTransfusions").click()


    def test_AssessmentsTab(self):
        # selects the tab
        self.magicMaker.find_element_by_id("tabAssessments").click()


    def test_HealthTab(self):
        # selects the tab
        self.magicMaker.find_element_by_id("tabHealth").click()

    def test_EncountersTab(self):
        # selects the tab
        self.magicMaker.find_element_by_id("tabEncounters").click()


    def test_HomeHealthTab(self):
        # selects the tab
        self.magicMaker.find_element_by_id("tabHomeHealth").click()

    def test_TransplantTab(self):
        # selects the tab
        self.magicMaker.find_element_by_id("tabTransplant").click()


    def test_FlowsheetsTab(self):
        # selects the tab
        self.magicMaker.find_element_by_id("tabFlowsheets").click()


    def test_ReportBuilderTab(self):
        # selects the tab
        self.magicMaker.find_element_by_id("tabReportBuilder").click()

    def test_DRISCommentsTab(self):
        # selects the tab
        self.magicMaker.find_element_by_id("tabDrisComments").click()
"""

