---
title: Milvus - Vector Store | liteLLM
url: https://docs.litellm.ai/docs/providers/milvus_vector_stores
source: sitemap
fetched_at: 2026-01-21T19:49:40.953225745-03:00
rendered_js: false
word_count: 0
summary: This document provides a Python implementation of a client for interacting with the Milvus REST API v2, facilitating collection management, data ingestion, and vector search operations.
tags:
    - milvus-vector-db
    - rest-api-v2
    - python-client
    - vector-search
    - api-wrapper
    - data-management
category: api
---

```
"""
Simple Milvus REST API v2 Client
Based on: https://milvus.io/api-reference/restful/v2.6.x/
"""

import requests
from typing import List, Dict, Any, Optional


classDataType:
"""Milvus data types"""

    INT64 ="Int64"
    FLOAT_VECTOR ="FloatVector"
    VARCHAR ="VarChar"
    BOOL ="Bool"
    FLOAT ="Float"


classCollectionSchema:
"""Collection schema builder"""

def__init__(self):
        self.fields =[]

defadd_field(
        self,
        field_name:str,
        data_type:str,
        is_primary:bool=False,
        dim: Optional[int]=None,
        description:str="",
):
"""Add a field to the schema"""
        field ={
"fieldName": field_name,
"dataType": data_type,
"isPrimary": is_primary,
"description": description,
}
if data_type == DataType.FLOAT_VECTOR and dim:
            field["elementTypeParams"]={"dim":str(dim)}
        self.fields.append(field)
return self

defto_dict(self):
"""Convert schema to dict for API"""
return{"fields": self.fields}


classIndexParams:
"""Index parameters builder"""

def__init__(self):
        self.indexes =[]

defadd_index(
        self, field_name:str, metric_type:str="L2", index_name: Optional[str]=None
):
"""Add an index"""
        index ={
"fieldName": field_name,
"indexName": index_name orf"{field_name}_index",
"metricType": metric_type,
}
        self.indexes.append(index)
return self

defto_list(self):
"""Convert to list for API"""
return self.indexes


classMilvusRESTClient:
"""
    Simple Milvus REST API v2 Client

    Reference: https://milvus.io/api-reference/restful/v2.6.x/
    """

def__init__(self, uri:str, token:str, db_name:str="default"):
"""
        Initialize Milvus REST client

        Args:
            uri: Milvus server URI (e.g., http://localhost:19530)
            token: Authentication token
            db_name: Database name
        """
        self.base_url = uri.rstrip("/")
        self.token = token
        self.db_name = db_name
        self.headers ={
"Authorization":f"Bearer {token}",
"Content-Type":"application/json",
}

def_make_request(self, endpoint:str, data: Dict[str, Any])-> Dict[str, Any]:
"""Make a POST request to Milvus API"""
        url =f"{self.base_url}{endpoint}"

# Add dbName if not already in data and not default
if"dbName"notin data and self.db_name !="default":
            data["dbName"]= self.db_name

try:
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()
except requests.exceptions.HTTPError as e:
print(f"e.response.text: {e.response.content}")
raise e

        result = response.json()

# Check for API errors
if result.get("code")!=0:
raise Exception(
f"Milvus API Error: {result.get('message','Unknown error')}"
)

return result

defhas_collection(self, collection_name:str)->bool:
"""
        Check if a collection exists

        Reference: https://milvus.io/api-reference/restful/v2.6.x/v2/Collection%20(v2)/Has.md
        """
try:
            result = self._make_request(
"/v2/vectordb/collections/has",{"collectionName": collection_name}
)
return result.get("data",{}).get("has",False)
except Exception:
returnFalse

defdrop_collection(self, collection_name:str):
"""
        Drop a collection

        Reference: https://milvus.io/api-reference/restful/v2.6.x/v2/Collection%20(v2)/Drop.md
        """
return self._make_request(
"/v2/vectordb/collections/drop",{"collectionName": collection_name}
)

defcreate_schema(self)-> CollectionSchema:
"""Create a new collection schema"""
return CollectionSchema()

defprepare_index_params(self)-> IndexParams:
"""Create index parameters"""
return IndexParams()

defcreate_collection(
        self,
        collection_name:str,
        schema: CollectionSchema,
        index_params: Optional[IndexParams]=None,
):
"""
        Create a collection

        Reference: https://milvus.io/api-reference/restful/v2.6.x/v2/Collection%20(v2)/Create.md
        """
        data ={"collectionName": collection_name,"schema": schema.to_dict()}

if index_params:
            data["indexParams"]= index_params.to_list()

return self._make_request("/v2/vectordb/collections/create", data)

defdescribe_collection(self, collection_name:str)-> Dict[str, Any]:
"""
        Describe a collection

        Reference: https://milvus.io/api-reference/restful/v2.6.x/v2/Collection%20(v2)/Describe.md
        """
        result = self._make_request(
"/v2/vectordb/collections/describe",{"collectionName": collection_name}
)
return result.get("data",{})

definsert(
        self,
        collection_name:str,
        data: List[Dict[str, Any]],
        partition_name: Optional[str]=None,
):
"""
        Insert data into a collection

        Reference: https://milvus.io/api-reference/restful/v2.6.x/v2/Vector%20(v2)/Insert.md
        """
        payload ={"collectionName": collection_name,"data": data}

if partition_name:
            payload["partitionName"]= partition_name

        result = self._make_request("/v2/vectordb/entities/insert", payload)
return result.get("data",{})

defflush(self, collection_name:str):
"""
        Flush collection data to storage

        Reference: https://milvus.io/api-reference/restful/v2.6.x/v2/Collection%20(v2)/Flush.md
        """
return self._make_request(
"/v2/vectordb/collections/flush",{"collectionName": collection_name}
)

defsearch(
        self,
        collection_name:str,
        data: List[List[float]],
        anns_field:str,
        limit:int=10,
        search_params: Optional[Dict[str, Any]]=None,
        output_fields: Optional[List[str]]=None,
)-> List[List[Dict]]:
"""
        Search for vectors

        Reference: https://milvus.io/api-reference/restful/v2.6.x/v2/Vector%20(v2)/Search.md
        """
        payload ={
"collectionName": collection_name,
"data": data,
"annsField": anns_field,
"limit": limit,
}

if search_params:
            payload["searchParams"]= search_params

if output_fields:
            payload["outputFields"]= output_fields

        result = self._make_request("/v2/vectordb/entities/search", payload)
return result.get("data",[])
```