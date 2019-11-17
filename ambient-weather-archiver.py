#!/usr/bin/env python3

#
# ambient-weather--archiver
# Author: Ben Blasdell
# Email: ben@fiter.org
# GitHub project URL: https://github.com/johnbenclark/ambient-weather-archiver
#
# Version: 0.1.0
#

# Libraries
import os, time, json, argparse, urllib.request

# Parse command line arguments
parser = argparse.ArgumentParser(
	description='Ambient Weather archiver'
)
parser.add_argument(
	'--config',
	dest='config',
	required=True,
	help='path to JSON configuraiton file'
)
parser.add_argument(
	'--datetime',
	dest='datetime',
	required=False,
	help='download date/time specified in "YYYYMMDDHHmmss" format'
)
args = parser.parse_args()

# Check command line arguments
if not os.path.isfile(args.config):
	print("Configuration file missing.")
	exit()

# Load configuration
with open(args.config, "r") as f:
	config = json.load(f)
	if not 'api_key' in config:
		print("Configuration file missing API key.")
		exit()
	if not 'application_key' in config:
		print("Configuration file missing application key.")
		exit()
	if not 'device_mac_address' in config:
		print("Configuration file missing device mac address.")
		exit()
	if not 'archive_dir' in config:
		print("Configuration file missing archive dir.")
		exit()
	if not 'datetime_fmt' in config:
		print("Configuration file missing date/time format.")
		exit()


API_KEY = config['api_key']
APP_KEY = config['application_key']
DEV_MAC = config['device_mac_address']
ARCHIVE = config['archive_dir']
DATETIME_FMT = config['datetime_fmt']

# Calculate download date
download_date = time.localtime()
if args.datetime is not None:
	download_date = time.strptime(args.datetime, "%Y%m%d%H%M%S")
def round_to_fmt(date, fmt):
	return time.strptime(time.strftime(fmt, date), fmt)
download_date = round_to_fmt(download_date, DATETIME_FMT)

# Convert download date to end date
end_date = str(int(time.mktime(download_date)) * 1000)
end_date_str = time.strftime(DATETIME_FMT, download_date)

# Download from Ambient Weather
url = f'https://api.ambientweather.net/v1/devices/{DEV_MAC}' + \
      f'?apiKey={API_KEY}&applicationKey={APP_KEY}&endDate={end_date}&limit=288'
print(url)
resp = urllib.request.urlopen(url).read().decode('utf-8')
fp = open(f'{ARCHIVE}/{end_date_str}', 'w')
fp.write(resp)
fp.close()
