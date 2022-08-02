# Description of the task
The task on hand is to write an Azure function which gets the current weather data from https://www.weatherapi.com every 1 hour, and saves it as a JSON file into a Blob Storage Container in Azure.

In order to use the api from https://www.weatherapi.com the API key needs to be generated.
The current key is: 5bd8a9107488438db57171650212212
The city chosen is : Szeged

When the function runs it will create a json file with the UTC datetime as the file name. 
The function runs hourly.

the URL of the azure Storage Blob is: 
https://jalalapiblob.blob.core.windows.net/outcontainer
Where the output files are found.

for the purpose of the evaluation of the files, the Blob container was made anonymous. 
