import os

inputFolder = ''
outputFolder = ''

def generateVideo(neutralImage,emotionalImage, filename):
  command = 'ffmpeg -y  -loop 1 -t 2 -i ' + neutralImage + ' -loop 1 -t 4 -i ' + emotionalImage + ' -loop 1 -t 2 -i ' + neutralImage + ' -filter_complex "concat=n=3" -shortest -c:v libx264 -pix_fmt yuv420p ' + filename + '.mp4'
  os.system(command)

def simulateDistance(width,height,situationName,filename):
  inputFile = inputFolder + '/' + filename
  outputFile = outputFolder + '/' + situationName + '/' + filename
  os.system('ffmpeg -i ' + inputFile + ' -vf scale='+width+':'+height+' '+ outputFile)

def simulateLighting(intensity,situationName,filename):
  inputFile = inputFolder + '/' + filename
  outputFile = outputFolder + '/' + situationName + '/' + filename
  os.system('ffmpeg -i ' + inputFile + ' -vf eq=brightness='+intensity+' -c:a copy ' + outputFile)