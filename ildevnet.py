from locale import atof, setlocale, LC_NUMERIC
from bs4 import BeautifulSoup
from urllib.request import urlopen
from property import Property

setlocale(LC_NUMERIC, 'English_United States.1252')

class IlDevNet:
    countyDict = {
        "ADAMS" : "adamsil",
        "CARROLL" : "carrollil",
        "CUMBERLAND" : "cumberlandil",
        "DEKALB" : "dekalbil",
        "EFFINGHAM" : "effinghamil",
        "FRANKLIN" : "franklinil",
        "FULTON" : "fultonil",
        "HENRY" : "henryil",
        "JERSEY" : "jerseyil",
        "KENDALL" : "kendallil",
        "LIVINGSTON" : "livingstonil",
        "MARION" : "marionil",
        "MCDONOUGH" : "mcdonoughil",
        "MCHENRY" : "mchenryil",
        "MORGAN" : "morganil",
        "PERRY" : "perryil",
        "SALINE" : "salineil",  
        "STCLAIR" : "stclairil",
        "STEPHENSON" : "stephensonil",
        "VERMILION" : "vermilionil",
        "WASHINGTON" : "washingtonil",

    }

    domain = ".devnetwedge.com/parcel/view/"

    def countyCheck(self, county):
        if county in self.countyDict:
            return True
        else:
            return False

    def searchProperty(self, property):
        parcel = property.getParcelId()
        county = property.getCounty()
        url = "https://" + self.countyDict[county] + self.domain + parcel
        print(url)
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find_all("table")
        assessment = atof(table[0].find_all("div")[19].text.strip())
        property.setAssessment(assessment)
        address = table[3].find_all("td")[2].text.strip().split("\n")[0]
        property.setAddress(address)
        legal = " ".join(table[0].find_all("td")[14].find_all("p")[0].text.strip().split("\r\n"))
        property.setLegalDescription(legal)
        taxes = atof(table[5].find_all("td")[3].text[1:])
        property.setCountyTaxes(taxes)
    def test(self):
        mchenry= Property("1435451010","IL", "MCHENRY")
        self.searchProperty(mchenry)
        print(mchenry)

ildevnet = IlDevNet()
ildevnet.test()