from locale import atof, setlocale, LC_NUMERIC
import mechanicalsoup
from property import Property

setlocale(LC_NUMERIC, 'English_United States.1252')

class BartlettTrustee:
    url = "https://cityofbartlett.munisselfservice.com/css/citizens/RealEstate/Default.aspx?mode=new"

    def searchProperty(self, property):
        try:
            parcel = property.getParcelId()
            browser = mechanicalsoup.StatefulBrowser()
            browser.open(self.url)
            browser.select_form("form")
            browser["ctl00$ctl00$PrimaryPlaceHolder$ContentPlaceHolderMain$Control$ParcelIdSearchFieldLayout$ctl01$ParcelIDTextBox"] = parcel
            browser.submit_selected("ctl00$ctl00$PrimaryPlaceHolder$ContentPlaceHolderMain$Control$FormLayoutItem7$ctl01$Button1")
            page = browser.get_current_page()
            table = page.find_all("table")[0]
            td = table.find_all("td")
            taxes = atof(td[11].text[1:])
            property.setCityTaxes(taxes)
        except:
            property.setCityTaxes(-1)
    def test(self):
        property = Property("B0149M00007", "Shelby")
        self.searchProperty(property)
        print(property.getCityTaxes())

# bartlett = BartlettTrustee()
# bartlett.test()