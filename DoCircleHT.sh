#! / bin / bash           
RUNFOLDER=$1
EDrift=$2
z=$3

Freq=80 # in MHz
Shutter=14.038 #13.8(shutter)+0.238(trigger delay)=14.038 #15.188 for run 90!

Run=${RUNFOLDER%%/}
echo "$Run"
RUNLCIOFILE=$Run/${RUNFOLDER%%/}TimePixCleanedThrownData.slcio
RUNMAP=$Run/${RUNFOLDER%%/}StatusMap.slcio
echo "$RUNLCIOFILE"

if [ ! $# == 3 ]; then
  echo "Usage: $0 RunFolder EDrift_V/cm z_cm"
  exit
fi

if [ $EDrift -eq 130 ]
  then echo "130 V/cm, B=0T"
  VDrift=55.20
  DT=75
  DL=330 
fi
  
if [ $EDrift -eq 230 ] # Runs 178-190
  then echo "230 V/cm, B=0T"
  VDrift=75.71
  DT=95.89
  DL=224.9
  DL2=424 # for broad track fit
fi
ZBinning=`ruby -e $"puts '%.2f' % ($VDrift/$Freq)"` # in mm
ZBinning2=`ruby -e $"puts '%.2f' % (20*$VDrift/$Freq)"` # in mm

# !calc result is a text!
SigmaXYWidth=`ruby -e $"puts '%.2f' % Math.sqrt($DT*$DT*$z/1000000)"`
TwoSigmaXYWidth=`ruby -e $"puts '%.2f' % Math.sqrt(4*$DT*$DT*$z/1000000)"`
ThreeSigmaXYWidth=`ruby -e $"puts '%.2f' % Math.sqrt(9*$DT*$DT*$z/1000000)"`
FourSigmaXYWidth=`ruby -e $"puts '%.2f' % Math.sqrt(16*$DT*$DT*$z/1000000)"`

SigmaZWidth=`ruby -e $"puts '%.2f' % Math.sqrt($DL*$DL*$z/1000000)"`
TwoSigmaZWidth=`ruby -e $"puts '%.2f' % Math.sqrt(4*$DL*$DL*$z/1000000)"`
ThreeSigmaZWidth=`ruby -e $"puts '%.2f' % Math.sqrt(9*$DL*$DL*$z/1000000)"`

echo -e "\t Doing a HT for $RUNLCIOFILE"
sleep 2s
cp SteeringFiles/AHT.xml .
sed -i "s%../LCIOFile%$RUNLCIOFILE%g" AHT.xml
sed -i "s%../StatusMap%$RUNMAP%g" AHT.xml
sed -i "s%../Vdrift%$VDrift%g" AHT.xml
sed -i "s%../HTDistanceToTrack%$FourSigmaXYWidth%g" AHT.xml
sed -i "s%../AssignHitsNSigmaXY%4%g" AHT.xml
sed -i "s%../AssignHitsNSigmaZ%6%g" AHT.xml
sed -i "s%../AssignHitsDT%$DT%g" AHT.xml
sed -i "s%../AssignHitsDL%$DL%g" AHT.xml
sed -i "s%../AssignHitsDL2%$DL2%g" AHTCorr.xml
sed -i "s%../AssignHitsLongRes%$ZBinning%g" AHT.xml
sed -i "s%../Shutter%$Shutter%g" AHT.xml
sed -i "s%../Freq%$Freq%g" AHT.xml

Marlin AHT.xml
mkdir -p /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/Reconstruction
mv aida_file.root /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/Reconstruction/${RUNFOLDER%%/}RecoTracksCirlce3rotm0_008_1rotm0_008.root
mv TimePixTracks.slcio TimePixTracksUnCorr.slcio

echo -e "\t Calculating field distortion offsets for $RUNLCIOFILE"
sleep 2s
cp SteeringFiles/CalculateFieldDist.xml .
sed -i "s%../LCIOFile%TimePixTracksUnCorr.slcio%g" CalculateFieldDist.xml

Marlin CalculateFieldDist.xml
mkdir -p /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/Analysis
cp MeansCorrection.txt /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/Analysis/${RUNFOLDER%%/}MeansCorrectionCircle3rotm0_008_1rotm0_008.txt
cp MeansCorrectionZ.txt /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/Analysis/${RUNFOLDER%%/}MeansCorrectionZCircle3rotm0_008_1rotm0_008.txt # cp, as it will be needed in NormalHoughTrafoCorr.xml to correct field distortions
mv MEANvsX.root /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/Analysis/${RUNFOLDER%%/}MEANvsXCirlce3rotm0_008_1rotm0_008.root
mv MEANvsZ.root /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/Analysis/${RUNFOLDER%%/}MEANvsZCirlce3rotm0_008_1rotm0_008.root

echo -e "\t Doing a HT including field distortions for $RUNLCIOFILE"
sleep 2s
cp SteeringFiles/AHTCorr.xml .
sed -i "s%../LCIOFile%$RUNLCIOFILE%g" AHTCorr.xml
sed -i "s%../StatusMap%$RUNMAP%g" AHTCorr.xml
sed -i "s%../Vdrift%$VDrift%g" AHTCorr.xml
sed -i "s%../HTDistanceToTrack%$FourSigmaXYWidth%g" AHTCorr.xml
sed -i "s%../AssignHitsNSigmaXY%4%g" AHTCorr.xml
sed -i "s%../AssignHitsNSigmaZ%6%g" AHTCorr.xml
sed -i "s%../AssignHitsDT%$DT%g" AHTCorr.xml
sed -i "s%../AssignHitsDL%$DL%g" AHTCorr.xml
sed -i "s%../AssignHitsDL2%$DL2%g" AHTCorr.xml
sed -i "s%../AssignHitsLongRes%$ZBinning%g" AHTCorr.xml
sed -i "s%../Shutter%$Shutter%g" AHTCorr.xml
sed -i "s%../Freq%$Freq%g" AHTCorr.xml

Marlin AHTCorr.xml
mv aida_file.root /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/Reconstruction/${RUNFOLDER%%/}RecoTracksFieldDistCorrCircle3rotm0_008_1rotm0_008.root
 
echo -e "\t Doing final analysis for corrected $Run"
sleep 2s
cp SteeringFiles/ana1T.xml .
sed -i "s%../LCIOFile%TimePixTracks.slcio%g" ana1T.xml

Marlin ana1T.xml
mv aida_file.root /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/Analysis/${RUNFOLDER%%/}AnalysisCorrCircle3rotm0_008_1rotm0_008.root
mv MeansCorrectionCorrectedZ.txt /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/Analysis/${RUNFOLDER%%/}MeansCorrectionZAfterCorrCircle3rotm0_008_1rotm0_008.txt
mv MeansCorrectionCorrected.txt /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/Analysis/${RUNFOLDER%%/}MeansCorrectionAfterCorrCircle3rotm0_008_1rotm0_008.txt
mv MEANvsX.root /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/Analysis/${RUNFOLDER%%/}MEANvsXAfterCorrCircle3rotm0_008_1rotm0_008.root
mv MEANvsZ.root /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/Analysis/${RUNFOLDER%%/}MEANvsZAfterCorrCircle3rotm0_008_1rotm0_008.root

rm ana1T.xml

echo -e "\t Doing final analysis for uncorrected $Run"
sleep 2s
cp SteeringFiles/ana1T.xml .
sed -i "s%../LCIOFile%TimePixTracksUnCorr.slcio%g" ana1T.xml

Marlin ana1T.xml
mv aida_file.root /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/Analysis/${RUNFOLDER%%/}AnalysisUncorrCircle3rotm0_008_1rotm0_008.root

mv TimePixTracksUnCorr.slcio /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/Reconstruction/${RUNFOLDER%%/}TimePixTracksCircle3rotm0_008_1rotm0_008.slcio
mv TimePixTracks.slcio /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/Reconstruction/${RUNFOLDER%%/}TimePixTracksFieldDistCorrCircle3rotm0_008_1rotm0_008.slcio

rm ana1T.xml
rm MeansCorrectionCorrectedZ.txt
rm MeansCorrectionCorrected.txt
rm MEANvsX.root
rm MEANvsZ.root

rm AHT.xml
rm AHTCorr.xml
rm CalculateFieldDist.xml

rm TrackHistos.root
rm HoughSpace.root
rm MeansCorrectionZ.txt
rm MeansCorrection.txt
rm HitData.txt
