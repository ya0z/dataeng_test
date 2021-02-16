#System Design
## Assumption
- The image processing codes will not be supported by the new infrastructure.
- The new infrastructure will be on Azure Cloud.
## Infrastructure Design
1. Create a resource group which house the following resources
- Azure Function
- Event Hub / Grid
- An SQL database (e.g. Cosmos DB)
- Storage Account (Blob)
- Power BI

2. Azure Function will consume the API / Events that uploads the image.
- Image will be stored as blob in the storage account
- Meta information e.g. customer/image info will be stored in the SQL database

3. Event Hub / Grid will consume the existing Kafka stream of images
- Image will be stored as blob in the storage account via Azure Function API call
- Meta information e.g. customer/image info will be send to Azure Function via API calls, which will then be stored in the SQL database

4. Power BI can then connect to the SQL database to generate statistics.