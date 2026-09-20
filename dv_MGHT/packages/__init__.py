from __future__ import annotations

from pathlib import Path

from dv_MGHT import get_package_base_path, get_local_data_path
from dv_MGHT.classes.package_classes import DVmghtPackage
from dv_MGHT.interface.json_tools import package_from_json

PACKAGE_BY_ID: dict[str, DVmghtPackage] = {}

def get_version(package: DVmghtPackage) -> list[ int ]:
    raw_version = "-".split(package.version.replace(".", "-"))
    new_version: list[int] = []
    for item in raw_version:
        if item.isnumeric():
            new_version.append(int(item))
        elif item[:-1].isnumeric():
            new_version.append(int(item[:-1]))
            new_version.append(ord(item[-1]))
        else:
            for i in item:
                new_version.append(ord(i))
    return new_version

def compare_versions(
    found_package: DVmghtPackage,
    existing_package:DVmghtPackage
) -> bool:
    found_v = get_version(found_package)
    exist_v = get_version(existing_package)

    minlen = min(len(found_v), len(exist_v))

    for i in range(minlen):
        if found_v[i] > exist_v[i]:
            return True

    if len(found_v) > len(exist_v):
        return True

    return False

def get_packages() -> None:
    package_paths_internal_raw = get_package_base_path().glob("*/manifest.json")
    package_paths_external_raw = get_local_data_path().glob("packages/*/manifest.json")
    package_paths = [
        Path(path).parent for path in [
            *package_paths_internal_raw,
            *package_paths_external_raw
        ] if Path(path).parent.parts[-1] != "example"
    ]

    output_packages: dict[str, DVmghtPackage] = {}
    for package_path in package_paths:
        this_package = package_from_json(package_path)
        if this_package.id in output_packages.keys():
            if compare_versions(this_package, output_packages[this_package.id]):
                output_packages[this_package.id] = this_package
        else:
            output_packages[this_package.id] = this_package
    
    list_order = [ item.name for item in output_packages.values() ]
    id_for_name = { k.name: v for v, k in output_packages.items() }
    list_order.sort()

    for item in list_order:
        this_id = id_for_name[item]
        PACKAGE_BY_ID[this_id] = output_packages[this_id]

get_packages()

PACKAGES: list[DVmghtPackage] = [ *PACKAGE_BY_ID.values() ]

