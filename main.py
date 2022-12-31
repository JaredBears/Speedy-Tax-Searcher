import shelbyassessor
import shelbytrustee
import memphistrustee

def main():
    assessor = shelbyassessor.ShelbyAssessor()
    countyTrustee = shelbytrustee.ShelbyTrustee()
    cityTrustee = memphistrustee.MemphisTrustee()
    property = assessor.searchProperty("06303400001")
    countyTrustee.searchProperty(property)
    cityTrustee.searchProperty(property)
    print(property)


main()