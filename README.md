# Willow Labs Python API
Willow labs APIs offers services to get information regarding companies and related entities. The main companents are:

|build-status| |docs|

* Information about the owners of a comapny. This service provides owners at all levels, meaning it recursively goes trough the ownership structure until a private owner is established.
* Basic company information as address, industry, number of employees and more.
* Signature rights and prokura holders for a comapny.
* Roles connected to the company, for example CEO, board members, accountant.


| Service name                             | Descritpion                          | Language  |
| ---------------------------------------- |:-------------------------------------| :--------- |
| get_basic_company_information            | Basic information                    | English   |
| get_company_ownership                    | Get the full ownership structure     | English   |
| get_company_power_of_attorney            | Get everyone with power of attorny.  | English   |
| get_company_prokura                      | Get everyone with prokura rights.    | Norwegian |
|                                          | Same as get_company_power_of_attorney|           |
| get_company_full_signatory_authority     | All signature holders                | English   |
| get_company_signatur                     | Get all signature holders. Same as   | Norwegian |
|                                          | get_company_full_signatory_authority |           |
| get_company_signatory_information        | Get the authority holder for a       | English   |
|                                          | given authorithy.                    |           |
| get_company_roles                        | Get all roles connect to a company.  | English   |


## Installation
``` pip install -U willowlabs ```

## Example usage
```
   from willowlabs.company_information.client import CompanyInformationClient
   client = CompanyInformationClient("client_config.yaml")
   company_basic_results = client.get_basic_company_information(organisation_number)
   company_ownership_results = client.get_company_ownership(organisation_number, record_year)
```

## Documentation
[Read the docs](https://willow-labs-python-api.readthedocs.io/en/doc_release/)


## Versions
### 0.4.0 (current) 
Relased 16.04.2020.

Change in import structure.

### 0.3.0  
Relased 15.04.2020.

Bugg fixes.

### 0.2.0 
Relased 04.04.2020.

First beta version: Basic functionality.

.. |build-status| image:: https://img.shields.io/travis/readthedocs/readthedocs.org.svg?style=flat
    :alt: build status
    :scale: 100%
    :target: https://travis-ci.org/readthedocs/readthedocs.org

.. |docs| image:: https://readthedocs.org/projects/docs/badge/?version=latest
    :alt: Documentation Status
    :scale: 100%
    :target: https://willow-labs-python-api.readthedocs.io/en/doc_release/#?badge=doc_release

License
-------

`MIT`_ © 2010-2019 Read the Docs, Inc & contributors

.. _MIT: LICENSE
