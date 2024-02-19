from fastapi import APIRouter, HTTPException, Request
from datetime import datetime

from marshmallow import ValidationError
from validation.request import SourceCreateRequest

from validation.responses import GeneralResponse
from service.connection_service import ConnectionService

SOURCE = "/api/source"


class SourceRouter:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route(SOURCE + "/v1/create", self.source_create, methods=["POST"])
        # self.router.add_api_route(SOURCE + "/v1/schema", self.source_create, methods=["POST"])

    async def source_create(self, request: SourceCreateRequest):
        try:
            self.connection_service = ConnectionService(request.sourceId, request.credentials)
            result = self.connection_service.create_connection()
            response: GeneralResponse = GeneralResponse(success=True, data=result)
            if response.success:
                return response.data
            else:
                raise HTTPException(status_code=406, detail=response.message)
        except ValidationError as exc:
            raise HTTPException(status_code=422, detail=str(exc))