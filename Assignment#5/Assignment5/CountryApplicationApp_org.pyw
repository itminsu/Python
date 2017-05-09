import sys
import csv
import locale

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPixmap

#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import CountryApplicationUI

#CHANGE THE SECOND PARAMETER HERE TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, CountryApplicationUI.Ui_MainWindow):
    locale.setlocale(locale.LC_ALL, '')  # system default locale
    dataFileName = "countries.txt"

    KILOMETERS_PER_MILE = 1.609344
    changesToSave = False
    sqMiChecked = True
    # declare a list variable that will hold all
    # of the countries data loaded from file into memory
    countries = []

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

        # Hide each widget when initializing
        self.hideWidgets()

        # Disable Save menu item to prevent list of countries from being saved before loading
        self.actionSave.setEnabled(False)

        # ADD SLOTS HERE
        # A slot for when the menu item of 'Load Countries...' is clicked
        self.action_Load_Countries.triggered.connect(self.push_load_countries)
        # # A slot for exit program
        self.action_Exit.triggered.connect(self.exit_program)
        # A slot for saving changes into the countries
        self.pushButton_update_population.clicked.connect(self.SaveCountriesToList)
        # A slot for when an item is selected in the list
        self.listWidget_country_lists.currentRowChanged.connect(self.country_selected_from_list)
        # A slot for converting to other area unit in area
        self.comboBox_choose_way.currentIndexChanged.connect(self.comboboxChanged)
        # A slot for converting to other area unit in population density
        self.radioButton_sqKM.clicked.connect(self.radio_KM_clicked)
        self.radioButton_sqMi.clicked.connect(self.radio_Mi_clicked)

    # ADD SLOT FUNCTIONS HERE
    def push_load_countries(self):
        self.LoadCountriesFromFile(self.dataFileName)
        self.LoadCountriesListBox()

    def country_selected_from_list(self, selected_index):
        self.showWidgets()# Show each widget only when a country is selected
        self.DisplayCountryData(selected_index)

    def comboboxChanged(self):
        area_unit = self.comboBox_area_unit.currentText()
        if area_unit == 'Sq. Mi.':
            self.convertArea("Mi")
            self.convertDensity("Mi")
            self.radioButton_sqMi.setChecked(True)
            self.radioButton_sqKM.setChecked(False)
            self.sqMiChecked = True

        elif area_unit == 'Sq. KM.':
            self.convertArea("KM")
            self.convertDensity("KM")
            self.radioButton_sqMi.setChecked(False)
            self.radioButton_sqKM.setChecked(True)
            self.sqMiChecked = False

    def radio_Mi_clicked(self, enabled):
        if enabled:
            self.convertDensity("Mi")
            self.convertArea("Mi")
            self.comboBox_area_unit.setCurrentIndex(0) # Sq. Mi.
            self.sqMiChecked = True

    def radio_KM_clicked(self, enabled):
        if enabled:
            self.convertDensity("KM")
            self.convertArea("KM")
            self.comboBox_area_unit.setCurrentIndex(1) # Sq. KM.
            self.sqMiChecked = False

    def exit_program(self):
        QApplication.closeAllWindows()

    def SaveCountriesToList(self):
        list_population = self.lineEdit_population.text().split(',')
        population = ''.join(list_population)
        if population.isdigit() == False:
            QMessageBox.information(self,
                                'Error',
                                'Please enter a valid number of population..',
                                QMessageBox.Ok)
            self.lineEdit_population.hasFocus()
        else:
            # determine the index of the currently selected country in the list
            selected_index = self.listWidget_countries.currentRow()
            # update the data in memory (countries[]) with the values in the text boxes
            self.countries[selected_index][1] = population
            self.changesToSave = True
            self.actionSave.setEnabled(True) # Enable save menu item to save the countries list to a file
            # reload the country data selected
            QMessageBox.information(self,
                                'Updated',
                                'Population updated...',
                                QMessageBox.Ok)
            self.DisplayCountryData(selected_index)

    def SaveCountriesToFile(self):
        # call the save_changes_to_file helper function which does the heavy lifting
        self.save_changes_to_file()
        # popup a message to the user confirming that the changes were saved to the file
        QMessageBox.information(self, 'Saved', 'Changes were saved to the file', QMessageBox.Ok)
        # toggle the unsaved_changes variable back to False because we no longer have any unsaved changes
        self.changesToSave = False

    #ADD HELPER FUNCTIONS HERE
    def save_changes_to_file(self):
        # open the file for writing (w)
        with open(self.dataFileName, "w") as myFile:
            #loop through each list within the in-memory countries list
            for country in self.countries: #<- refer to each list as country
                # join each value in the country list and write them with a line break
                myFile.write(",".join(country) + "\n")

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

    def LoadCountriesFromFile(self, dataFileName):
        self.countries.clear()

        # open txt file with csv reader and read data into countries list
        with open(dataFileName, "r") as myFile:
            # load data into reader object
            fileData = csv.reader(myFile)
            # loop through each line in reader...each line is a list of values
            for row in fileData:
                # add each list to the countries list variable declared above
                self.countries.append(row)

    def LoadCountriesListBox(self):
        self.listWidget_countries.clear()

        for country in self.countries:
            self.listWidget_countries.addItem(country[0])

    def DisplayCountryData(self, selected_index): #<- selected_index is the index of the item that was selected in the ui list

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

    def CalculateAreaInKM(self, countryAreaInMiles):
        return countryAreaInMiles * (1.609344**2)

    def DisplayPopulationData(self):
        self.lineEdit_population.setText('{0:,}'.format(self.country_population))
        self.label_density.setText(locale.format('%.2f', self.country_density_mile, 1))
        self.label_percentage_display.setText('{0:.3%}'.format(self.country_percentage))
        if(self.sqMiChecked == True): # Sq. Mi.
            self.radioButton_sqMi.setChecked(True)
            self.radioButton_sqKM.setChecked(False)
            self.comboBox_area_unit.setCurrentIndex(0) # Sq. Mi.
        else: # Sq. KM.
            self.radioButton_sqMi.setChecked(False)
            self.radioButton_sqKM.setChecked(True)
            self.comboBox_area_unit.setCurrentIndex(1) # Sq. KM.

    def image_display(self, country_name):
        flag = country_name.split()
        if len(flag) > 1:
            country_name = '_'.join(flag)
        image = QPixmap("Flags\{}.png".format(country_name))
        #set the label with the selected pixmap
        self.label_flag.setPixmap(image)

    def convertArea(self, area_unit):
        if area_unit == 'KM':
            self.label_area_display.setText(locale.format('%.2f', self.country_area_kilometer, 1))
        elif area_unit == 'Mi':
            self.label_area_display.setText(locale.format('%.2f', self.country_area_mile, 1))

    def convertDensity(self, area_unit):
        if area_unit == 'KM':
            self.label_density.setText(locale.format('%.2f', self.country_density_kilometer, 1))
        elif area_unit == 'Mi':
            self.label_density.setText(locale.format('%.2f', self.country_density_mile, 1))

    def CalculateTotalWorldPopulation(self):
        sum = 0.0
        for country in self.countries:
            sum += int(country[1])
        return sum

    def closeEvent(self, event):

        if self.changesToSave == True:
            msg = "Save changes to file before closing?"
            reply = QMessageBox.question(self, 'Save?',
                     msg, QMessageBox.Yes, QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.save_changes_to_file()
                event.accept()

# DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
# END DO NOT MODIFY
