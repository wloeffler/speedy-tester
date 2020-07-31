"""
This laysout and instantiates the GUI
Picture Perfect 2020
"""

import tkinter as tk
from tkinter import ttk
from choices import SessionInfo
from testMain import DRISTestDriver

VERSIONNUMBER = 0.69
LASTUPDATED = "7/27/2020"

window = tk.Tk()

window.title("Speedy Tester " + str(VERSIONNUMBER))
window.geometry("500x500")
window.minsize(400,500)
#window.configure(background = '#007BFF')



#top menus ****Needs work***
menu = tk.Menu(window)
window.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="Exit", command=window.quit)

helpmenu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command = lambda: openAboutWindow(LASTUPDATED,VERSIONNUMBER))

#list of all the buttons created
buttonList = list()

#list of all the Client names
listOfClientNames = ['ssmhealth', 'bjc', 'bhar']

#list of site types
listOfSiteTypes = ['dev', 'dev1', 'dev2', 'staging','gl','preprod','prod']



#opens a new window to explain how to use the tester
def openAboutWindow(updatedDate, versionNum):
    aboutWindow = tk.Tk()
    aboutWindow.geometry("500x500")
    aboutWindow.maxsize(500,350)
    aboutWindow.minsize(500,350)
    aboutWindow.title("About the Speedy Tester")
    ttk.Label(aboutWindow, text = "This program is used to help speed up the testing of DRIS sites \n\n"
                     "The user will select the site version (ex. dev, prod, gl) and the customer whos site it is\n"
                     "\tnote that if the site version or customer is not listed, \n \tthe user can input the desired names in the boxes instead\n"
                     "The user will input their information in the fields\n"
                     "The user will select the check boxes they wish to have the tests run on\n"
                     "\nThe options are:\n\t1. Update Check Test/ Functionality Test"
                     "\n\t2. Quick Test"
                     "\n\t3. Deep Test"
                     "\n\n"
                     "For Help Please contact IT and ask for Amanda Hugenkiz, or reach out to her pager at 8675309\n\n").grid(column =0, row = 0)
    ttk.Label(aboutWindow, text = "Version Number: " + str(versionNum) +" Updated: " +updatedDate).grid(sticky = 's')
    return

#this is the error window if there is missing information
def errorWindow():
    errorWin = tk.Tk()
    errorWin.geometry("500x350")
    errorWin.maxsize(300,200)
    errorWin.minsize(300,200)
    errorWin.title("ERROR")
    ttk.Label(errorWin, text= "You failed to input one or more of the following:\nUser name\nPassword\nSite information\nPatient MRN\nChoose a test to run").grid(sticky = 'n')


#the launch button, creates an instance of a the session info class
def launchTheButton(uName,uPass,addr,prob,aller,med,recon,immun,vital,proced,order,result,pthx,doc,trans,assess,health,encounter,homeHealth,transplant,flow,reportBuild,comments, ptMRN, tstCh):
    if(uName=='' or uPass=='' or addr=='' or ptMRN =='' or tstCh == -1):
        errorWindow()
        return

    passer = SessionInfo(uName,uPass,addr,prob,aller,med,recon,immun,vital,proced,order,result,pthx,doc,trans,assess,health,encounter,homeHealth,transplant,flow,reportBuild,comments,ptMRN, tstCh)

    #launches the chrome window to test
    drisTesDriver = DRISTestDriver(passer)
    return

#changes all the buttons state
def markAll(listOfAllButtons, stateOfSelectAllButton):
    if stateOfSelectAllButton == True:
        for button in listOfAllButtons:
            button.set(True)
    else:
        for button in listOfAllButtons:
            button.set(False)
    return


#site name maker
def siteName(siteType, clientName):
    if clientName == "prod": return ("https://dris-" + clientName + ".citi-us.com/")
    else: return ("https://dris-" + clientName + '-' + siteType +".citi-us.com/")


#creates all the textboxes and buttons
siteNameLabel = ttk.Label(window, text = "Site Information")
siteNameLabel.grid(column =0, row =0, padx = 10, pady =5)
siteType = ttk.Combobox(window, values = listOfSiteTypes)
siteType.grid(column =1, row =0, padx = 10, pady =5)
clientName = ttk.Combobox(window, values = listOfClientNames)
clientName.grid(column =2, row =0, padx = 10, pady =5)


userNameLabel = ttk.Label(window, text= "Site User Name")
userNameLabel.grid(column = 0, row =1, padx = 10, pady =5)
userNameEntry = ttk.Entry(window, width = 50)
userNameEntry.grid(column =1, row =1, columnspan = 3, padx = 10, pady =5)

userPwLabel = ttk.Label(window, text= "Site User Password")
userPwLabel.grid(column = 0, row =2, padx = 10, pady =5)
userPwEntry = ttk.Entry(window, width = 50, show ="x")
userPwEntry.grid(column =1, row =2, columnspan = 3, padx = 10, pady =5)

ptMRNLabel = ttk.Label(window, text= "Patient MRN").grid(column = 0, row = 3)
ptMRN = ttk.Entry(window, width = 10)
ptMRN.grid(column = 1, row =3, sticky = 'w', padx = 10, pady = 5)

fieldLabel = ttk.Label(window, text= "Modules to be Included").grid(column = 1, row = 4, padx =10, pady = 15)

#****SHOULD BE REWRITTEN TO DYNAMICALLY GENERATE GRID**** create list of all desired modules, and list for all checkboxes, iterate through with counters for rows and columns
#checkboxes for selection of components of dris
problemListSelected = tk.BooleanVar()
allergiesSelected = tk.BooleanVar()
medicationsSelected = tk.BooleanVar()
immunizationsSelected = tk.BooleanVar()
reconcilliationsSelected = tk.BooleanVar()
vitalsSelected = tk.BooleanVar()
proceduresSelected = tk.BooleanVar()
ordersSelected = tk.BooleanVar()
resultsSelected = tk.BooleanVar()
patientHistorySelected = tk.BooleanVar()
documentsSelected = tk.BooleanVar()
transfusionsSelected = tk.BooleanVar()
assessmentsSelected = tk.BooleanVar()
healthSelected = tk.BooleanVar()
encountersSelected = tk.BooleanVar()
homeHealthSelected = tk.BooleanVar()
transplantSelected = tk.BooleanVar()
flowsheetsSelected = tk.BooleanVar()
reportBuilderSelected = tk.BooleanVar()
commentsSelected = tk.BooleanVar()

#adds all the buttons to a master list
buttonList.extend((problemListSelected,allergiesSelected,medicationsSelected,immunizationsSelected,reconcilliationsSelected,vitalsSelected,proceduresSelected,ordersSelected,resultsSelected,patientHistorySelected,documentsSelected,transfusionsSelected,assessmentsSelected,healthSelected,encountersSelected,homeHealthSelected,transplantSelected,flowsheetsSelected,reportBuilderSelected,commentsSelected))
selectAll = tk.BooleanVar()


c1 = tk.Checkbutton(window, text = "Problem List", variable = problemListSelected, onvalue = True, offvalue = False).grid(column =0,row =5, padx =5, pady = 5, sticky = 'w' )
c2 = tk.Checkbutton(window, text = "Allergies", variable = allergiesSelected, onvalue = True, offvalue = False).grid(column =1,row =5, padx =5, pady = 5, sticky = 'w' )
c3 = tk.Checkbutton(window, text = "Medications", variable = medicationsSelected, onvalue = True, offvalue = False).grid(column =2,row =5, padx =5, pady = 5, sticky = 'w' )
c4 = tk.Checkbutton(window, text = "Reconcilliations", variable = reconcilliationsSelected, onvalue = True, offvalue = False).grid(column =0,row =6, padx =5, pady = 5, sticky = 'w' )
c5 = tk.Checkbutton(window, text = "Immunizations", variable = immunizationsSelected, onvalue = True, offvalue = False).grid(column =1,row =6, padx =5, pady = 5, sticky = 'w' )
c6 = tk.Checkbutton(window, text = "Vitals", variable = vitalsSelected, onvalue = True, offvalue = False).grid(column =2,row =6, padx =5, pady = 5, sticky = 'w' )
c7 = tk.Checkbutton(window, text = "Procedures", variable = proceduresSelected, onvalue = True, offvalue = False).grid(column =0,row =7, padx =5, pady = 5, sticky = 'w' )
c8 = tk.Checkbutton(window, text = "Orders", variable = ordersSelected, onvalue = True, offvalue = False).grid(column =1,row =7, padx =5, pady = 5, sticky = 'w' )
c9 = tk.Checkbutton(window, text = "Results", variable = resultsSelected, onvalue = True, offvalue = False).grid(column =2,row =7, padx =5, pady = 5, sticky = 'w' )
c10 = tk.Checkbutton(window, text = "Patient History", variable = patientHistorySelected, onvalue = True, offvalue = False).grid(column =0,row =8, padx =5, pady = 5, sticky = 'w' )
c11 = tk.Checkbutton(window, text = "Documents", variable = documentsSelected, onvalue = True, offvalue = False).grid(column =1,row =8, padx =5, pady = 5, sticky = 'w' )
c12 = tk.Checkbutton(window, text = "Transfusions", variable = transfusionsSelected, onvalue = True, offvalue = False).grid(column =2,row =8, padx =5, pady = 5, sticky = 'w' )
c13 = tk.Checkbutton(window, text = "Assessments", variable = assessmentsSelected, onvalue = True, offvalue = False).grid(column =0,row =9, padx =5, pady = 5, sticky = 'w' )
c14 = tk.Checkbutton(window, text = "Health", variable = healthSelected, onvalue = True, offvalue = False).grid(column =1,row =9, padx =5, pady = 5, sticky = 'w' )
c15 = tk.Checkbutton(window, text = "Encounter", variable = encountersSelected, onvalue = True, offvalue = False).grid(column =2,row =9, padx =5, pady = 5, sticky = 'w' )
c16 = tk.Checkbutton(window, text = "Home Health", variable = homeHealthSelected, onvalue = True, offvalue = False).grid(column =0,row =10, padx =5, pady = 5, sticky = 'w' )
c17 = tk.Checkbutton(window, text = "Transplant", variable = transplantSelected, onvalue = True, offvalue = False).grid(column =1,row =10, padx =5, pady = 5, sticky = 'w' )
c18 = tk.Checkbutton(window, text = "Flowsheets", variable = flowsheetsSelected, onvalue = True, offvalue = False).grid(column =2,row =10, padx =5, pady = 5, sticky = 'w' )
c19 = tk.Checkbutton(window, text = "Report Builder", variable = reportBuilderSelected, onvalue = True, offvalue = False).grid(column =0,row =11, padx =5, pady = 5, sticky = 'w' )
c20 = tk.Checkbutton(window, text = "DRIS Comments", variable = commentsSelected, onvalue = True, offvalue = False).grid(column = 1, row = 11, padx = 5, pady = 5, sticky = 'w')
c21 = tk.Checkbutton(window, text = "SELECT ALL", variable = selectAll, onvalue = True, offvalue = False, command = lambda: markAll(buttonList,selectAll.get())).grid(column =2, row =11, padx = 5, pady=5, sticky ='w')

choiceOfTest = tk.IntVar()
choiceOfTest.set(-1)
tk.Radiobutton(window,text ="Update Check", variable = choiceOfTest, value =1).grid(column = 0, row = 12, pady = 5)
tk.Radiobutton(window,text ="Quick Test", variable = choiceOfTest, value = 2).grid(column = 1, row = 12, pady = 5)
tk.Radiobutton(window,text ="Deep Test", variable = choiceOfTest, value = 3).grid(column = 2, row = 12, pady = 5)

runButton = ttk.Button(window, text = "Launch Tester", command = lambda: launchTheButton(userNameEntry.get(),userPwEntry.get(),siteName(siteType.get(),clientName.get()),problemListSelected.get(),allergiesSelected.get(),medicationsSelected.get(),reconcilliationsSelected.get(),immunizationsSelected.get(),vitalsSelected.get(),proceduresSelected.get(),ordersSelected.get(),resultsSelected.get(),patientHistorySelected.get(),documentsSelected.get(),transfusionsSelected.get(),assessmentsSelected.get(),healthSelected.get(),encountersSelected.get(),homeHealthSelected.get(),transplantSelected.get(),flowsheetsSelected.get(),reportBuilderSelected.get(),commentsSelected.get(),ptMRN.get(), choiceOfTest.get()))
runButton.grid(column =1, row = 14, padx = 15, pady = 15)


#starts the fun!!!
window.mainloop()
