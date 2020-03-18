import subprocess
import setuptools


def install_package():
    code = subprocess.call("pip install --upgrade pip setuptools wheel && pip install -r requirements.txt", shell=True)
    if code:
        print("Error installing the requirements for the package. Installation failed.")
        return 1

    code = subprocess.call("python -m grpc_tools.protoc --proto_path=protos/ --python_out=. --grpc_python_out=. "
                           "protos/willowlabs/service_grpc/company_information/company_information_service.proto",
                           shell=True)
    if code:
        print("Error generating the grpc python files. Installation failed.")
        return 1

    with open("README.md", "r") as fh:
        long_description = fh.read()

    setuptools.setup(
        name="willowlabs",
        version="1.0.0",
        author="Willow Labs AS",
        description="A Python package for accessing the Willow Labs APIs",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/willowlabs/willowlabs-apis-python",
        packages=setuptools.find_packages(),
        classifiers=[
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.7',
    )
    return 0


install_package()
