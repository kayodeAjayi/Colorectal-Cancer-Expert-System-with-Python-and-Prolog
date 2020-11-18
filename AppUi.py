import tkinter as tk
from tkinter import *

from PIL import ImageTk, Image

from AppBackend import Patient

titleFont = "Helvetica", 16, 'bold'
titleText = 'Welcome to the Colorectal Cancer Diagnostic System'
headingFont = "Helvetica", 12, 'bold'
btnFont = "Helvetica", 10
basicFont = "Helvetica", 8
baseColor = '#a11b00'
textColor = 'white'
titleBg = '#00195c'
titleFg = '#ffa000'


class WelcomePage(tk.Frame):

    def __init__(self):
        tk.Frame.__init__(self)

        self.__checkedArray = []
        welcomeFrame = tk.Frame(self)
        welcomeFrame.grid(row=0, column=0, sticky='N')
        welcomeFrame.config(
            bg=baseColor
        )
        self.frame = welcomeFrame

        # Add Title Frame to Welcome Page Frame
        titleFrame = tk.Frame(welcomeFrame, bg=titleBg)
        titleFrame.grid(row=0, column=0, sticky='N', ipadx=400, pady=20)

        # Add Welcome Text to Title Frame
        welcomeLbl = tk.Label(welcomeFrame, text=titleText,
                              font=titleFont,
                              height=3, bg=titleBg, fg=titleFg)
        welcomeLbl.grid(row=0, column=0, columnspan=6, sticky='nEW')

        # Add Form Frame To Welcome Page Frame
        formFrame = tk.Frame(welcomeFrame,
                             bg=baseColor
                             )
        formFrame.grid(row=1, column=0, sticky='N', pady=20)

        # PERSONAL INFORMATION
        PersonalInfoLabel = tk.Label(formFrame, text="Personal Information", font=headingFont, bg=baseColor,
                                     fg=textColor)
        PersonalInfoLabel.grid(row=0, column=0, columnspan=6, pady=27)

        # Last Name label
        lastNameLabel = tk.Label(formFrame, text="Last Name", font=basicFont, bg=baseColor, fg=textColor)
        lastNameLabel.grid(row=1, column=0, sticky='w', pady=5)

        # Last Name Field
        self.lastNameEntry = tk.Entry(formFrame)
        self.lastNameEntry.grid(row=1, column=1, sticky='w', pady=5)

        # Add Space
        SpaceLabel = tk.Label(formFrame, text="   ",
                              font=basicFont, bg=baseColor, fg=textColor)
        SpaceLabel.grid(row=1, column=2, pady=5)

        # First Name Label
        firstNameLabel = tk.Label(formFrame, text="First Name", font=basicFont, bg=baseColor, fg=textColor)
        firstNameLabel.grid(row=1, column=3, sticky='w', pady=5)

        # First Name Entry
        self.FirstNameEntry = tk.Entry(formFrame)
        self.FirstNameEntry.grid(row=1, column=4, sticky='w', pady=5)

        # Age Label
        ageLabel = tk.Label(formFrame, text="Age", font=basicFont, bg=baseColor, fg=textColor)
        ageLabel.grid(row=2, column=0, sticky='w', pady=5)

        # Age Entry
        self.ageEntry = tk.Entry(formFrame)
        self.ageEntry.grid(row=2, column=1, sticky='w', pady=5)

        # Add Space
        SpaceLabel = tk.Label(formFrame,
                              text="                                                                                           ",
                              font=basicFont, bg=baseColor, fg=textColor)
        SpaceLabel.grid(row=2, column=2, pady=5)

        # Patient's Number Label
        patientsNumLabel = tk.Label(formFrame, text="Patient No", font=basicFont, bg=baseColor, fg=textColor)
        patientsNumLabel.grid(row=2, column=3, sticky='w', pady=5)

        # Patient's Number Entry
        patientsNumEntry = tk.Entry(formFrame)
        patientsNumEntry.grid(row=2, column=4, sticky='w', pady=5)

        # MEDICAL HISTORY QUESTIONS
        medicalHistoryLabel = tk.Label(formFrame, text="Medical History", font=headingFont, bg=baseColor, fg=textColor)
        medicalHistoryLabel.grid(row=3, column=0, columnspan=6, pady=15)

        # Personal history of colon cancer?
        self.__colonHistory = StringVar()
        colonHistoryCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__colonHistory,
                                           onvalue="colonHistory",
                                           offvalue="unchecked", command=lambda: self.sendData())
        colonHistoryCheck.deselect()
        colonHistoryCheck.grid(row=4, column=0, pady=5, sticky='e')

        # Personal history of colon cancer Label
        colonHistoryLabel = tk.Label(formFrame, text="Personal history of colon cancer?", font=basicFont, bg=baseColor,
                                     fg=textColor)
        colonHistoryLabel.grid(row=4, column=1, sticky='w', pady=5, columnspan=2)

        # Family history of colon cancer?
        self.__familyHistory = StringVar()
        familyHistoryCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__familyHistory,
                                            onvalue='familyHistory', offvalue='unchecked',
                                            command=lambda: self.sendData())
        familyHistoryCheck.deselect()
        familyHistoryCheck.grid(row=5, column=0, pady=5, sticky='e')

        # Personal history of colon cancer Label
        familyHistoryLabel = tk.Label(formFrame, text="Family history of colon cancer?", font=basicFont, bg=baseColor,
                                      fg=textColor)
        familyHistoryLabel.grid(row=5, column=1, sticky='w', pady=5, columnspan=2)

        # Diabetes history ?
        self.__diabetesHistory = StringVar()
        diabetesHistoryCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__diabetesHistory,
                                              onvalue='diabetesHistory', offvalue='unchecked',
                                              command=lambda: self.sendData())
        diabetesHistoryCheck.deselect()
        diabetesHistoryCheck.grid(row=6, column=0, pady=5, sticky='e')

        # Diabetes history Label
        diabetesHistoryLabel = tk.Label(formFrame, text="Diabetes history?", font=basicFont, bg=baseColor, fg=textColor)
        diabetesHistoryLabel.grid(row=6, column=1, sticky='w', pady=5, columnspan=2)

        # Inflamatory condition check ?
        self.__inflamatoryCondition = StringVar()
        inflamatoryConditionCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__inflamatoryCondition,
                                                   onvalue='inflamatoryCondition', offvalue='unchecked',
                                                   command=lambda: self.sendData())
        inflamatoryConditionCheck.deselect()
        inflamatoryConditionCheck.grid(row=4, column=2, pady=5, sticky='e')

        # Inflamatory condition Label
        inflamatoryConditionLabel = tk.Label(formFrame, text="Inflamatory condition?", font=basicFont, bg=baseColor,
                                             fg=textColor)
        inflamatoryConditionLabel.grid(row=4, column=3, sticky='w', pady=5, columnspan=2)

        # Radiation therapy check ?
        self.__radiationTherapy = StringVar()
        radiationTherapyCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__radiationTherapy,

                                               onvalue='radiationTherapy', offvalue='unchecked',
                                               command=lambda: self.sendData())
        radiationTherapyCheck.deselect()
        radiationTherapyCheck.grid(row=5, column=2, pady=5, sticky='e')

        # Radiation therapy Label
        radiationTherapyLabel = tk.Label(formFrame, text="Past radiation therapy?", font=basicFont, bg=baseColor,
                                         fg=textColor)
        radiationTherapyLabel.grid(row=5, column=3, sticky='w', pady=5, columnspan=2)

        # LIFESTYLE QUESTIONS
        personalInfoLabel = tk.Label(formFrame, text="Lifestlye", font=headingFont, bg=baseColor, fg=textColor)
        personalInfoLabel.grid(row=7, column=0, columnspan=6, pady=15)

        # Smokes check ?
        self.__smokes = StringVar()
        smokesCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__smokes, onvalue='smokes',
                                     offvalue='unchecked',
                                     command=lambda: self.sendData())
        smokesCheck.deselect()
        smokesCheck.grid(row=8, column=0, pady=5, sticky='e')

        # Smokes Label
        smokesLabel = tk.Label(formFrame, text="Smokes?", font=basicFont, bg=baseColor, fg=textColor)
        smokesLabel.grid(row=8, column=1, sticky='w', pady=5, columnspan=2)

        # Alcohol check ?
        self.__alcohol = StringVar()
        alcoholCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__alcohol, onvalue='alcohol',
                                      offvalue='unchecked', command=lambda: self.sendData())
        alcoholCheck.deselect()
        alcoholCheck.grid(row=9, column=0, pady=5, sticky='e')

        alcoholLabel = tk.Label(formFrame, text="Drinks alcohol?", font=basicFont, bg=baseColor, fg=textColor)
        alcoholLabel.grid(row=9, column=1, sticky='w', pady=5, columnspan=2)

        # diet check ?
        self.__diet = StringVar()
        dietCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__diet, onvalue='diet', offvalue='unchecked',
                                   command=lambda: self.sendData())
        dietCheck.deselect()
        dietCheck.grid(row=8, column=2, pady=5, sticky='e')

        dietLabel = tk.Label(formFrame, text="Low-fiber/ High-fat diet?", font=basicFont, bg=baseColor, fg=textColor)
        dietLabel.grid(row=8, column=3, sticky='w', pady=5, columnspan=2)

        # obesity check ?
        self.__obese = StringVar()
        obesityCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__obese, onvalue='obese',
                                      offvalue='unchecked',
                                      command=lambda: self.sendData())
        obesityCheck.deselect()
        obesityCheck.grid(row=9, column=2, pady=5, sticky='e')

        obesityLabel = tk.Label(formFrame, text="Obese?", font=basicFont, bg=baseColor, fg=textColor)
        obesityLabel.grid(row=9, column=3, sticky='w', pady=5, columnspan=2)

        # Next Button
        nextBtn = tk.Button(formFrame, text='Next',
                            command=lambda: dispFrame.nextClicked(), bg=titleFg,
                            fg=titleBg, font=btnFont
                            )
        nextBtn.grid(row=10, column=0, columnspan=6, pady=15, ipadx=40)

    def sendData(self):
        checkBtnArray = [self.__colonHistory.get(), self.__familyHistory.get(), self.__diabetesHistory.get(),
                         self.__inflamatoryCondition.get(), self.__radiationTherapy.get(), self.__smokes.get(),
                         self.__alcohol.get(),
                         self.__diet.get(), self.__obese.get()]
        # print(checkBtnArray)
        self.lastName = self.lastNameEntry.get()
        self.firstName = self.FirstNameEntry.get()
        self.age = self.ageEntry.get()
        self.__checkedArray = checkBtnArray

    def getCheckedArray(self):
        return self.__checkedArray

    def getName(self):
        return self.firstName + " " + self.lastName

    def getAge(self):
        return self.age

    def showNext(self):
        dispFrame.showFrame(SymptomsPage)

    def setData(self, a, b, c):
        pass


class SymptomsPage(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        self.__checkedArray = []
        symptomsFrame = tk.Frame(self
                                 , bg=baseColor
                                 )
        symptomsFrame.grid(row=0, column=0, sticky='N')
        symptomsFrame.config(
            bg=baseColor
        )

        # Add Title Frame to Symptoms Page Frame
        titleFrame = tk.Frame(symptomsFrame, bg=baseColor)
        titleFrame.grid(row=0, column=0, sticky='N', pady=50, padx=20)

        # Add Welcome Text to Title Frame
        welcomeLbl = tk.Label(symptomsFrame, text="Symptoms",
                              font=titleFont,
                              height=3, anchor='center', bg=titleBg, fg=titleFg)
        welcomeLbl.grid(row=0, column=0, columnspan=6, sticky='nEW')

        # Add Form Frame To Welcome Page Frame
        formFrame = tk.Frame(symptomsFrame,
                             bg=baseColor
                             )
        formFrame.grid(row=1, column=0, sticky='N', pady=2, padx=35)

        # PRIMARY SYMPTOMS
        symptomsLabel = tk.Label(formFrame, text="Primary Symptoms", font=headingFont, anchor='center', bg=baseColor,
                                 fg=textColor)
        symptomsLabel.grid(row=1, column=0, columnspan=7, pady=15, sticky='n')

        # Constipation check ?
        self.__constipation = StringVar()
        constipationCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__constipation,
                                           onvalue='constipation',
                                           offvalue='unchecked', command=lambda: self.sendData())
        constipationCheck.deselect()
        constipationCheck.grid(row=2, column=0, pady=5, sticky='e')

        # Constipation Label
        constipationLabel = tk.Label(formFrame, text="Constipation?", font=basicFont, bg=baseColor, fg=textColor)
        constipationLabel.grid(row=2, column=1, sticky='w', pady=5, columnspan=2)

        # Diarrhea check ?
        self.__diarrhea = StringVar()
        diarrheaCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__diarrhea, onvalue='diarrhea',
                                       offvalue='unchecked', command=lambda: self.sendData())
        diarrheaCheck.deselect()
        diarrheaCheck.grid(row=3, column=0, pady=5, sticky='e')

        diarrheaLabel = tk.Label(formFrame, text="Diarrhea?", font=basicFont, bg=baseColor, fg=textColor)
        diarrheaLabel.grid(row=3, column=1, sticky='w', pady=5, columnspan=2)

        # Change in stool color ?
        self.__stoolChange = StringVar()
        stoolChangeCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__stoolChange, onvalue='stoolChange',
                                          offvalue='unchecked', command=lambda: self.sendData())
        stoolChangeCheck.deselect()
        stoolChangeCheck.grid(row=4, column=0, pady=5, sticky='e')

        stoolChangeLabel = tk.Label(formFrame, text="Changes in stool color?", font=basicFont, bg=baseColor,
                                    fg=textColor)
        stoolChangeLabel.grid(row=4, column=1, sticky='w', pady=5, columnspan=2)

        # Changes in stool shape ?
        self.__stoolShape = StringVar()
        stoolShapeCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__stoolShape, onvalue='stoolShape',
                                         offvalue='unchecked', command=lambda: self.sendData())
        stoolShapeCheck.deselect()
        stoolShapeCheck.grid(row=5, column=0, pady=5, sticky='e')

        stoolShapeLabel = tk.Label(formFrame, text="Changes in stool shape?", font=basicFont, bg=baseColor,
                                   fg=textColor)
        stoolShapeLabel.grid(row=5, column=1, sticky='w', pady=5, columnspan=2)

        # Blood in stool ?
        self.__stoolBlood = StringVar()
        stoolBloodCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__stoolBlood, onvalue='stoolBlood',
                                         offvalue='unchecked', command=lambda: self.sendData())
        stoolBloodCheck.deselect()
        stoolBloodCheck.grid(row=6, column=0, pady=5, sticky='e')

        stoolBloodLabel = tk.Label(formFrame, text="Blood in stool?", font=basicFont, bg=baseColor, fg=textColor)
        stoolBloodLabel.grid(row=6, column=1, sticky='w', pady=5, columnspan=2)

        # Add Space
        SpaceLabel = tk.Label(formFrame,
                              text="                                                                                        ",
                              font=basicFont, bg=baseColor, fg=textColor)
        SpaceLabel.grid(row=3, column=3, pady=5)

        # Bleeding in Rectum ?
        self.__rectumBleeding = StringVar()
        rectumBleedingCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__rectumBleeding,
                                             onvalue='rectumBleeding',
                                             offvalue='unchecked', command=lambda: self.sendData())
        rectumBleedingCheck.deselect()
        rectumBleedingCheck.grid(row=2, column=4, pady=5, sticky='e')

        # Bleeding in Rectum Label
        rectumBleedingLabel = tk.Label(formFrame, text="Bleeding from rectum?", font=basicFont, bg=baseColor,
                                       fg=textColor)
        rectumBleedingLabel.grid(row=2, column=5, sticky='w', pady=5, columnspan=2)

        # Excessive Farting ?
        self.__excessFart = StringVar()
        excessFartCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__excessFart, onvalue='excessFart',
                                         offvalue='unchecked', command=lambda: self.sendData())
        excessFartCheck.deselect()
        excessFartCheck.grid(row=3, column=4, pady=5, sticky='e')

        excessFartLabel = tk.Label(formFrame, text="Excess Farting?", font=basicFont, bg=baseColor, fg=textColor)
        excessFartLabel.grid(row=3, column=5, sticky='w', pady=5, columnspan=2)

        # abdominal Cramps ?
        self.__abdominalCramps = StringVar()
        abdominalCrampsCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__abdominalCramps,
                                              onvalue='abdominalCramps'
                                              , offvalue='unchecked', command=lambda: self.sendData())
        abdominalCrampsCheck.deselect()
        abdominalCrampsCheck.grid(row=4, column=4, pady=5, sticky='e')

        abdominalCrampsLabel = tk.Label(formFrame, text="Abdominal Cramps?", font=basicFont, bg=baseColor, fg=textColor)
        abdominalCrampsLabel.grid(row=4, column=5, sticky='w', pady=5, columnspan=2)

        # abdominal Pain ?
        self.__abdominalPain = StringVar()
        abdominalPainCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__abdominalPain,
                                            onvalue='abdominalPain',
                                            offvalue='unchecked', command=lambda: self.sendData())
        abdominalPainCheck.deselect()
        abdominalPainCheck.grid(row=5, column=4, pady=5, sticky='e')

        abdominalPainLabel = tk.Label(formFrame, text="Abdominal Pains?", font=basicFont, bg=baseColor, fg=textColor)
        abdominalPainLabel.grid(row=5, column=5, sticky='w', pady=5, columnspan=2)

        # Excessive Fatigue ?
        self.__excessiveFatigue = StringVar()
        excessiveFatigueCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__excessiveFatigue,
                                               onvalue='excessiveFatigue'
                                               , offvalue='unchecked', command=lambda: self.sendData())
        excessiveFatigueCheck.deselect()
        excessiveFatigueCheck.grid(row=6, column=4, pady=5, sticky='e')

        excessiveFatigueLabel = tk.Label(formFrame, text="Excessive Fatigue?", font=basicFont, bg=baseColor,
                                         fg=textColor)
        excessiveFatigueLabel.grid(row=6, column=5, sticky='w', pady=5, columnspan=2)

        # Weight Loss ?
        self.__weightLoss = StringVar()
        weightLossCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__weightLoss, onvalue='weightLoss',
                                         offvalue='unchecked', command=lambda: self.sendData())
        weightLossCheck.deselect()
        weightLossCheck.grid(row=7, column=0, pady=5, sticky='e')

        weightLossLabel = tk.Label(formFrame, text="Weight Loss?", font=basicFont, bg=baseColor, fg=textColor)
        weightLossLabel.grid(row=7, column=1, sticky='w', pady=5, columnspan=2)

        # Vomiting ?
        self.__vomiting = StringVar()
        vomitingCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__vomiting, onvalue='vomiting',
                                       offvalue='unchecked', command=lambda: self.sendData())
        vomitingCheck.deselect()
        vomitingCheck.grid(row=7, column=4, pady=5, sticky='e')

        vomitingLabel = tk.Label(formFrame, text="Vomiting?", font=basicFont, bg=baseColor, fg=textColor)
        vomitingLabel.grid(row=7, column=5, sticky='w', pady=5, columnspan=2)

        # SECONDARY SYMPTOMS
        symptomsLabel = tk.Label(formFrame, text="Secondary Symptoms", font=headingFont, anchor='center', bg=baseColor,
                                 fg=textColor)
        symptomsLabel.grid(row=8, column=0, columnspan=7, pady=15, sticky='n')

        # Jaundice check ?
        self.__jaundice = StringVar()
        jaundiceCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__jaundice, onvalue='jaundice',
                                       offvalue='unchecked', command=lambda: self.sendData())
        jaundiceCheck.deselect()
        jaundiceCheck.grid(row=9, column=0, pady=5, sticky='e')

        # Constipation Label
        jaundiceLabel = tk.Label(formFrame, text="Jaundice?", font=basicFont, bg=baseColor, fg=textColor)
        jaundiceLabel.grid(row=9, column=1, sticky='w', pady=5, columnspan=2)

        # Body Swell check ?
        self.__bodySwell = StringVar()
        bodySwellCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__bodySwell, onvalue='bodySwell',
                                        offvalue='unchecked', command=lambda: self.sendData())
        bodySwellCheck.deselect()
        bodySwellCheck.grid(row=10, column=0, pady=5, sticky='e')

        # Body Swell Label
        bodySwellLabel = tk.Label(formFrame, text="Swelling in hands or feet?", font=basicFont, bg=baseColor,
                                  fg=textColor)
        bodySwellLabel.grid(row=10, column=1, sticky='w', pady=5, columnspan=2)

        # Breathing Difficulty check ?
        self.__breathingDiff = StringVar()
        breathingDiffCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__breathingDiff,
                                            onvalue='breathingDiff',
                                            offvalue='unchecked', command=lambda: self.sendData())
        breathingDiffCheck.deselect()
        breathingDiffCheck.grid(row=11, column=0, pady=5, sticky='e')

        # Breathing Difficulty Label
        breathingDiffLabel = tk.Label(formFrame, text="Breathing Difficulty?", font=basicFont, bg=baseColor,
                                      fg=textColor)
        breathingDiffLabel.grid(row=11, column=1, sticky='w', pady=5, columnspan=2)

        # Chronic Headache check ?
        self.__chronicHeadache = StringVar()
        chronicHeadacheCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__chronicHeadache,
                                              onvalue='chronicHeadache'
                                              , offvalue='unchecked', command=lambda: self.sendData())
        chronicHeadacheCheck.deselect()
        chronicHeadacheCheck.grid(row=9, column=4, pady=5, sticky='e')

        # Chronic Headache Label
        chronicHeadacheLabel = tk.Label(formFrame, text="Chronic Headache?", font=basicFont, bg=baseColor, fg=textColor)
        chronicHeadacheLabel.grid(row=9, column=5, sticky='w', pady=5, columnspan=2)

        # Blurry Vision check ?
        self.__blurryVision = StringVar()
        blurryVisionCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__blurryVision,
                                           onvalue='blurryVision',
                                           offvalue='unchecked', command=lambda: self.sendData())
        blurryVisionCheck.deselect()
        blurryVisionCheck.grid(row=10, column=4, pady=5, sticky='e')

        # Blurry Vision label
        blurryVisionLabel = tk.Label(formFrame, text="Blurry Vision?", font=basicFont, bg=baseColor, fg=textColor)
        blurryVisionLabel.grid(row=10, column=5, sticky='w', pady=5, columnspan=2)

        # Bone Fractures check ?
        self.__boneFracture = StringVar()
        boneFractureCheck = tk.Checkbutton(formFrame, bg=baseColor, variable=self.__boneFracture,
                                           onvalue='boneFracture',
                                           offvalue='unchecked', command=lambda: self.sendData())
        boneFractureCheck.deselect()
        boneFractureCheck.grid(row=11, column=4, pady=5, sticky='e')

        # Bone Fractures label
        boneFractureLabel = tk.Label(formFrame, text="Bone Fractures?", font=basicFont, bg=baseColor, fg=textColor)
        boneFractureLabel.grid(row=11, column=5, sticky='w', pady=5, columnspan=2)

        # Next Button
        nextBtn = tk.Button(formFrame, text='Next',
                            command=lambda: dispFrame.nextClicked(), bg=titleFg,
                            fg=titleBg, font=btnFont)
        nextBtn.grid(row=12, column=0, columnspan=7, pady=15, ipadx=40)

    def sendData(self):
        checkBtnArray = [self.__constipation.get(), self.__diarrhea.get(), self.__stoolChange.get(),
                         self.__stoolShape.get(), self.__stoolBlood.get(), self.__rectumBleeding.get(),
                         self.__excessFart.get(),
                         self.__abdominalCramps.get(), self.__abdominalPain.get(), self.__excessiveFatigue.get(),
                         self.__weightLoss.get(),
                         self.__vomiting.get(), self.__jaundice.get(), self.__bodySwell.get(),
                         self.__breathingDiff.get(),
                         self.__chronicHeadache.get(),
                         self.__blurryVision.get(), self.__boneFracture.get()]
        self.__checkedArray = checkBtnArray

    def getCheckedArray(self):
        return self.__checkedArray

    def showNext(self):
        dispFrame.showFrame(StagingPage)

    def showNext2(self):
        dispFrame.showFrame(ResultsPage)

    def setData(self, a, b, c):
        pass


class StagingPage(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        self.__radioSelectionArray = []

        symptomsFrame = tk.Frame(self
                                 , bg=baseColor
                                 )
        symptomsFrame.grid(row=0, column=0, sticky='N')
        symptomsFrame.config(
            # bg='grey'
        )

        # Add Title Frame to Staging Page Frame
        titleFrame = tk.Frame(symptomsFrame)
        titleFrame.grid(row=0, column=0, sticky='N', pady=50, padx=40)

        # Add Welcome Text to Title Frame
        welcomeLbl = tk.Label(symptomsFrame, text="Staging Page",
                              font=titleFont,
                              height=3, anchor='center', bg=titleBg, fg=titleFg)
        welcomeLbl.grid(row=0, column=0, columnspan=6, sticky='nEW')

        # Add Form Frame To Welcome Page Frame
        formFrame = tk.Frame(symptomsFrame,
                             bg=baseColor
                             )
        formFrame.grid(row=1, column=0, sticky='N', pady=(2, 34), padx=2)

        # CANCER STAGING
        stagingLabel = tk.Label(formFrame, text="The patient shows symptoms of Colorectal cancer. Undergo a "
                                                "CT Scan and choose the appropriate option to determine cancer stage",
                                font=basicFont, anchor='center', bg=baseColor,
                                fg=textColor)
        stagingLabel.grid(row=1, column=0, columnspan=7, pady=15, sticky='n')

        self.__stage = StringVar()
        self.__stage.set('stage 0')

        # Mucusa  Membrane check ?
        mucusaCheck = tk.Radiobutton(formFrame, bg=baseColor, variable=self.__stage, value='stage 0')
        mucusaCheck.grid(row=2, column=0, pady=5, sticky='e')

        # Mucusa Membrane Label
        mucusaLabel = tk.Label(formFrame, text="Cancer cells are only in the mucusa membrane?", font=basicFont,
                               bg=baseColor, fg=textColor)
        mucusaLabel.grid(row=2, column=1, sticky='w', pady=5, columnspan=2)

        # Invade Mucular Layer of Colon/Rectum check ?
        colonMucularCheck = tk.Radiobutton(formFrame, bg=baseColor, variable=self.__stage, value='stage 1')
        colonMucularCheck.grid(row=3, column=0, pady=5, sticky='e')

        # Invade Mucular Layer of Colon/Rectum Label
        colonMucularLabel = tk.Label(formFrame, text="Cancer cells have invaded the mucular layer of colon or rectum?",
                                     font=basicFont, bg=baseColor, fg=textColor)
        colonMucularLabel.grid(row=3, column=1, sticky='w', pady=5, columnspan=2)

        # Through Colon Wall check ?
        throughColonCheck = tk.Radiobutton(formFrame, bg=baseColor, variable=self.__stage, value='stage 2A')
        throughColonCheck.grid(row=4, column=0, pady=5, sticky='e')

        # Through Colon Wall Label
        throughColonLabel = tk.Label(formFrame, text="Cancer cells have grown through the wall of the colon or rectum?",
                                     font=basicFont, bg=baseColor, fg=textColor)
        throughColonLabel.grid(row=4, column=1, sticky='w', pady=5, columnspan=2)

        # Through layer of muscle lining check ?
        throughMuscleLayersCheck = tk.Radiobutton(formFrame, bg=baseColor, variable=self.__stage, value='stage 2B')
        throughMuscleLayersCheck.grid(row=4, column=0, pady=5, sticky='e')

        # Through layer of muscle lining Label
        throughMuscleLayersLabel = tk.Label(formFrame,
                                            text="Cancer cells have grown through layers of the muscle to the lining of the abdomen?",
                                            font=basicFont, bg=baseColor, fg=textColor)
        throughMuscleLayersLabel.grid(row=4, column=1, sticky='w', pady=5, columnspan=2)

        # Nearby Structures check ?
        neverStructuresCheck = tk.Radiobutton(formFrame, bg=baseColor, variable=self.__stage, value='stage 2C')
        neverStructuresCheck.grid(row=5, column=0, pady=5, sticky='e')

        # Nearby Structures Label
        neverStructuresLabel = tk.Label(formFrame,
                                        text="Tumor has spread through the wall of colon or rectum into nearby structures?",
                                        font=basicFont, bg=baseColor, fg=textColor)
        neverStructuresLabel.grid(row=5, column=1, sticky='w', pady=5, columnspan=2)

        # Few Lymph Nodes check ?
        fewLympNodesCheck = tk.Radiobutton(formFrame, bg=baseColor, variable=self.__stage, value='stage 3A')
        fewLympNodesCheck.grid(row=6, column=0, pady=5, sticky='e')

        # Few Lymph Nodes  Label
        fewLympNodesLabel = tk.Label(formFrame,
                                     text="Tumor has spread into 1-3 lymph nodes or a module of is found in tissues around the colon?",
                                     font=basicFont, bg=baseColor, fg=textColor)
        fewLympNodesLabel.grid(row=6, column=1, sticky='w', pady=5, columnspan=2)

        # Through Bowel check ?
        throughBowelCheck = tk.Radiobutton(formFrame, bg=baseColor, variable=self.__stage, value='stage 3B')
        throughBowelCheck.grid(row=7, column=0, pady=5, sticky='e')

        # Through Bowel Label
        throughBowelLabel = tk.Label(formFrame,
                                     text="Tumor has grown thouugh the bowel wall and spread into 1-3 lymph nodes?",
                                     font=basicFont, bg=baseColor, fg=textColor)
        throughBowelLabel.grid(row=7, column=1, sticky='w', pady=5, columnspan=2)

        # Four Lymph Nodes check ?
        fourLymphCheck = tk.Radiobutton(formFrame, bg=baseColor, variable=self.__stage, value='stage 3C')
        fourLymphCheck.grid(row=8, column=0, pady=5, sticky='e')

        # Four Lymph Nodes Label
        fourLymphLabel = tk.Label(formFrame,
                                  text="Cancer has spread to four or more lymph nodes?",
                                  font=basicFont, bg=baseColor, fg=textColor)
        fourLymphLabel.grid(row=8, column=1, sticky='w', pady=5, columnspan=2)

        # Single Distant check ?
        singleDistantCheck = tk.Radiobutton(formFrame, bg=baseColor, variable=self.__stage, value='stage 4A')
        singleDistantCheck.grid(row=9, column=0, pady=5, sticky='e')

        # Single Distant Label
        singleDistantLabel = tk.Label(formFrame,
                                      text="Cancer has spread to a single distant part of the body (lungs, liver)?",
                                      font=basicFont, bg=baseColor, fg=textColor)
        singleDistantLabel.grid(row=9, column=1, sticky='w', pady=5, columnspan=2)

        # More Distant check ?
        moreDistantCheck = tk.Radiobutton(formFrame, bg=baseColor, variable=self.__stage, value='stage 4B')
        moreDistantCheck.grid(row=10, column=0, pady=5, sticky='e')

        # More Distant Label
        moreDistantLabel = tk.Label(formFrame,
                                    text="Cancer has spread to more than one part of the body?",
                                    font=basicFont, bg=baseColor, fg=textColor)
        moreDistantLabel.grid(row=10, column=1, sticky='w', pady=5, columnspan=2)

        # Peritoneum check ?
        peritoneumCheck = tk.Radiobutton(formFrame, bg=baseColor, variable=self.__stage, value='stage 4C')
        peritoneumCheck.grid(row=11, column=0, pady=5, sticky='e')

        # Peritoneum Label
        peritoneumLabel = tk.Label(formFrame,
                                   text="Cancer has spread to distant parts of the peritoneum "
                                        "(the lining of the abdominal cavity)?",
                                   font=basicFont, bg=baseColor, fg=textColor)
        peritoneumLabel.grid(row=11, column=1, sticky='w', pady=5, columnspan=2)

        # Nearby Structures Label
        neverStructuresLabel = tk.Label(formFrame,
                                        text="Tumor has spread through the wall of colon or rectum into nearby "
                                             "structures?",
                                        font=basicFont, bg=baseColor, fg=textColor)
        neverStructuresLabel.grid(row=5, column=1, sticky='w', pady=5, columnspan=2,padx=100)

        # Next Button
        nextBtn = tk.Button(formFrame, text='Next', command=lambda: dispFrame.nextClicked(), bg=titleFg,
                            fg=titleBg, font=btnFont)
        nextBtn.grid(row=12, column=0, columnspan=7, pady=15, ipadx=40)

    def sendData(self):
        radioArray = [self.__stage.get()]
        self.__radioSelectionArray = radioArray

    def getCheckedArray(self):
        return self.__radioSelectionArray

    def showNext(self):
        dispFrame.showFrame(ResultsPage)

    def setData(self, a, b, c):
        pass


class ResultsPage(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        resultsFrame = tk.Frame(self
                                , bg=baseColor
                                )
        resultsFrame.grid(row=0, column=0, sticky='N', ipady=50)
        resultsFrame.config(
            # bg='grey'
        )

        # Add Title Frame to Results Page Frame
        titleFrame = tk.Frame(resultsFrame)
        titleFrame.grid(row=0, column=0, sticky='N', pady=50, padx=400)

        # Add Welcome Text to Title Frame
        welcomeLbl = tk.Label(resultsFrame, text="Result and Recommendation",
                              font=titleFont,
                              height=3, anchor='center', bg=titleBg, fg=titleFg)
        welcomeLbl.grid(row=0, column=0, columnspan=6, sticky='nEW')

        # Add Form Frame To Welcome Page Frame
        formFrame = tk.Frame(resultsFrame,
                             bg=baseColor
                             )
        formFrame.grid(row=1, column=0, sticky='N', pady=(2, 64), padx=12)

        # Prediction Title Label
        predictionLabel = tk.Label(formFrame, text='Prediction', font=headingFont, anchor='center', bg=baseColor,
                                   fg=textColor)
        predictionLabel.grid(row=1, column=0, columnspan=7, pady=15, sticky='n')

        # Prediction Text Label
        self.__predictionText = StringVar()
        self.mee = 'bay'
        self.__predictionText.set(self.mee)
        predictionTextLabel = tk.Label(formFrame,
                                       textvariable=self.__predictionText,
                                       font=basicFont, bg=baseColor, fg=textColor, anchor='center')

        predictionTextLabel.grid(row=2, column=0, pady=5, columnspan=3)

        # Suggestion Title Label
        suggestionLabel = tk.Label(formFrame, text="Recommendation", font=headingFont, anchor='center', bg=baseColor,
                                   fg=textColor)
        suggestionLabel.grid(row=3, column=0, columnspan=3, pady=15)

        # Suggestion Text Label
        self.__suggestionText = StringVar()
        suggestionTextLabel = tk.Label(formFrame,
                                       textvariable=self.__suggestionText,
                                       font=basicFont, bg=baseColor, fg=textColor, anchor='center')
        suggestionTextLabel.grid(row=4, column=0, pady=5, columnspan=3)

        # download icon

        # Summary Title Label

        summaryLabel = tk.Label(formFrame, text='Caution', font=headingFont, anchor='center', bg=baseColor,
                                fg=textColor)
        summaryLabel.grid(row=5, column=0, columnspan=7, pady=15, sticky='n')

        # Summary Text Label
        self.__summaryText = StringVar()
        summaryTextLabel = tk.Label(formFrame,
                                    textvariable=self.__summaryText,
                                    font=basicFont, bg=baseColor, fg=textColor, anchor='center')
        summaryTextLabel.grid(row=6, column=0, pady=5, columnspan=3)

        # Summary Image button
        # btnImg = Image.open('downloadIcon.png')
        # resizedBtnImg = btnImg.resize((20, 20), Image.ANTIALIAS)
        # newBtnImg = ImageTk.PhotoImage(resizedBtnImg)

        # summaryBtn = tk.Button(formFrame, text='Download Summary', image=newBtnImg, border=1, compound=LEFT,
        #                      bg=baseColor, fg=textColor)
        # summaryBtn.image = newBtnImg
        # summaryBtn.grid(row=6, column=1, ipadx=5, ipady=2)

        # Next Button
        nextBtn = tk.Button(formFrame, text='Finish', command=lambda: dispFrame.clearMem(), bg=titleFg,
                            fg=titleBg, font=btnFont)
        nextBtn.grid(row=12, column=0, columnspan=7, pady=15, ipadx=40)

    def nextClicked(self):
        dispFrame.showFrame(WelcomePage)

    def setData(self, prediction, suggestion, summary):
        self.__predictionText.set(prediction)
        self.__suggestionText.set(suggestion)
        self.__summaryText.set(summary)


class PageController(tk.Frame):

    def __init__(self):
        super().__init__()
        self.p = Patient()
        self.res = None
        self.a = None
        self.b = None
        self.c = None
        self.collected = []

        self.frames = {}
        for f in (WelcomePage, WelcomePage, SymptomsPage, StagingPage, ResultsPage):
            frame = f()
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky='N', pady=(60, 120))
        self.showFrame(WelcomePage)

    def showFrame(self, toPage):
        frame = self.frames[toPage]
        self.frame = frame
        self.frame.setData(self.a, self.b, self.c)
        frame.tkraise()

    def nextClicked(self):
        frame = self.frame
        frame.sendData()
        frame.getCheckedArray()
        self.p.collectChecked(frame.getCheckedArray())
        try:
            self.p.collectName(frame.getName())
            self.p.collectAge(frame.getAge())
        except:
            pass
        self.a = self.p.getPredictionText()
        self.c = self.p.getSummaryText()
        self.b = self.p.getSuggestionText()
        frame.showNext()
        if self.p.showStagingPage():
            frame.showNext()
        else:
            try:
                frame.showNext2()
            except:
                pass

    def clearMem(self):
        frame = self.frame
        frame.nextClicked()
        self.p.__init__()


root = tk.Tk()
root.title('Cancer Expert System')
root.iconbitmap('logo.ico')
root.columnconfigure(0, weight=1)
root.geometry('960x680')

# Add background image to root frame
backgroundImg = ImageTk.PhotoImage(Image.open("cancerbg.jpg"))
imgCont = tk.Label(root, image=backgroundImg)
imgCont.grid(row=0, column=0, sticky='news')

# Create Welcome Page frame
dispFrame = PageController()

root.mainloop()
