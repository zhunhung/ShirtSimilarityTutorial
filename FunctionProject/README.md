# ShirtSimilarityTutorial - Azure Functions
Architecting your app and deploying to Azure Functions

## Prerequisites

By now, you should have already went through the notebook and understand how to create embeddings. Otherwise, please complete those first:

1. [Code Explanation](https://github.com/zhunhung/ShirtSimilarityTutorial/tree/master/Notebook) - Notebook explaining how it works

### Getting Started

In order to deploy your own function, you will need to have an [Azure subscription](https://azure.microsoft.com/en-us/free/). If you do not, do sign up as it has free tiers for you to explore.

### Deployment

Refer to the step-by-step deployment guide [here](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-vs-code)

### Testing your deployed function

*POST request*

```bash
curl -i -X POST -k https://XXX.azurewebsites.net/api/ShirtSim?code=XXX 
-F "file=@{path_to_test_image}"
```

*Response*

```
[{"result": "shirt2.jpg", "filename": "test3.jpg", "score": 0.7708896352246695}]
```



