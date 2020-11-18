from pyswip import Prolog

prolog = Prolog()


class Backend:
    def __init__(self):
        pass


class Patient:
    # initialize the Patient class
    def __init__(self):
        self.__patientChecked = []
        self.__myprediction = ''
        self.__patientName = ''
        self.__cancerStage = ''
        self.__predictionText = ''
        self.__suggestionText = ''
        self.__age = 0

    # Function to collect patient name
    def collectName(self, name):
        self.__patientName = name

    # Function to collect patient age
    def collectAge(self, age):
        self.__age = age

    # Function to collect the array of checked boxes
    def collectChecked(self, checkedArr):
        for checks in checkedArr:
            if checks not in (
                    'stage 0', 'stage 1', 'stage 2A', 'stage 2B', 'stage 2C', 'stage 3A', 'stage 3B', 'stage 3C',
                    'stage 4A', 'stage 4B', 'stage 4C'):
                if checks != 'unchecked':
                    self.__patientChecked.append(checks)

            else:
                self.__cancerStage = checks + " "

        self.knowledgeBase(self.__patientChecked)

    def knowledgeBase(self, patientChecked):

        for checked in patientChecked:
            prolog.assertz("true(" + checked + ")")

        prolog.assertz(
            "hypothesis('not likely'):- true(diet),true(obese); true(vomiting),true(inflamatoryCondition);"
            "true(breathingDiff),true(radiationTherapy);true(excessFart),true(bodySwell);true(chronicHeadache),"
            "true(blurryVision);true(alcohol);true(boneFracture)")

        prolog.assertz(
            "hypothesis('not likely'):- true(diet);true(obese), true(vomiting);true(inflamatoryCondition),"
            "true(breathingDiff);true(radiationTherapy),true(excessFart);true(bodySwell),true(chronicHeadache);"
            "true(blurryVision),true(alcohol),true(boneFracture)")

        prolog.assertz(
            "hypothesis('less likely'):- "
            "true(diet),true(obese), true(vomiting),true(inflamatoryCondition),"
            "true(breathingDiff),true(radiationTherapy),true(excessFart);true(bodySwell),true(chronicHeadache),"
            "true(blurryVision),true(alcohol)")

        prolog.assertz(
            "hypothesis('less likely'):- "
            "true(diet),true(obese), true(vomiting),true(inflamatoryCondition),"
            "true(breathingDiff),true(bodySwell);true(chronicHeadache),true(blurryVision),true(alcohol)"
            ",true(radiationTherapy),true(excessFart)")

        prolog.assertz(
            "hypothesis('likely'):- "
            "true(stoolBlood),true(weightLoss);true(abdominalPain),true(abdominal"
            "Cramps);true(abdominalCramps),true(excessiveFatigue); true(constipation), true(stoolChange);"
            "true(stoolShape),true(rectumBleeding);true(diarrhea),true(diabetesHistory)")
        prolog.assertz(
            "hypothesis('likely'):- "
            "true(abdominalPain),true(weightLoss);true(stoolBlood),true(abdominal"
            "Cramps);true(constipation),true(excessiveFatigue);true(abdominalCramps),true(stoolChange);"
            "true(stoolShape),true(diarrhea);true(rectumBleeding),true(diabetesHistory)")

        prolog.assertz(
            "hypothesis('very likely'):- "
            "true(abdominalPain),true(weightLoss),true(stoolBlood),true(abdominal"
            "Cramps);true(constipation),true(excessiveFatigue),true(abdominalCramps),true(stoolChange);"
            "true(stoolShape),true(diarrhea),true(rectumBleeding),true(diabetesHistory)")

        prolog.assertz(
            "hypothesis('very likely'):- "
            "true(abdominalPain),true(weightLoss),true(abdominalCramps),true(stoolChange);"
            "true(constipation),true(excessiveFatigue),true(stoolBlood),true(abdominalCramps);true(stoolShape),"
            "true(diarrhea),true(rectumBleeding),true(diabetesHistory)")

        prolog.assertz(
            "hypothesis('very likely'):- "
            "true(abdominalPain),true(diabetesHistory),true(abdominalCramps), "
            "true(stoolChange);true(constipation),true(excessiveFatigue),true(stoolBlood),true(rectumBleeding);"
            "true(stoolShape),true(diarrhea),true(abdominalCramps),true(weightLoss)")

        checkHypothesis = prolog.query("hypothesis(Hypothesis).")

        hypothesis = list(checkHypothesis)
        self.__myprediction = ""
        for message in hypothesis:
            self.__myprediction = message['Hypothesis']

        if self.__myprediction == "":
            self.__myprediction = "unclear if"

        self.__predictionText = "It is " + self.__myprediction + " patient " + self.__patientName + " has " + self.__cancerStage + \
                                "colorectal cancer"

    # functions that determines whether to show the cancer staging page or not
    def showStagingPage(self):
        if self.__myprediction == "unclear if":
            self.__suggestionText = "Your selections do not show clear symptoms of Colorectal cancer consult a doctor " \
                                    "for further tests."
            return False
        elif self.__myprediction == "not likely":
            self.__suggestionText = "Your selections do not show clear symptoms of Colorectal cancer consult a doctor " \
                                    "for further tests."
            return False
        elif self.__myprediction == "less likely":
            self.__suggestionText = "Your selections do not show clear symptoms of Colorectal cancer consult a doctor " \
                                    "for further tests."
            return False
        elif self.__myprediction == "likely":
            self.__suggestionText = "Your selections show symptoms of Colorectal cancer consult a doctor " \
                                    "for further tests."
            return True
        elif self.__myprediction == "very likely":
            self.__suggestionText = "Your selections show high symptoms of Colorectal cancer consult a doctor " \
                                    "immediately for further tests."
            return True
        else:
            self.__suggestionText = "I have no recommendations"
            return False

    # Function to get the cancer stage
    def getCancer(self):
        return self.__cancerStage

    # function that returns the prediction text to the UI
    def getPredictionText(self):
        return self.__predictionText

    # function that returns the suggestion text to the UI
    def getSuggestionText(self):
        return self.__suggestionText

    # function that returns the summary text to the UI
    def getSummaryText(self):
        return "This system should only be used as a guide as it does not replace an expert doctor.\nConsult a trained " \
               "doctor for more accurate diagnosis. "
