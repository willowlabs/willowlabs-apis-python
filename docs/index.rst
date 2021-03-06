.. image:: https://i.imgur.com/J2CGGYd.jpg
    :width: 1200px
    :align: center
    :height: 600px
    :alt: Willow Labs logo

Willow Labs Python API's documentation
==================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Willow labs APIs offers services to get information regarding companies and related entities. The main companents are:

* Information about the owners of a company. This service provides owners at all levels, meaning it recursively goes through the ownership structure until a private owner is established.
* Basic company information as address, industry, number of employees and more.
* Signature rights and prokura holders for a company.
* Roles connected to the company, for example CEO, board members, accountant.



+-----------------------------------------+-------------------------------------------------------+-----------+-----------------------------------+
| Service name                            | Descritpion                                           | Language  | English version                   |
+=========================================+=======================================================+===========+===================================+
| get_basic_company_information           | Basic information.                                    |  English  |                                   |
+-----------------------------------------+-------------------------------------------------------+-----------+-----------------------------------+
| get_company_ownership                   | Get the full ownership structure.                     | English   |                                   |
+-----------------------------------------+-------------------------------------------------------+-----------+-----------------------------------+
| get_company_power_of_attorney           | Get everyone with power of attorney.                  | English   |                                   |
+-----------------------------------------+-------------------------------------------------------+-----------+-----------------------------------+
| \*get_company_prokura                   | Get everyone with prokura rights (power of attorney). | Norwegian | get_company_power_of_attorney     |
+-----------------------------------------+-------------------------------------------------------+-----------+-----------------------------------+
| get_company_full_signatory_authority    | All signature holders.                                | English   |                                   |
+-----------------------------------------+-------------------------------------------------------+-----------+-----------------------------------+
| \*get_company_signatur                  | Get all signatur (signature) holders.                 | Norwegian | get_company_signatory_information |
+-----------------------------------------+-------------------------------------------------------+-----------+-----------------------------------+
| get_company_signatory_information       | Get the authority holder.                             | English   |                                   |
+-----------------------------------------+-------------------------------------------------------+-----------+-----------------------------------+
| get_company_roles                       | Get all roles connect to a company.                   | English   |                                   |
+-----------------------------------------+-------------------------------------------------------+-----------+-----------------------------------+

\* The function is a Norwegian version of an english function - see english version column for information.

Installation
-------------

.. code-block:: python

   pip install -U willowlabs

Example usage
-------------

.. code-block:: python

   from willowlabs.company_information.client import CompanyInformationClient
   client = CompanyInformationClient("client_config.yaml")
   company_basic_results = client.get_basic_company_information(organisation_number)
   company_ownership_results = client.get_company_ownership(organisation_number, record_year)


User self testing suite
-----------------------
org_list is a user supplied list of organisation number, run without parameter
org_list to use build in list of organisations.


.. code-block:: python

    from willowlabs import test_report as tr
    org_list = [1,...,1000]
    tr.run_report(org_list=org_list)

Modules
-------------

Client Module
==================

.. automodule:: willowlabs.company_information.client
   :members:
   :special-members:
   :show-inheritance:


Versions
==========
Using `Semantic Versioning 2.0.0`_.

.. _Semantic Versioning 2.0.0: https://semver.org/


[0.5.0] - 16.04.2020
------------------------------

Added
^^^^^
* Readme file documentation.


[0.4.0] - 16.04.2020
------------------------------

Added
^^^^^
* Change in import structure.

[0.3.0] - 15.04.2020
--------------------

Added
^^^^^
* New function to get roller

Bugg fix
^^^^^^^^
* Removed __init__ import

[0.2.0] - 04.04.2020
--------------------

First beta version: Basic functionality.


Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
