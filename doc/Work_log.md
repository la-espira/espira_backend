# Work log

---

# 2023.06.25 Device Profile

Added Create Device Profile.

# 2023.06.21 problem with initial insert

There's some problem with initial API for create model (for example).
Is it a problem with async session?

```shell
INFO:     127.0.0.1:49558 - "POST /api/v1/device/vendor/create/ HTTP/1.1" 400 Bad Request
DEBUG | 2023-06-22 00:18:22.721 | util | add_item_by_model:50 - Failed to add item: <db.models.device.DeviceVendor object at 0x7fc8a69a87c0>: IntegrityError: (sqlalchemy.dialects.postgresql.asyncpg.IntegrityError) <class 'asyncpg.exceptions.UniqueViolationError'>: duplicate key value violates unique constraint "t_device_vendor_pkey"
DETAIL:  Key (id)=(1) already exists.
[SQL: INSERT INTO t_device_vendor (name) VALUES ($1::VARCHAR) RETURNING t_device_vendor.id]
[parameters: ('Custom',)]
(Background on this error at: https://sqlalche.me/e/20/gkpj)
```

# 2023.06.19 async

Commited & pushed to feature/1.
Created branch feature/2 from feature/1.
Started refactoring for async.

# 2023.06.13 exceptions 
- [x] Try except for add_item_by_model
- [ ] Handling in create_device_type

# 2023.06.12 create
Added create operation. No constraint or exception handling.

# 2023.06.10 read
Added read operation in API /api/v1/device/all, /type, /vendor, /model, /device-profile.
Added alembic revision with sample data insertion.


# 2023.06.08 alembic
Fixed Create revision: imports changed.


# 2023.06.07 alembic
Deleted: revisions .py files, alembic_version table.
But failed to create new revision. 
