import gc

from ROOT import *
from subprocess import call
# from memory_profiler import profile

# @profile
def save_hist(fname, hist_base_name, eventID):
        f = TFile(fname)
        # read the hist
        h = f.MyLinearRegressionProcessor.Get("%s%d" % (hist_base_name, eventID))
        save_file = None
        
        # draw and save
        if h:
            h.Draw()
            canvas.Update()
        
            # save to pdf
            save_file = "%s%d.pdf" % (hist_base_name, eventID)
            canvas.SaveAs(save_file)
            
            f.Close()
            del h
        
            return save_file
        else:
            return None

# @profile
def main_func():
    root_file = '/home/vlad/Program_Files/ilcsoft/marlintpc/workspace/aida_file.root'
    hist_base_name = 'XY_full_Evt_'
#     hist_base_name = 'Residuals_'
    save_files = []
    
    canvas = TCanvas( "canvas", "canvas", 50, 50, 1200, 600 )
    for eventID in range(1, 20):
        save_file = save_hist(root_file, hist_base_name, eventID)
        if save_file:
            save_files.append(save_file)
    # raw_input('Press Enter to exit')
    
    # merge results in single file
    print(save_files)
    bash_command = ['pdfunite'] + save_files + ['tracks.pdf']
    call(bash_command)


if __name__ == '__main__':
    main_func()


