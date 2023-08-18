from typing import List, Optional

from pydantic import StrictInt
from pydantic.dataclasses import dataclass

from qroma_enums import ProtobufCompiler, FirmwareFramework


@dataclass
class ProtobufNanoPbReplicationStage:
    dirs: list[str]


@dataclass
class ProtobufPythonReplicationStage:
    dirs: list[str]


@dataclass
class ProtobufTypescriptReplicationStage:
    dirs: list[str]


@dataclass
class ProtobufDartReplicationStage:
    dirs: list[str]


@dataclass
class ProtobufReplicationStage:
    nanopb: ProtobufNanoPbReplicationStage
    python: ProtobufPythonReplicationStage
    typescript: ProtobufTypescriptReplicationStage
    dart: ProtobufDartReplicationStage


@dataclass
class ProtobufSource:
    source_path: str
    dest_path: str
    # site_path: str


@dataclass
class MakeProtobufStage:
    compilers: List[ProtobufCompiler]
    root_dir: str
    sources: list[ProtobufSource]
    replication: ProtobufReplicationStage


@dataclass
class MakeFirmwareStage:
    project_dirs: list[str]


@dataclass
class MakeAppsStage:
    project_dirs: list[str]


@dataclass
class ReplicatedFirmwareFilesItem:
    source_filepath: str
    local_publication_filepath: str
    hosted_publication_filepath: str


@dataclass
class ZippedDirItem:
    source_dir: str
    local_publication_zip_file: str


@dataclass
class GeneratedFileItem:
    local_publication_filepath: str
    template_str: str
    hosted_publication_filepath: str


@dataclass
class BundleVersionPublication:
    firmware_file_replications: list[ReplicatedFirmwareFilesItem]
    zipped_dirs: list[ZippedDirItem]
    generated_files: list[GeneratedFileItem]


@dataclass
class BundleStage:
    local_bundle_static_dir: str
    local_bundle_static_qroma_dir: str
    local_bundle_version_content_root_dir: str

    hosted_qroma_bundle_root: str
    hosted_qroma_bundle_versions_root: str
    hosted_bundle_version_path: str

    publish_version: BundleVersionPublication


@dataclass
class MakeSitesStage:
    project_dirs: list[str]
    bundle: BundleStage


@dataclass
class QromaProjectSwStages:
    protobuf: MakeProtobufStage
    firmware: MakeFirmwareStage
    apps: MakeAppsStage
    sites: MakeSitesStage


@dataclass
class QromaProjectStages:
    sw: QromaProjectSwStages


@dataclass
class QromaProjectFirmware:
    platforms: List[FirmwareFramework]


@dataclass
class QromaProjectDirs:
    pb_root: str
    firmware_root: str
    app_root: str
    site_root: str
    

@dataclass
class QromaProjectDict:
    id: str
    name: str
    version: str
    dirs: QromaProjectDirs
    firmware: QromaProjectFirmware
    stages: QromaProjectStages


@dataclass
class QromaRoot:
    project: QromaProjectDict


@dataclass
class QromaProjectConfig:
    qroma: QromaRoot


def create_project_config(qroma_config_file_dict: dict) -> QromaProjectConfig:
    project_config = QromaProjectConfig(**qroma_config_file_dict)
    return project_config
