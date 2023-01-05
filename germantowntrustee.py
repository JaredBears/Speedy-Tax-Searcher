
class GermantownTrustee:
    url = "https://germ-egov.aspgov.com/Click2GovTX/accountsearch.html?"

    def searchProperty(self, property):
        parcel = property.getParcelId()
        district = parcel[0:3]
        block = parcel[3:6]
        sub = parcel[6]
        lot = parcel[7:]
        print(district, block, sub, lot)
        