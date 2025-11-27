#include "iostream"

TH2D* mach3_hist_make(TDirectoryFile* NSIFile, TString NSIHistName){
  TH2D* mach3_hist = (TH2D*)NSIFile->Get(NSIHistName);
  //mach3_hist->SetLineColor(kRed);
  mach3_hist->SetNameTitle("LLH Scan", "LLH Scan");
  //mach3_hist->SetFillColorAlpha(kRed, 0.5);
  //mach3_hist->GetXaxis()->SetTitleOffset(1.2);
  mach3_hist->GetZaxis()->SetTitleOffset(3.5);
  return mach3_hist;
}

void Draw_2DLLHScans(){
  gStyle->SetOptStat(0);

  TFile* File = new TFile("inputs/LLHScans/test_t2k_NSI_2DLLHscans_allstartatzero.root");

  //Just draw the NSI parameters

  std::vector<TString> MaCh3Name = {
    "Delta_emu_Eps_emu",
       "Delta_etau_Eps_etau"
  }; 

  int total_systs = MaCh3Name.size();

  TString mach3_sample_prefix="sam";

  TDirectoryFile* MaCh3_Sample = (TDirectoryFile*)File->Get("Sample_2DLLH");

  //create outputfile and canvas
  TString sample_llh = "NSIFitLLH_2D20points_SAMPLE.pdf";
  TCanvas* sample_llh_canvas = new TCanvas("sample_llh_canvas", "sample_llh_canvas", 1200, 800);   
  sample_llh_canvas->Draw();


  // Now need to write these to files
  sample_llh_canvas->Print(sample_llh+"[");
   
  for(int i=0; i<total_systs; i++){
    // Could this be done with a function... yes
    // Would it be easier ... yes
    // oh well

    // Get systematics names
    TString mach3_systematic = MaCh3Name[i];
    TString MaCh3_sample_llh_name = mach3_systematic+"_"+mach3_sample_prefix;
    //std::cout << MaCh3Name[i] << "   " << MaCh3_full_llh_name << std::endl;

    TH2D* sample_llh_stack=  mach3_hist_make(MaCh3_Sample, MaCh3_sample_llh_name);
    sample_llh_canvas->cd();
    sample_llh_stack->SetTitle("Sample LLH "+mach3_systematic+";Systematic Variation;LLH");
    gPad->SetRightMargin(0.3);
    gPad->SetLeftMargin(0.15);
    sample_llh_stack->Draw("COLZ");
    sample_llh_canvas->Print(sample_llh);
    
    sample_llh_canvas->Clear();
    
  }

  // Finish off
  sample_llh_canvas->Print(sample_llh+"]");
}
