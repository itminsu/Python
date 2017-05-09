import sys
import csv
import locale

from PyQt5.QtWidgets import QApplication, QMainWindow

#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import CountryApplicationUI

#CHANGE THE SECOND PARAMETER HERE TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, CountryApplicationUI.Ui_MainWindow):
    countries = []
    dataFileName = "countries.txt"

    country_name = ''
    country_population = 0
    country_area_mile = 0.0
    country_area_kilometer = 0.0
    country_density_mile = 0.0
    country_density_kilometer = 0.0
    country_percentage = 0.0

        # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        # END DO NOT MODIFY
        self.hideWidgets()
        # ADD SLOTS HERE
        self.action_Load_Countries.triggered.connect(self.push_load_countries)
        self.listWidget_country_lists.currentRowChanged.connect(self.country_selected_from_list)

    # ADD SLOT FUNCTIONS HERE
    def push_load_countries(self):
        self.LoadCountriesFromFile(self.dataFileName)
        self.LoadCountriesListBox()
    def country_selected_from_list(self, selected_index):
        self.showWidgets()# Show each widget only when a country is selected
        self.DisplayCountryData(selected_index)

    #ADD HELPER FUNCTIONS HERE

    def DisplayCountryData(self, selected_index):
        # retrieve the appropriate data from the countries list which
        # contains the data that was loaded from the file
        self.country_name = self.countries[selected_index][0] #<- 0 is the country name (the first value in the line)
        self.country_population = int(self.countries[selected_index][1])  #<- 1 is the country's population (the second value in the line)
        self.country_area_mile = float(self.countries[selected_index][2])  #<- 1 is the country's area (the 3rd value in the line)
        self.country_area_kilometer = self.CalculateAreaInKM(self.country_area_mile)
        self.country_density_mile = self.country_population/self.country_area_mile
        self.country_density_kilometer = self.country_density_mile / (self.KILOMETERS_PER_MILE ** 2)
        self.country_percentage = self.country_population / self.CalculateTotalWorldPopulation()

        # set the values to the labels, image and line edit on the form
        self.label_countryname.setText(self.country_name)
        self.image_display(self.country_name)

        self.label_area_display.setText(locale.format('%.2f', self.country_area_mile, 1))
        self.DisplayPopulationData()


    def LoadCountriesFromFile(self, dataFileName):
        # open txt file with csv reader and read data into countries list
        with open(dataFileName, "r") as myFile:
            # load data into reader object
            fileData = csv.reader(myFile)
            # loop through each line in reader...each line is a list of values
            for row in fileData:
                # add each list to the countries list variable declared above
                self.countries.append(row)

    def LoadCountriesListBox(self):
        self.listWidget_country_lists.clear()
        for country in self.countries:
            self.listWidget_country_lists.addItem(country[0])

    def hideWidgets(self):
        self.label_population.hide()
        self.lineEdit_population.hide()
        self.label_area_static.hide()
        self.label_population_3.hide()
        self.comboBox_area_unit.hide()
        self.label_area_display.hide()
        self.groupBox_density.hide()
        self.radioButton_sqMi.hide()
        self.radioButton_sqKM.hide()
        self.label_density.hide()
        self.label_percentage_static.hide()
        self.label_percentage_display.hide()
        self.pushButton.hide()

    def showWidgets(self):
        self.label_population.show()
        self.lineEdit_population.show()
        self.label_area_static.show()
        self.label_population_3.show()
        self.comboBox_area_unit.show()
        self.label_area_display.show()
        self.groupBox_density.show()
        self.radioButton_sqMi.show()
        self.radioButton_sqKM.show()
        self.label_density.show()
        self.label_percentage_static.show()
        self.label_percentage_display.show()
        self.pushButton.show()

# DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
# END DO NOT MODIFY
