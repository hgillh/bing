# Bing Search (POC)

###### Bing search is a POC developed wityh Python 3.8, Django, DynamoDB, Big Web Search API and Docker

## Instructions to Setup and Run

---

#### Clone the repo on your local system

```python
git clone https://github.com/hgillh/bing.git
```

#### Setup containers and run

```python
cd <project_folder>
docker-compose up --build
```

###### It will configure the DynmoDB container and an Ubuntu 20.04 container. On Ubuntu 20.04, it will configure Django project and start it on port: 8080.

## Other Details

-   It will start DynamoDB on port 8000 with default settings
    -- It will presist the DynamoDB data on restart of container. Used Docker volume for the same
    --More detials at : https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html
-   It is using Bing Web Search API to fetch bing search results.
    --It is using Bing sandbox API key, which will expire after a week
    --https://docs.microsoft.com/en-us/azure/cognitive-services/bing-web-search/
