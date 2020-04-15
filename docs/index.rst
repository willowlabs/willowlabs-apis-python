

Welcome to Willow Labs Python API's documentation!
==================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

This library conatins APIs to connect to Willow Labs services.


Installation:

.. code-block:: python

   pip install -U willowlabs
	
Example usage:

.. code-block:: python

   import willowlabs as wl
   client = wl.company_information.client.CompanyInformationClient("client_config.yaml")
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
0.2.0. (current). Basic funcunality.


Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
