# Prerequisite:
- Python 3 is needed
- cron need to be installed
- python3 pandas need to be installed
```
pip install pandas
```
# Processing logic:
## Assumptions
- The dataset will arrive in the filename *dataset.csv* exactly at 1am daily.
- The output dataset will be the filename *dataset-output.csv*
- Salutation list can be found: [salutation list](https://www.codeproject.com/Questions/262876/Titles-or-Salutation-list), assuming the salutation is prefix of the name field.
- Using pandas dataframe float64 datatype will automatically remove zero-padding in the price column.
- Assume *above_100* field is false if it is less than 100 or equal to 100.
- Assume the following fields are needed: first_name, last_name, price, above_100
## Steps
- Using pandas Dataframe to create the dataframe for processing
- Drop the row that do not have a *name*.
- Clean the name by removing salutation from the start of the name field.
- Split the name into first_name and last_name
- Create the *above_100* field
- Select the fields required: first_name, last_name, price, above_100
- Create the output csv file.
## Cron
Please load the cron job with the cronjob file
```
crontab cronjob
```
Everyday, the cron job will run at 1AM at the 0-minute.