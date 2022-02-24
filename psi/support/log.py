from datetime import datetime
class logFile:
    def __init__(self, logPath, logType, logFormat):
        self.logPath = logPath
        self.logType = logType
        self.logFormat = logFormat
        #init the log file
        with open(logPath, 'a') as logFileWriterInit:
            logFileWriterInit.write('Start of log at '+str(datetime.now())+'. ['+logType+' '+logFormat+']')
            logFileWriterInit.write('\n')
    def log(self, logLevel, logMsg):
        logTime = str(datetime.now())
        with open(self.logPath, 'a') as logFileWriter:
            logFileWriter.write('['+str(logTime)+']'+'['+logLevel+']'+' '+logMsg)
            logFileWriter.write('\n')