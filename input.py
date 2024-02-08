# Description: This script demonstrates how to use the Benchling SDK to list DNA sequences in your Benchling account.
# To run this script, you will need to install the Benchling SDK. You can do this by running the following command:
# pip install benchling-sdk
# You will also need to replace the placeholders in the code below with your own credentials.

# if you are using OAuth2, you can use the following code:
from benchling_sdk.benchling import Benchling
from benchling_sdk.auth.client_credentials_oauth2 import ClientCredentialsOAuth2

auth_method = ClientCredentialsOAuth2(client_id="{id_here}",client_secret="{secret_here}")
benchling = Benchling(url="https://{tenant_name}.benchling.com", auth_method=auth_method)


# if you are using an API key, you can use the following code:
# from benchling_sdk.benchling import Benchling
# from benchling_sdk.auth.api_key_auth import ApiKeyAuth
#
# benchling = Benchling(url="https://my.benchling.com", auth_method=ApiKeyAuth("api_key"))

example_entities = benchling.dna_sequences.list()
for page in example_entities:
    for sequence in page:
        print(f"name: {sequence.name}\nid:{sequence.id}\n")
