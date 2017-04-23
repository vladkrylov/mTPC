#! / bin / bash           
RUNLCIOFILE=$1
RunName=$2

OccCutVal=2 # cut in occupancy in percent of number of events
SpecHighCountOccCutVal=1.0 # cut in occupany for high count hits
AllowedHighCountsPerChipCutVal=4 # chips with more than this value of high count hits will be marked
ThrowCompleteHighCountEvents=1 # 1: complete event with high marked high count chips will be thrown, 0: only data on chip thrown

echo -e "\tCrearing Occupancy to identify dead pixels for $RUNLCIOFILE"
sleep 2s
cp SteeringFiles/FullOccupancyFromLCIO.xml .
sed -i "s%../LCIOFile%$RUNLCIOFILE%g" FullOccupancyFromLCIO.xml
sed -i "s%../CutVal%$OccCutVal%g" FullOccupancyFromLCIO.xml

Marlin FullOccupancyFromLCIO.xml

linesToSkip=6
{
  for ((i=$linesToSkip;i--;))
  do
    read
  done
  read line
  chips=$(echo $line | cut -d':' -f2)
  read line
  columns=$(echo $line | cut -d':' -f2)
  read line
  rows=$(echo $line | cut -d':' -f2)
  read line
  pixel=$(echo $line | cut -d':' -f2)
  read line
  offchips=$(echo $line | cut -d':' -f2)
  echo -e $file
} <MaskedLog

Run=${RUNLCIOFILE##*LCIO_}
# RunName=${Run%.slcio}
# echo "$RunName"

cp SteeringFiles/StatusMap.xml .
sed -i "s%../deadChips%$chips%g" StatusMap.xml
sed -i "s%../deadCols%$columns%g" StatusMap.xml
sed -i "s%../deadRows%$rows%g" StatusMap.xml
sed -i "s%../deadPix%$pixel%g" StatusMap.xml

echo -e "\tCreating status map"
sleep 2s
Marlin StatusMap.xml

# # echo -e "\tCreadting TOT spectrum"
# # sleep 2s
# # cp SteeringFiles/DrawPixelSpecFromLCIO.xml .
# # sed -i "s%../LCIOFile%$RUNLCIOFILE%g" DrawPixelSpecFromLCIO.xml
# # sed -i "s%../StatusMap%`pwd`/StatusMap96.slcio%g" DrawPixelSpecFromLCIO.xml
# # sed -i "s%../PerCentHighCountsPerPixel%$SpecHighCountOccCutVal%g" DrawPixelSpecFromLCIO.xml
# # sed -i "s%../allowedHighCountsPerChip%$AllowedHighCountsPerChipCutVal%g" DrawPixelSpecFromLCIO.xml
# # Marlin DrawPixelSpecFromLCIO.xml
# # 
# # mv PixelSpecLog $RunName/${Run%.slcio}PixelSpecLog
# # mv HighCountEvents $RunName/${Run%.slcio}HighCountEvents
# # 
# # echo -e "\tCreating new StatusMap including HighTOA count pixels"
# # sleep 2s
# # 
# # linesToSkip=12
# # {
# #   for ((i=$linesToSkip;i--;))
# #   do
# #     read
# #   done
# #   read line
# #   HighCountPixel=$(echo $line | cut -d':' -f2)
# #   echo -e $file
# # } <MaskedLog
# # 
# # sed -i "s%$pixel%$pixel$HighCountPixel%g" StatusMap.xml
# # Marlin StatusMap.xml
# # 
# echo -e "\tRemoving data from chips/events with too many high counts in one event and creating cleaned LCIO data"
# sleep 2s

cp SteeringFiles/CreateCleanedData.xml .
sed -i "s%../LCIOFile%$RUNLCIOFILE%g" CreateCleanedData.xml
sed -i "s%../StatusMap%`pwd`/StatusMap96.slcio%g" CreateCleanedData.xml
sed -i "s%../PerCentHighCountsPerPixel%100.0%g" CreateCleanedData.xml
sed -i "s%../allowedHighCountsPerChip%65536%g" CreateCleanedData.xml
sed -i "s%../ThrowCompleteEvent%$ThrowCompleteHighCountEvents%g" CreateCleanedData.xml
sed -i "s%../HighCountEvents%$RunName/${Run%.slcio}HighCountEvents%g" CreateCleanedData.xml

Marlin CreateCleanedData.xml

mkdir $RunName
mv StatusMap96.slcio $RunName/StatusMap.slcio
mv aida_file.root $RunName/Occuppancy.root
mv aida2_file.root $RunName/PixelSpec.root
mv aida3_file.root $RunName/CleanedThrownPixelSpec.root
mv TimePixCleanedThrownData.slcio $RunName/TimePixCleanedThrownData.slcio
mv MaskedLog $RunName/MaskedLog

echo -e "\tCleaning up"
rm PixelSpecLog
rm HighCountEvents
rm StatusMap.xml
rm FullOccupancyFromLCIO.xml
rm DrawPixelSpecFromLCIO.xml
rm CreateCleanedData.xml
rm cdb.log
