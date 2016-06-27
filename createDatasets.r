# Script to 
# +write maldiquant fiedler data to files
# +write MassSpecWavelet data to file
# see https://raw.githubusercontent.com/sgibb/MALDIquant/master/demo/peaks.R 
# source("https://bioconductor.org/biocLite.R")
# biocLite("MassSpecWavelet")
 

dir.create(file.path(getwd(),'data'))

writeFiedlerData <- function() {
  library('MALDIquant')
  dir.create(file.path(getwd(),'data', 'fiedlerData'))  
  data("fiedler2009subset", package="MALDIquant")
  DatDescriptor = c("mass","original","IntensityTransformed","smoothed", "curvatureRemoved")
  
  for(i in seq(from=1, to=16, by=1)){
    s1 <- fiedler2009subset[[i]]
    s2 <- transformIntensity(s1, method="sqrt")
    s3 <- smoothIntensity(s2, method="SavitzkyGolay", halfWindowSize=10)
    s4 <- removeBaseline(s3, method="SNIP", iterations=100)
    
    SpecData <- data.frame(mass(s1),intensity(s1),intensity(s2),intensity(s3),intensity(s4)) # ,row.names = DatDescriptor
    SpecName = paste("data/fiedlerData/Spectrum-",sprintf("%02d", i),".csv",sep="")
    print (paste ("writing spectra to" , SpecName )) 
    write.csv(SpecData, file = SpecName,row.names=FALSE)
    
    p <- detectPeaks(s4, method="MAD", halfWindowSize=20, SNR=2)
    madnoise = rep.int(stats::mad(intensity(s4)), length(intensity(s4)))
    print(paste("madnoise" , madnoise[1]))
    PeakData = data.frame(mass(p), intensity(p))
    PeakName <- paste("data/fiedlerData/Peaks-",sprintf("%02d", i),".csv",sep="")
    print (paste ("writing peaks to " , PeakName )) 
    write.csv(PeakData, file = PeakName,row.names=FALSE)
  }
}


writeExampleMS <- function() {
  dir.create(file.path(getwd(), 'data', 'ExampleMS'))
  library("MassSpecWavelet")
  basePath="/D/myfiles/2016/Mass-Spec/data/ExampleMS/"
  data(exampleMS)
  SNR.Th <- 3
  peakInfo <- peakDetectionCWT(exampleMS, SNR.Th=SNR.Th)
  majorPeakInfo = peakInfo$majorPeakInfo
  peakIndex <- majorPeakInfo$peakIndex
  plotPeak(exampleMS, peakIndex, main=paste('Identified peaks with SNR >', SNR.Th)) 

  outdat <- as.vector(exampleMS)
  SpectrumName = paste("data/ExampleMS/Spectrum.csv",sep="")
  print (paste ("writing spectra to" , SpectrumName ))
  write.csv(exampleMS, file = SpectrumName,row.names=FALSE)
  
  peaks <- as.vector(peakIndex)
  PeakName = paste("data/ExampleMS/Peaks.csv",sep="")
  print (paste ("writing Peak indices to" , PeakName))
  write.csv(peaks, file = PeakName,row.names=FALSE)
}

writeFiedlerData()
writeExampleMS()
