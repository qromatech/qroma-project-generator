from enum import Enum

from pydantic import BaseModel


class QromaSiteManifestType(str, Enum):
    publishedQromaFirmwareBuild = "publishedQromaFirmwareBuild"


class QromaSiteManifestDetails(BaseModel):
    pass


class QromaSiteProtoFileDetails(BaseModel):
    protoPath: str


class QromaEsp32LoaderManifest(BaseModel):
    name: str
    manifestPath: str


class QromaFirmwareBuildManifest(BaseModel):
    project_id: str
    version: str

    qromaEsp32LoaderManifests: list[QromaEsp32LoaderManifest]


class QromaSiteManifest(BaseModel):
    type: QromaSiteManifestType
    path: str
    details: QromaSiteManifestDetails


class QromaSiteManifests(BaseModel):
    manifests: list[QromaSiteManifest]
