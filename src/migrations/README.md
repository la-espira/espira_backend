# Espira Backend

# API

```text
/api
  v1
    data
    device/devices
    device/devices/{id}
    device/devices/{id}/parameters
    device/device_models
    device/device_profiles
    device/device_types
    parameters
    vendors
```

# TODO

- [ ] Rename API URLs
- [ ] Add UUID to tables
- [ ] Redesign device_link
- [ ] Implement API for data load to mongo

# alembic

To generate revision, run in project root folder:

```shell
alembic revision --autogenerate -m "Create device tables"
```