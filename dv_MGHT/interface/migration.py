from __future__ import annotations

import copy
import typing
from collections.abc import Callable

Migrations = typing.Sequence[Callable[[dict], dict] | None]

def get_version(migrations: Migrations) -> int:
    return len(migrations) + 1

def apply_migrations(
    data: dict,
    migrations: Migrations,
    *,
    copy_before_migrating: bool = False,
    version_name: str = "version"
) -> dict:
    schema_version = data.get("schema_version", 1)
    version = get_version(migrations)

    while schema_version < version:
        if copy_before_migrating:
            data = copy.deepcopy(data)
            copy_before_migrating = False

        migration = migrations[schema_version - 1]
        if migration == None:
            raise UnsupportedVersion(
                "Requested migration from {} {}, but it is no longer supported.".format(version_name, schema_version),
                "You can try using an older dv_MGHT version."
            )
        data = migration(data)
        schema_version += 1
    return data