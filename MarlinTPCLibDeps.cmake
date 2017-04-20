# Generated by CMake

if("${CMAKE_MAJOR_VERSION}.${CMAKE_MINOR_VERSION}" GREATER 2.4)
  # Information for CMake 2.6 and above.
  set("MarlinTPC_LIB_DEPENDS" "general;TPCCondData;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/Marlin/v01-05/lib/libMarlin.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/lcio/v02-05/lib/liblcio.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/lcio/v02-05/lib/libsio.so;general;/usr/lib64/libz.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/gear/v01-04-01/lib/libgearsurf.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/gear/v01-04-01/lib/libgear.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/gear/v01-04-01/lib/libgearxml.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/CLHEP/2.1.4.1/lib/libCLHEP.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/ilcutil/v01-02/lib/libstreamlog.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/lccd/v01-03/lib/liblccd.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/lcio/v02-05/lib/liblcio.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/lcio/v02-05/lib/libsio.so;general;/usr/lib64/libz.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/RAIDA/v01-06-02/lib/libRAIDA.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libCore.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libCint.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libRIO.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libNet.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libHist.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libGraf.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libGraf3d.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libGpad.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libTree.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libRint.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libPostscript.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libMatrix.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libPhysics.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libMathCore.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libThread.so;general;/usr/lib64/libdl.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libMinuit2.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/CLHEP/2.1.4.1/lib/libCLHEP.so;general;/usr/lib64/libgsl.so;general;/usr/lib64/libgslcblas.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/KalTest/v01-05-03/lib/libKalTest.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/KalDet/v01-13/lib/libKalDet.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/Marlin/v01-05/lib/libMarlin.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/lcio/v02-05/lib/liblcio.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/lcio/v02-05/lib/libsio.so;general;/usr/lib64/libz.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/gear/v01-04-01/lib/libgearsurf.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/gear/v01-04-01/lib/libgear.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/gear/v01-04-01/lib/libgearxml.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/CLHEP/2.1.4.1/lib/libCLHEP.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/ilcutil/v01-02/lib/libstreamlog.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/MarlinUtil/v01-08-01/lib/libMarlinUtil.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/CED/v01-09-01/lib/libCED.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/CLHEP/2.1.4.1/lib/libCLHEP.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/lccd/v01-03/lib/liblccd.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/lcio/v02-05/lib/liblcio.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/lcio/v02-05/lib/libsio.so;general;/usr/lib64/libz.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/RAIDA/v01-06-02/lib/libRAIDA.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libCore.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libCint.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libRIO.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libNet.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libHist.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libGraf.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libGraf3d.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libGpad.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libTree.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libRint.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libPostscript.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libMatrix.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libPhysics.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libMathCore.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libThread.so;general;/usr/lib64/libdl.so;general;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libMinuit2.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/CLHEP/2.1.4.1/lib/libCLHEP.so;general;/usr/lib64/libgsl.so;general;/usr/lib64/libgslcblas.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/KalTest/v01-05-03/lib/libKalTest.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/KalDet/v01-13/lib/libKalDet.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/pathfinder/v00-06/lib/libPathFinder.so;")
  set("TPCCondData_LIB_DEPENDS" "general;/home/vlad/Program_Files/ilcsoft/v01-17-06/lcio/v02-05/lib/liblcio.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/lcio/v02-05/lib/libsio.so;general;/usr/lib64/libz.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/lccd/v01-03/lib/liblccd.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/lcio/v02-05/lib/liblcio.so;general;/home/vlad/Program_Files/ilcsoft/v01-17-06/lcio/v02-05/lib/libsio.so;general;/usr/lib64/libz.so;")
else()
  # Information for CMake 2.4 and lower.
  set("MarlinTPC_LIB_DEPENDS" "TPCCondData;/home/vlad/Program_Files/ilcsoft/v01-17-06/Marlin/v01-05/lib/libMarlin.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/lcio/v02-05/lib/liblcio.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/lcio/v02-05/lib/libsio.so;/usr/lib64/libz.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/gear/v01-04-01/lib/libgearsurf.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/gear/v01-04-01/lib/libgear.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/gear/v01-04-01/lib/libgearxml.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/CLHEP/2.1.4.1/lib/libCLHEP.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/ilcutil/v01-02/lib/libstreamlog.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/lccd/v01-03/lib/liblccd.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/lcio/v02-05/lib/liblcio.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/lcio/v02-05/lib/libsio.so;/usr/lib64/libz.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/RAIDA/v01-06-02/lib/libRAIDA.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libCore.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libCint.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libRIO.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libNet.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libHist.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libGraf.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libGraf3d.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libGpad.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libTree.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libRint.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libPostscript.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libMatrix.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libPhysics.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libMathCore.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libThread.so;/usr/lib64/libdl.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libMinuit2.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/CLHEP/2.1.4.1/lib/libCLHEP.so;/usr/lib64/libgsl.so;/usr/lib64/libgslcblas.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/KalTest/v01-05-03/lib/libKalTest.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/KalDet/v01-13/lib/libKalDet.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/Marlin/v01-05/lib/libMarlin.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/lcio/v02-05/lib/liblcio.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/lcio/v02-05/lib/libsio.so;/usr/lib64/libz.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/gear/v01-04-01/lib/libgearsurf.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/gear/v01-04-01/lib/libgear.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/gear/v01-04-01/lib/libgearxml.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/CLHEP/2.1.4.1/lib/libCLHEP.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/ilcutil/v01-02/lib/libstreamlog.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/MarlinUtil/v01-08-01/lib/libMarlinUtil.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/CED/v01-09-01/lib/libCED.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/CLHEP/2.1.4.1/lib/libCLHEP.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/lccd/v01-03/lib/liblccd.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/lcio/v02-05/lib/liblcio.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/lcio/v02-05/lib/libsio.so;/usr/lib64/libz.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/RAIDA/v01-06-02/lib/libRAIDA.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libCore.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libCint.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libRIO.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libNet.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libHist.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libGraf.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libGraf3d.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libGpad.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libTree.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libRint.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libPostscript.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libMatrix.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libPhysics.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libMathCore.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libThread.so;/usr/lib64/libdl.so;/home/vlad/Program_Files/root/root-5.34.26/install/lib/root/libMinuit2.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/CLHEP/2.1.4.1/lib/libCLHEP.so;/usr/lib64/libgsl.so;/usr/lib64/libgslcblas.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/KalTest/v01-05-03/lib/libKalTest.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/KalDet/v01-13/lib/libKalDet.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/pathfinder/v00-06/lib/libPathFinder.so;")
  set("TPCCondData_LIB_DEPENDS" "/home/vlad/Program_Files/ilcsoft/v01-17-06/lcio/v02-05/lib/liblcio.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/lcio/v02-05/lib/libsio.so;/usr/lib64/libz.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/lccd/v01-03/lib/liblccd.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/lcio/v02-05/lib/liblcio.so;/home/vlad/Program_Files/ilcsoft/v01-17-06/lcio/v02-05/lib/libsio.so;/usr/lib64/libz.so;")
endif()
