from locale import atof, setlocale, LC_NUMERIC
from bs4 import BeautifulSoup
from urllib.request import urlopen
from shelbytrustee import ShelbyTrustee
from memphistrustee import MemphisTrustee
from bartletttrustee import BartlettTrustee
from germantowntrustee import GermantownTrustee
from property import Property

setlocale(LC_NUMERIC, 'English_United States.1252')

class ShelbyAssessor:
    url = "https://www.assessormelvinburgess.com/propertyDetails?parcelid="
    countyTrustee = ShelbyTrustee()
    memphisTrustee = MemphisTrustee()
    bartlettTrustee = BartlettTrustee()
    germantownTrustee = GermantownTrustee()

    def searchProperty(self, property):
        try:
            parcel = property.getParcelId()
            page = urlopen(self.url + parcel)
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            table = soup.find_all("td")
            property.setAddress(self.getAddress(table))
            property.setCity(self.getCity(table))
            property.setLegalDescription(self.getLot(table) + " - " + self.getSubdivision(table) + " - " + self.getPlatBookPage(table))
            property.setMailingStreet(self.getMailingStreet(table))
            property.setMailingCity(self.getMailingCity(table))
            property.setAppraisedValue(self.getAppraisal(table))
            property.setAssessment(self.getAssessment(table))
            self.countyTrustee.searchProperty(property)
            if parcel[0] == '0':
                self.memphisTrustee.searchProperty(property)
            elif parcel[0] == 'B':
                self.bartlettTrustee.searchProperty(property)
            elif parcel[0] == 'G':
                self.germantownTrustee.searchProperty(property)
        except:
            property.setNotes("Error: Could not find all property information - Please verify details.")
    def getAddress(self, table):
        return table[3].text.strip()
    def getCity(self, table):
        return table[5].text.strip()
    def getSubdivision(self, table):
        return table[17].text.strip()
    def getLot(self, table):
        return table[19].text.strip()
    def getPlatBookPage(self, table):
        return table[21].text.strip()
    def getOwner(self, table):
        return table[25].text.strip()
    def getMailingStreet(self, table):
        return table[27].text.strip()
    def getMailingCity(self, table):
        return table[29].text.strip()
    def getAppraisal(self, table):
        return atof(table[40].text.strip()[1:])
    def getAssessment(self, table):
        return atof(table[42].text.strip()[1:])

    def test(self):
        memphis = Property("06303400001", "TN", "SHELBY")
        self.searchProperty(memphis)
        print(memphis)
        print(memphis.toCSV())
        print(memphis.toJSON())

        # bartlett = Property("B0149M00007", "TN", "SHELBY")
        # self.searchProperty(bartlett)
        # print(bartlett)
        # print(bartlett.toCSV())
        # print(bartlett.toJSON())

        # germantown = Property("G0221EH00027", "TN", "SHELBY")
        # self.searchProperty(germantown)
        # print(germantown)
        # print(germantown.toCSV())
        # print(germantown.toJSON())
        

ShelbyAssessor().test()