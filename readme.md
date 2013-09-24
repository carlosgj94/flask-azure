# Flask-Azure

A `ResourceProvider` template for integrating with the Azure app store. Based on [Azure's example](https://github.com/WindowsAzure/azure-resource-provider-sdk/tree/master/samples/python-flask), but in its own repo for ease of deployment.

## Install

Get the repo, install dependencies, and proceed to dance:

    git clone git@github.com:garbados/flask-azure.git
    cd flask-azure
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    echo "now it is time to dance" | say

## Usage

A `ResourceProvider` performs CRUD operations on a handful of models that are mocked out in `/resourceprovider/models.py`. To make them work, you'll need to implement the no-ops.

To make sure your implement is up to spec: 

  python resourceprovider/tests.py