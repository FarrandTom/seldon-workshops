from seldon_core.seldon_client import SeldonClient

endpoint = "0.0.0.0:9001"

data = ['COC(C)(C)CCCC(C)CC=CC(C)=CC(=O)OC(C)C',
          'CCOC(=O)CC',
          'CSc1nc(NC(C)C)nc(NC(C)C)n1',
          'CC(C#C)N(C)C(=O)Nc1ccc(Cl)cc1',
          'Cc1cc2ccccc2cc1C']

sc = SeldonClient(microservice_endpoint=endpoint)
response = sc.microservice(
   json_data = data,
   method='predict'
)

print(response.request)
print(response.response)