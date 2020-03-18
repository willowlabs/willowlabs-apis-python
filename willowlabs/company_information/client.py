import os
import json
import grpc
from time import time
from datetime import date, datetime
from willowlabs.tools import tools
from willowlabs.service_grpc.company_information import company_information_service_pb2 as pb2, company_information_service_pb2_grpc as pb2_grpc
from typing import Any, Optional, Union


def date_to_pb2_date(d: Union[date, datetime, None]) -> Optional[pb2.Date]:
    if d is None:
        return None
    return pb2.Date(year=d.year, month=d.month, day=d.day)


class CompanyInformationClient:
    def __init__(self, configuration_path: str, **kwargs: Any):
        self.configuration_path = configuration_path
        self.configuration = None
        self.service_type = kwargs.get("service_type", "production")
        self.credentials_info = None
        self.host = None
        self.issuer = None
        self.audiences = None
        self.jwt = None
        self.jwt_expires = None
        self.api_key = None
        self.timeout = kwargs.get("timeout", 60)        # Seconds
        self.scopes = ["https://www.googleapis.com/auth/cloud-platform"]

    def load_configuration(self):
        self.configuration = tools.load_client_configuration(self.configuration_path)
        self.host = self.configuration["service"][self.service_type]["host"]
        self.issuer = self.configuration["authentication"]["issuer"]
        self.audiences = self.configuration["authentication"]["audiences"]
        self.api_key = self.configuration["service"][self.service_type]["api_key"]

    def load_credentials(self):
        if self.configuration is None:
            self.load_configuration()
        configuration = self.configuration["service"][self.service_type]
        path = configuration["service_account_credentials"]
        if path.endswith(".json") and os.path.exists(path):
            with open(path, "r") as fp:
                self.credentials_info = json.load(fp)
        else:
            raise FileNotFoundError(f"Unable to find credentials in path {path}.")

    def get_json_web_token(self):
        if self.credentials_info is None:
            self.load_credentials()
        token, expires = tools.generate_jwt_token_from_impersonated_account(self.credentials_info, self.audiences,
                                                                            self.issuer)
        self.jwt = token
        self.jwt_expires = expires

    def get_company_ownership(self, organisation_number: int, record_year: int, depth: int = 25, cutoff: float = 1.0,
                              top: int = 0) -> pb2.OwnershipResponse:
        if self.jwt is None or self.jwt_expires is None or self.jwt_expires < time():
            self.get_json_web_token()

        with grpc.secure_channel(self.host, grpc.ssl_channel_credentials()) as channel:
            stub = pb2_grpc.CompanyInformationStub(channel)
            metadata = [("authorization", f"Bearer {self.jwt}"), ("x-api-key", self.api_key)]
            request = pb2.OwnershipRequest(organisation_number=organisation_number, record_year=record_year,
                                           depth=depth, cutoff=cutoff, top=top)
            ownership_information = stub.get_company_ownership(request, self.timeout, metadata=metadata)
        return ownership_information

    def get_company_roles(self, organisation_number: int, query_date: date) -> pb2.RoleResponse:
        if self.jwt is None or self.jwt_expires is None or self.jwt_expires < time():
            self.get_json_web_token()
        with grpc.secure_channel(self.host, grpc.ssl_channel_credentials()) as channel:
            stub = pb2_grpc.CompanyInformationStub(channel)
            metadata = [("authorization", f"Bearer {self.jwt}"), ("x-api-key", self.api_key)]
            request = pb2.RoleRequest(organisation_number=organisation_number,
                                      query_date=date_to_pb2_date(query_date))
            roles = stub.get_company_roles(request, self.timeout, metadata=metadata)
        return roles

    def get_basic_company_information(self, organisation_number: int,
                                      query_date: Optional[date] = None) -> pb2.BasicCompanyInformationResponse:
        if self.jwt is None or self.jwt_expires is None or self.jwt_expires < time():
            self.get_json_web_token()
        with grpc.secure_channel(self.host, grpc.ssl_channel_credentials()) as channel:
            stub = pb2_grpc.CompanyInformationStub(channel)
            metadata = [("authorization", f"Bearer {self.jwt}"), ("x-api-key", self.api_key)]
            request = pb2.BasicCompanyInformationRequest(organisation_number=organisation_number,
                                                         query_date=date_to_pb2_date(query_date))
            results = stub.get_basic_company_information(request, self.timeout, metadata=metadata)
        return results
