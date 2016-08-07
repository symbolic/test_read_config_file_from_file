# -*- coding: utf-8 -*-
from xml.dom.minidom import parse, parseString

def getText(nodelist):
	rc = ""
	
	for node in nodelist:
		if node.nodeType == node.TEXT_NODE:
			rc = rc + node.data
			
	return rc
	
def main():
	dom1 = parse('../conf/db_config.xml')
	config_element = dom1.getElementsByTagName('config')[0]
	servers = config_element.getElementsByTagName('server')
	
	for server in servers:
		print type(server)
		print getText(server.childNodes)
		print type(getText(server.childNodes))
		temp = getText(server.childNodes)
		print 'temp: ' + temp
		print type(temp)
		print '*'*30
	
if __name__ == '__main__':
	main()