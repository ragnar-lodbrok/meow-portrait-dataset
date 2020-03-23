import os

def main():
    
    datasetDir = 'dataset'
    srcImg = 'src.png'
    dstImg = 'dst.png'
    sep = os.path.sep

    firstLine = True

    trainFile = open("train.txt","w") 

    for dir1 in os.listdir('./'+datasetDir):
        
        srcPath = datasetDir + sep + dir1 + sep + srcImg
        dstPath = datasetDir + sep + dir1 + sep + dstImg
        
        try:
            f1 = open('./' + srcPath)
            f2 = open('./' + dstPath)
        except IOError:
            print('FAIL: ' +  srcPath + ' ' + dstPath)
            continue
        finally:
            f1.close()
            f2.close()
                
        if (firstLine == False):                    
            trainFile.write('\n')
                    
        firstLine = False
                
        trainFile.write(srcPath + ' ' + dstPath)
                   
            
    trainFile.close();

if __name__ == "__main__":
    main()
