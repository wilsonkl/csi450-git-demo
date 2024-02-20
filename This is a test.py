#This is a test
def Test(status):
    if status == "test":
        print("neat")
Test('test')

#https://api.eia.gov/v2/electricity/electric-power-operational-data/data/?frequency=monthly&data[0]=total-consumption-btu&facets[fueltypeid][]=ALL&facets[fueltypeid][]=AOR&facets[fueltypeid][]=COW&facets[fueltypeid][]=FOS&facets[fueltypeid][]=NGO&facets[fueltypeid][]=NUC&facets[fueltypeid][]=SUN&start=2023-01&end=2023-02&sort[0][column]=location&sort[0][direction]=desc&offset=0&length=5000&api_key=u7e5iYnTkIJ7cwq2emALYbwgolqCG7DKuXRpaHPC