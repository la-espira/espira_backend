# Espira Backend

It's a backend API for the project [Espira](https://github.com/la-espira/espira)

# Documentation

Main documentation is here: [Espira - README.md](https://github.com/la-espira/espira/blob/dev/README.md)

# ADR

[ADR.md](doc/ADR.md)

# Work Log

[Work_log.md](doc/Work_log.md)

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

