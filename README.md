# ambient-weather-archiver
Store Ambient Weather data to file-system

### Description ###

This program is a simple Ambient Weather archiver in Python.

### Installation ###

Clone the repository:

```
git clone https://github.com/johnbenclark/ambient-weather-archiver.git
```

### Configuration ###

Create a file, `config.json`, and specify its location with the `--config` command-line flag.

The default behavior is to use the current date, but a different date can be specified using the `--datetime` command-line flag. 

#### Setup ####

Example `config.json`:
```
{
    "api_key": "API_KEY",
    "application_key": "APP_KEY",
    "device_mac_address": "ff:ff:ff:ff:ff:ff",
    "archive_dir": "/tmp/",
    "datetime_fmt": "%Y%m%d_%H%M%S"
}
```

All of the following keys are required:
* `api_key`: API key from Ambient Weather.
* `application_key`: Application key from Ambient Weather.
* `device_mac_address`: Device MAC address from Ambient Weather.
* `archive_dir`: Folder where Ambient Weather data will be stored.
* `datetime_fmt`: Format for date/time. Refer to python3's time.strftime for format directives.
