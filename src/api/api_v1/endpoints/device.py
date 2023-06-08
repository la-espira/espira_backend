from typing import List

from fastapi import APIRouter

from schemas.device import (
    DeviceShow,
)

router = APIRouter()


@router.get("/", response_model=List[DeviceShow])
def read_devices(
    skip: int = 0,
    limit: int = 100,
):
    """
    Retrieve devices
    """
    # users = utils.get_docs(bucket, doc_type, doc_model, skip, limit)
    # utils.get_docs:
    #   doc_results = get_doc_results_by_type(bucket, doc_type, skip, limit)
    #     crud.utils.get_doc_results_by_type:
    #       q = N1QLQuery(query_str, bucket, type, limit, skip)
    ...
