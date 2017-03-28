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
  
#   echo $chips
#   echo $columns
#   echo $rows
  echo $pixel
#   echo $offchips
} <MaskedLog

xargs sed -i "s%../deadPix%$pixel%g" StatusMap.xml

