# datasette-knightlab-timeline

[![PyPI](https://img.shields.io/pypi/v/datasette-knightlab-timeline.svg)](https://pypi.org/project/datasette-knightlab-timeline/)
[![Changelog](https://img.shields.io/github/v/release/ashanan/datasette-knightlab-timeline?include_prereleases&label=changelog)](https://github.com/ashanan/datasette-knightlab-timeline/releases)
[![Tests](https://github.com/ashanan/datasette-knightlab-timeline/workflows/Test/badge.svg)](https://github.com/ashanan/datasette-knightlab-timeline/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/ashanan/datasette-knightlab-timeline/blob/main/LICENSE)

A Datasette plugin to create timelines using the TimelineJS library.

## Installation

Install this plugin in the same environment as Datasette.

    datasette install datasette-knightlab-timeline

## Usage

Add a `datasette-knightlab-timeline` object to the metadata plugins section.

```json
{
    "title": "This is the top-level title in metadata.json",
    "plugins": {
		"datasette-knightlab-timeline": {
			"databases": [{
				"database": "database_one",
				"query": "SELECT  date_measured as start_date FROM measurement_event WHERE date_measured > (SELECT DATETIME('now', '-30 day'))",
				"text": "This text will prepend the value of the column whose name is in 'text_column'",
				"text_column": "Average"
			}, {
				"database": "inaturalist",
				"query": "SELECT created_at as start_date, species_guess FROM observations WHERE created_at > (SELECT DATETIME('now', '-30 day'))",
				"text": "Nature observation!  Observed: ",
				"text_column": "species_guess"
			}]
		}
    }
}


```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

    cd datasette-knightlab-timeline
    python3 -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
