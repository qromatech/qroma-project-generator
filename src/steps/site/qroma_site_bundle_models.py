from enum import Enum

from pydantic import BaseModel


class QromaSiteManifestType(str, Enum):
    publishedQromaFirmwareBuild = "publishedQromaFirmwareBuild"


class QromaSiteManifestDetails(BaseModel):
    pass


class QromaSiteProtoFileDetails(BaseModel):
    protoPath: str


# class QromaSiteProtoDetails(BaseModel):
#     protofileDetails: list[QromaSiteProtoFileDetails]


class QromaEsp32LoaderManifest(BaseModel):
    name: str
    manifestPath: str


class QromaFirmwareBuildManifest(BaseModel):
    project_id: str
    version: str

    qromaEsp32LoaderManifests: list[QromaEsp32LoaderManifest]
    # protoDetails: QromaSiteProtoDetails


class QromaSiteManifest(BaseModel):
    type: QromaSiteManifestType
    path: str
    details: QromaSiteManifestDetails


class QromaSiteManifests(BaseModel):
    manifests: list[QromaSiteManifest]
