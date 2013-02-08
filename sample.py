#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import dfa_report

def get_dfa_report(profileId, reportId):
	service = dfa_report.initialize_service()
	myreportid = get_dfa_report_id(service, profileId, reportId)

	dfafiles = service.files()
	dfalistfiles = dfafiles.list(profileId=profileId)
	dfalistfilesexecuter = dfalistfiles.execute()

	for a in dfalistfilesexecuter.get('items'):
		print a

def get_dfa_report_id(service, profileId, reportId):
	dfareports = service.reports()
	dfareport_runner = dfareports.run(profileId=profileId, reportId=reportId)
	dfareport_executer = dfareport_runner.execute()


	myreportid = dfareport_executer.get("id")
	return myreportid


def main():
	if len(sys.argv) == 3:
		get_dfa_report(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    try:
    	main()
    except Exception, e:
        print e


