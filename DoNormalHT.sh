#! / bin / bash           
RUNFOLDER=$1
EDrift=$2
z=$3

Freq=40 # in MHz
Shutter=14.038 #13.8(shutter)+0.238(trigger delay)=14.038 #15.188 for run 90!

Run=${RUNFOLDER%%/}
echo "$Run"
RUNLCIOFILE=$Run/TimePixCleanedThrownData.slcio
RUNMAP=$Run/StatusMap.slcio
echo "$RUNLCIOFILE"

if [ ! $# == 3 ]; then
  echo "Usage: $0 RunFolder EDrift_V/cm z_cm"
  exit
fi

if [ $EDrift -eq 130 ]
  then echo "130 V/cm, B=0T"
  VDrift=55.20
  DT=314
  DL=314 
fi
  
if [ $EDrift -eq 230 ] # for runs 090-105
  then echo "230 V/cm, B=0T"
  VDrift=76.375
  DT=323.75
  DL=223.9
fi
ZBinning=`ruby -e $"puts '%.2f' % ($VDrift/$Freq)"` # in mm

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
cp SteeringFiles/NormalHoughTrafo.xml .
sed -i "s%../LCIOFile%$RUNLCIOFILE%g" NormalHoughTrafo.xml
sed -i "s%../StatusMap%$RUNMAP%g" NormalHoughTrafo.xml
sed -i "s%../Vdrift%$VDrift%g" NormalHoughTrafo.xml
sed -i "s%../HTDistanceToTrack%$FourSigmaXYWidth%g" NormalHoughTrafo.xml
sed -i "s%../AssignHitsNSigmaXY%40%g" NormalHoughTrafo.xml
sed -i "s%../AssignHitsNSigmaZ%5%g" NormalHoughTrafo.xml
sed -i "s%../AssignHitsDT%$DT%g" NormalHoughTrafo.xml
sed -i "s%../AssignHitsDL%$DL%g" NormalHoughTrafo.xml
sed -i "s%../AssignHitsLongRes%$ZBinning%g" NormalHoughTrafo.xml
sed -i "s%../Shutter%$Shutter%g" NormalHoughTrafo.xml
sed -i "s%../Freq%$Freq%g" NormalHoughTrafo.xml

Marlin NormalHoughTrafo.xml
# mkdir -p /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/ReconstructionNTracksPhiD0
# mv aida_file.root /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/ReconstructionNTracksPhiD0/${RUNFOLDER%%/}RecoTracks3rotm0_008_1rotm0_008.root
# mv TimePixTracks.slcio TimePixTracksUnCorr.slcio
# 
# echo -e "\t Calculating field distortion offsets for $Run"
# sleep 2s
# cp SteeringFiles/CalculateFieldDist.xml .
# sed -i "s%../LCIOFile%TimePixTracksUnCorr.slcio%g" CalculateFieldDist.xml
# 
# Marlin CalculateFieldDist.xml
# mkdir -p /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/AnalysisNTracksPhiD0
# cp MeansCorrection.txt /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/AnalysisNTracksPhiD0/${RUNFOLDER%%/}MeansCorrection3rotm0_008_1rotm0_008.txt # cp, as it will be needed in NormalHoughTrafoCorr.xml to correct field distortions
# mv MEANvsX.root /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/AnalysisNTracksPhiD0/${RUNFOLDER%%/}MEANvsX3rotm0_008_1rotm0_008.root
# 
# echo -e "\t Doing a HT including field distortions for $RUNLCIOFILE"
# sleep 2s
# cp SteeringFiles/NormalHoughTrafoCorr.xml .
# sed -i "s%../LCIOFile%$RUNLCIOFILE%g" NormalHoughTrafoCorr.xml
# sed -i "s%../StatusMap%$RUNMAP%g" NormalHoughTrafoCorr.xml
# sed -i "s%../Vdrift%$VDrift%g" NormalHoughTrafoCorr.xml
# sed -i "s%../HTDistanceToTrack%$FourSigmaXYWidth%g" NormalHoughTrafoCorr.xml
# sed -i "s%../AssignHitsNSigmaXY%2%g" NormalHoughTrafoCorr.xml
# sed -i "s%../AssignHitsNSigmaZ%5%g" NormalHoughTrafoCorr.xml
# sed -i "s%../AssignHitsDT%$DT%g" NormalHoughTrafoCorr.xml
# sed -i "s%../AssignHitsDL%$DL%g" NormalHoughTrafoCorr.xml
# sed -i "s%../AssignHitsLongRes%$ZBinning%g" NormalHoughTrafoCorr.xml
# sed -i "s%../Shutter%$Shutter%g" NormalHoughTrafoCorr.xml
# sed -i "s%../Freq%$Freq%g" NormalHoughTrafoCorr.xml
# 
# Marlin NormalHoughTrafoCorr.xml
# mv aida_file.root /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/ReconstructionNTracksPhiD0/${RUNFOLDER%%/}RecoTracksFieldDistCorr3rotm0_008_1rotm0_008.root
# 
# 
# echo -e "\t Doing final analysis for corrected $Run"
# sleep 2s
# cp SteeringFiles/ana.xml .
# sed -i "s%../LCIOFile%TimePixTracks.slcio%g" ana.xml
# 
# Marlin ana.xml
# mv aida_file.root /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/AnalysisNTracksPhiD0/${RUNFOLDER%%/}Analysis3rotm0_008_1rotm0_008.root
# mv MeansCorrectionCorrected.txt /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/AnalysisNTracksPhiD0/${RUNFOLDER%%/}MeansCorrectionAfterCorr3rotm0_008_1rotm0_008.txt
# mv MEANvsX.root /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/AnalysisNTracksPhiD0/${RUNFOLDER%%/}MEANvsXAfterCorr3rotm0_008_1rotm0_008.root
# 
# rm ana.xml
# 
# echo -e "\t Doing final analysis for uncorrected $Run"
# sleep 2s
# cp SteeringFiles/ana.xml .
# sed -i "s%../LCIOFile%TimePixTracksUnCorr.slcio%g" ana.xml
# 
# Marlin ana.xml
# mv aida_file.root /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/AnalysisNTracksPhiD0/${RUNFOLDER%%/}AnalysisUncorrected.root
# 
# mv TimePixTracksUnCorr.slcio /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/ReconstructionNTracksPhiD0/${RUNFOLDER%%/}TimePixTracks3rotm0_008_1rotm0_008.slcio
# mv TimePixTracks.slcio /media/tpc/HD3/20150331-0406_testbeam_DESY_Analysis/$Run/ReconstructionNTracksPhiD0/${RUNFOLDER%%/}TimePixTracksFieldDistCorr3rotm0_008_1rotm0_008.slcio
# 
# rm ana.xml
# rm MeansCorrectionCorrected.txt
# rm MEANvsX.root
# 
# rm NormalHoughTrafo.xml
# rm NormalHoughTrafoCorr.xml
# rm CalculateFieldDist.xml
# 
# rm TrackHistos.root
# rm HoughSpace.root
# rm MeansCorrection.txt
# rm HitData.txt
