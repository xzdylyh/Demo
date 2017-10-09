from Scripts import gl

if __name__=="__main__":
    gl.init()
    gl.setOverallStatus('userName','msh195')
    print(gl.getOverallStatus('userName'))