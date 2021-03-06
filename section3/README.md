![Image of System Design](https://github.com/ya0z/dataeng_test/blob/main/section3/dataeng_test_section3.jpg)
## Assumption
- The image processing codes will not be supported by the new infrastructure.
- The new infrastructure will be on Azure Cloud.
- Files deletion do not need to be recorded.
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

5. Clean up files that are more than 7 days: we can use Blob Lifecycle Management by defining a policy to delete blobs if they are older than 7 days.
Reference: [Blob Lifecycle Management!](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-lifecycle-management-concepts)
