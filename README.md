# raspberry_prov

## Getting started
This instruction will get the project up and running on your local machine. The folders contained in the raspberry_prov folder are described below:

* converter: Contains code that extracts events from ctf stream file located in `ctf/` and converts these events to PROV-DM format. Also contains code for storing provenance into neo4j database in `tester.py`.
* ctf: contains metadata and stream file from trace collection. *This folder and the files in it are generated by running a sample.*
* experiments: Data collected from experimental tests of the trace-to-provenance tools.
* platforms: barectf platforms.
* prov2neo4j: Contains code for storing provenance into neo4j database.
* samples: example applications instrumented with tracing.
* traces: Trace data collected.

## Prerequisite

In order to run the code here, you need to install the following software

* GCC (C- Compiler)
* barectf
* babeltrace 1.5
* python >= 2.7, python3
* A slew of python3 libraries:
  * PyYAML: `pip3 install PyYAML`
  * babeltrace python bindings: `python3-babeltrace`
  * PROV Python: `pip3 install prov`
  * ProvNeo4j: `pip install provneo4j`
  * pydot: `pip install pydot`
* Neo4j
* make


## Installing

* To compile the sample `temperature` program, use the command 'make' in `samples/temperature` and to clean the directory, usually before compiling a new version, use the command 'make clean'. The 'make' command generates the stream file contained in the ctf folder. This file contains events trace from the sample application. 

* To convert trace events contained in the stream file to human readable PROV-DM format, run the python3 script `ctf_to_prov.py` located in the `converter` folder, passing as argument the path to a directory containing the metadata file and 1 or more trace (stream) files. *Note: babeltrace will return an error if any other files are found.* This generates a json file `output.json` containing the provenance conversion.


* To store PROV-DM file in the neo4j database, run python script `tester.py` contained in the `converter` folder. This also produces a pdf file `output.pdf` containing the provenance representation.






