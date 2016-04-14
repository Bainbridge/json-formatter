# json-formatter
-----------------
Rewrites non-human readable json files to be readable.  Primary reason for this is to compare lines of one json to another

## Usage
**Needs** to run from the command line, you pass an argument "-f" preceding the name of the json file you're trying to convert.  It will spit your file back out as CleanJSON-formatted.json.

**Formatting**
`$ python format.py -f 'GrossJSON.json'`

**Directory Cleaning**
If you have a ton of formatted JSON files and want them removed, just use the -c argument!
`$ python format.py -c`
