#*_*coding:utf-8*_*

import xml.dom.minidom as xmlDoc
import os
import gl
import sys



class cREPORTXML(object):
    def __init__(self):
        self.__struct = self.createReportNode()

    #创建report节点
    def createReportNode(self):
        try:
            xmlD = xmlDoc.Document()

            #xml样式
            xlstNode = xmlD.createProcessingInstruction("xml-stylesheet","href=\"LOG.XSLT\" type=\"text/xsl\"")
            xmlD.appendChild(xlstNode)

            report = xmlD.createElement('REPORT')
            xmlD.appendChild(report)

            overStatus = xmlD.createElement('OVER_STATUS')
            overStatus.appendChild(xmlD.createTextNode('PASSED'))
            report.appendChild(overStatus)



            returnResult = []
            returnResult.append(xmlD)
            returnResult.append(report)
            returnResult.append(overStatus)

        except Exception,ex:
            return ex.message
        return returnResult

    def writeOverStatus(self,overStatus = 'PASSED'):
        self.__struct[2]._get_childNodes().item(0).nodeValue = overStatus


    def writeReport(self,execTime='',stepResult='',comName='',stepDisc=''):
        #reportNodeList = self.createReportNode()

        entry = self.createLogEntry(self.__struct[0],execTime,stepResult,comName,stepDisc)
        self.__struct[1].appendChild(entry)
        self.writeXml(self.__struct[0],gl.reporterPath+'reportxml.xml')
        #self.writeXml(self.__struct[0],gl.reporterPath+'reportxml_%s.xml'%(gl.curTimeStr))


 #-------------创建xml格式-有多个相同的节点，并且该节点下有4个名称相同的子节点----------------
    def createLogEntry(self,docObj,executeTime,stepResult,componentName,stepDiscription):
        entry = docObj.createElement("LOG_ENTRY")

        status = docObj.createElement("STATUS")
        nodeExecuteTime = docObj.createElement("EXECUTION_TIME")
        nodeStepResult = docObj.createElement("STEP_RESULT")
        nodeComponentName = docObj.createElement("COMPONENT_NAME")
        nodeStepDiscription = docObj.createElement("STEP_DESCRIPTION")

        status.appendChild(docObj.createTextNode(stepResult))
        nodeExecuteTime.appendChild(docObj.createTextNode(executeTime))
        nodeStepResult.appendChild(docObj.createTextNode(stepResult))
        nodeComponentName.appendChild(docObj.createTextNode(componentName))
        nodeStepDiscription.appendChild(docObj.createTextNode(stepDiscription))

        entry.appendChild(status)
        entry.appendChild(nodeExecuteTime)
        entry.appendChild(nodeStepResult)
        entry.appendChild(nodeComponentName)
        entry.appendChild(nodeStepDiscription)
        return entry


    #参数，xml对象，准备存储xml文件路径，文件模式：读 and 写 (r and w)
    def writeXml(self,xmlDoc,xmlPath):
        f = open(xmlPath,"w")
        xmlDoc.writexml(f,indent='\t', addindent='\t', newl='\n', encoding="utf-8")
        f.close()




if __name__=='__main__':
    reportx =cREPORTXML()
    print  reportx.writeReport('20170602','PASSED','1-SETTEXT','AUTOMATION TEST')
    print  reportx.writeReport('20170606','FIELD','2-SETTEXT','AUTOMATION TEST')