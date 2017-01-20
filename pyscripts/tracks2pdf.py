import gc

from ROOT import *
from subprocess import call
from memory_profiler import profile

# @profile
def save_hist(fname, hist_base_name, eventID):
        f = TFile(fname)
        # read the hist
        h = f.MyLinearRegressionProcessor.Get("%s%d" % (hist_base_name, eventID))
        # draw and save
        h.Draw()
        canvas.Update()
        
        # save to pdf
        save_file = "%s%d.pdf" % (hist_base_name, eventID)
        canvas.SaveAs(save_file)
        
        f.Close()
        del h
        
        return save_file

# @profile
def main_func():
    fname = '/home/vlad/Program_Files/ilcsoft/marlintpc/workspace/Run_000102_150402_12-08-06/Results/Run_000102_150402_12-08-06RecoTracks3rotm0_008_1rotm0_008.root'
    hist_base_name = 'XY_full_Evt_'
    save_files = []
    
    canvas = TCanvas( "canvas", "canvas", 50, 50, 1200, 600 )
    for eventID in range(100):
        save_file = save_hist(fname, hist_base_name, eventID)
        save_files.append(save_file)
    # raw_input('Press Enter to exit')
    
    # merge results in single file
    bash_command = ['pdfunite'] + save_files + ['tracks.pdf']
    call(bash_command)


if __name__ == '__main__':
    main_func()

