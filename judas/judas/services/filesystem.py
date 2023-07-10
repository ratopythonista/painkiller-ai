from uuid import uuid4
from io import BytesIO

from minio import Minio
from urllib3.response import HTTPResponse
from loguru import logger

from jonas.config import FILESYSTEM_ACCESS_KEY, FILESYSTEM_SECRET_KEY, FILESYSTEM_HOST, FILESYSTEM_BUCKET

class FileSystem:
    def __init__(self) -> None:
        self.client = Minio(
            FILESYSTEM_HOST,
            access_key=FILESYSTEM_ACCESS_KEY,
            secret_key=FILESYSTEM_SECRET_KEY,
            secure=False
        )

        found = self.client.bucket_exists(FILESYSTEM_BUCKET)
        if not found:
            self.client.make_bucket(FILESYSTEM_BUCKET)

    def insert(self, file: bytes, metadata: dict):
        object_id = str(uuid4())
        self.client.put_object(FILESYSTEM_BUCKET, object_id, BytesIO(file), len(file), metadata=metadata)
        return object_id
    
    def get_model(self, object_id: str):
        response: HTTPResponse = self.client.get_object(FILESYSTEM_BUCKET, object_id)
        object_data = response.read()
        response.close()
        response.release_conn()
        return object_data

    def get_recall(self, object_id: str):
        response: HTTPResponse = self.client.get_object(FILESYSTEM_BUCKET, object_id)
        recall = response.getheader("x-amz-meta-recall")
        response.close()
        response.release_conn()
        return recall