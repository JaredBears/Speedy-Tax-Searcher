import shelbyassessor
import shelbytrustee
import memphistrustee
import property

def main():
    parcelId = "06303400001"
    assessor = shelbyassessor.ShelbyAssessor()
    countyTrustee = shelbytrustee.ShelbyTrustee()
    cityTrustee = memphistrustee.MemphisTrustee()
    prop = property.Property(parcelId)
    assessor.searchProperty(prop)
    countyTrustee.searchProperty(prop)
    cityTrustee.searchProperty(prop)
    print(prop)


main()