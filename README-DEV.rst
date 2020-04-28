Willow Labs dev setup
========================

Using `pre-commit`_ to add git commit and push hooks. Available hooks:

* Black - formating the code [commit]
* Flake8 - check pep8 compliance [commit]
* Bandit - Security checks [commit]
* mypy - check typing - disabled
* pytests - unit and integration tests [push]



Installation
-------------

* add path to config file for service account to config-dev.yaml
* inatall needed packages using pip and install pre-commit to .git folder by running:

.. code-block:: python

    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    # Pre commit hooks to git
    #pre-commit install
    pre-commit install -t pre-push


.. _pre-commit: https://pre-commit.com/