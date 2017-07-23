#!/usr/bin/env
#import provneo4j.api
import babeltrace
import sys
import datetime
from prov.dot import prov_to_dot
from prov.model import ProvDocument, Namespace, Literal, PROV, Identifier

#provneo4j_api = provneo4j.api.Api(base_url="http://localhost:7474/db/data", username="neo4j", password="neo4j")

# get the trace path from the first command line argument
trace_path = sys.argv[1]
trace_collection = babeltrace.TraceCollection()
trace_collection.add_trace(trace_path, 'ctf')
#Outputs the event keys of each trace that was recorded.
def ctfToProv():
    d1 = ProvDocument()
    dummy = ProvDocument()
    ex = Namespace('ex', 'http://example/')  # namespaces do not need to be explicitly added to a document
    data = ['timestamp', 'humidity', 'temperature', 'sensor_info', 'device_info']
    counter = 0
    relationships = []
    for event in trace_collection.events:
        dataset = {'ex:'+data[0]:event[data[0]], 'ex:'+data[1]:event[data[1]], 'ex:'+data[2]:event[data[2]]}
        e1 = d1.entity(ex['dataset'+str(counter)],dataset)
        sensor_agent = d1.agent('ex:'+event['sensor_info'])
        device_agent = d1.agent('ex:'+event['device_info'])
        activity = d1.activity('ex:read')
        d1.wasGeneratedBy(e1, activity)
        # strings used to detect if the relationship already exists in the d1 document
        association_relationship = str(dummy.wasAssociatedWith(activity, sensor_agent))
        used_relationship = str(dummy.used(device_agent, sensor_agent))
        #check if the association already esists
        if association_relationship not in relationships:
            d1.wasAssociatedWith(activity,sensor_agent)
            relationships.append(association_relationship)
        if used_relationship not in relationships:
            d1.used(device_agent, sensor_agent)
            relationships.append(used_relationship)
        counter+=1
    return d1
prov_document = ctfToProv()
prov_document = prov_document.unified()
prov_document.serialize('output.json')
#prov_document.serialize('output.json')
#provneo4j_api.document.create(prov_document, name="Primer Example")
