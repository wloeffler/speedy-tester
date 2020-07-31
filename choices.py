"""
This class is used to pass the users info and choices together instead of all spread out
Picture Perfect 2020
"""

class SessionInfo:

    def __init__(self,uName,uPass,addr,prob,aller,med,recon,immun,vital,proced,order,result,pthx,doc,trans,assess,health,encounter,homeHealth,transplant,flow,reportBuild,comments, ptMRN,testChoice):
        #the variables to store all the info
        #users Info
        self.userName = uName
        self.userPassword = uPass
        self.drisSiteAddress = addr
        self.ptMrn = ptMRN
        self.testChoice = testChoice
        #selected parts of the site to test
        self.problemListSelected = prob
        self.allergiesSelected = aller
        self.medicationsSelected = med
        self.reconSelected = recon
        self.immunizationsSelected = immun
        self.vitalsSelected = vital
        self.proceduresSelected = proced
        self.ordersSelected = order
        self.resultsSelected = result
        self.patientHxSelected = pthx
        self.documentsSelected = doc
        self.transfusionsSelected = trans
        self.assessmentsSelected = assess
        self.healthSelected = health
        self.encountersSelected = encounter
        self.homeHealthSelected = homeHealth
        self.transplantSelected = transplant
        self.flowsheetsSelected = flow
        self.reportBuilderSelected = reportBuild
        self.drisCommentsSelected = comments

