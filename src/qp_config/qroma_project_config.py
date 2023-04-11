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
    site_path: str


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
    publication_filepath: str


@dataclass
class ZippedDirItem:
    source_dir: str
    publication_zip_file: str


@dataclass
class GeneratedFileItem:
    publication_filepath: str
    template_str: str


@dataclass
class BundleVersionPublication:
    firmware_file_replications: list[ReplicatedFirmwareFilesItem]
    zipped_dirs: list[ZippedDirItem]
    generated_files: list[GeneratedFileItem]


@dataclass
class BundleStage:
    bundle_static_dir: str
    bundle_version_content_root_dir_template: str
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
class QromaProjectDict:
    name: str
    version: str
    firmware: QromaProjectFirmware
    stages: QromaProjectStages


@dataclass
class QromaRoot:
    project: QromaProjectDict


@dataclass
# class QromaProjectConfigDict:
class QromaProjectConfig:
    qroma: QromaRoot
    blah: Optional[str] = "notset"
    # number: StrictInt


def create_project_config(qroma_config_file_dict: dict) -> QromaProjectConfig:
    project_config = QromaProjectConfig(**qroma_config_file_dict)
    return project_config
