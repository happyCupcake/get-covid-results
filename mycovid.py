import sys
#import json
from covid import Covid



# to get data from worldometers.info
covid = Covid(source="worldometers")

# get all data
#covid_data = covid.get_data()
countries = covid.list_countries()

#print(covid_data)
#print(countries)

country_cases = covid.get_status_by_country_name(sys.argv[1])

#json_cases = json.loads(country_cases)

print(country_cases["new_cases"])