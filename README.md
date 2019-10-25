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

Create a file, `config.json`, and specify its location with the appropriate command-line flag.

#### Setup ####

Example `config.json`:
```
{
    "api_key": "API_KEY",
    "application_key": "APP_KEY"
}
```

All of the following keys are required:
* `api_key`: API key from Ambient Weather (e.g. `asdasd`)
* `application_key`: Application key from Ambient Weather (e.g. `asdasd`)
