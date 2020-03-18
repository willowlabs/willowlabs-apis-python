#!/usr/bin/env bash

python -m grpc_tools.protoc --proto_path=protos/ --python_out=. --grpc_python_out=. protos/willowlabs/service_grpc/company_information/company_information_service.proto