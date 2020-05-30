from willowlabs.company_information.client import CompanyInformationClient
import datetime as dt
import csv

org_list = [
    917811210,
    917811253,
    917811288,
    917811385,
    917811539,
    917811733,
    917811741,
    917811849,
    917811903,
    917812284,
    917812306,
]


client = CompanyInformationClient("C:\\Users\\Sven\\projects\\client_config.yaml")


error_list = []

for org in org_list:
    result = client.get_company_roles(org, query_date=dt.datetime.today())
    print(result)

    error_list.append([org, result.server_error])


with open("testing_out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(error_list)
