

Welcome to Willow Labs Python API's documentation!
==================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Willow labs APIs offers services to get information regarding companies and related entities. The main companents are:

* Information about the owners of a comapny. This service provides owners at all levels, meaning it recursively goes trough the ownership structure until a private owner is established.
* Basic company information as address, industry, number of employees and more.
* Signature rights and prokura holders for a comapny.
* Roles connected to the company, for example CEO, board members, accountant.


	
+-----------------------------------------+-------------------------------+-----------+
| Service name                            | Descritpion                   | Language  |
+=========================================+===============================+===========+
| get_basic_company_information           | Basic information             |  English  |
+-----------------------------------------+-------------------------------+-----------+
| get_company_full_signatory_authority    | All signature holders         | English   | 
+-----------------------------------------+-------------------------------+-----------+


Installation
############

.. code-block:: python

   pip install -U willowlabs
	
Example usage
#############

.. code-block:: python

   from willowlabs.company_information.client import CompanyInformationClient
   client = CompanyInformationClient("client_config.yaml")
   company_basic_results = client.get_basic_company_information(organisation_number)
   company_ownership_results = client.get_company_ownership(organisation_number, record_year)
	
	
Client Module
==================

.. automodule:: willowlabs.company_information.client
   :members:
   :special-members:
   :show-inheritance:


Versions
==================
0.4.0 (current)
############### 
Relased 16.04.2020.

Change in import structure.

0.3.0
#####  
Relased 15.04.2020.

Bugg fixes.

0.2.0
##### 
Relased 04.04.2020.

First beta version: Basic funcunality.


Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
