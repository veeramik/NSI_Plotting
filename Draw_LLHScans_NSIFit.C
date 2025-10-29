#include "iostream"

TH1D* mach3_hist_make(TDirectoryFile* NSIFile, TString NSIHistName){
  TH1D* mach3_hist = (TH1D*)NSIFile->Get(NSIHistName);
  mach3_hist->SetLineColor(kRed);
  mach3_hist->SetNameTitle("LLH Scan", "LLH Scan");
  mach3_hist->SetFillColorAlpha(kRed, 0.5);
  mach3_hist->GetYaxis()->SetTitleOffset(2);
  return mach3_hist;
}

void Draw_LLHscans_NSIFit(){
  gStyle->SetOptStat(0);

  //TFile* File = new TFile("../LLHScans/test_t2k_NSI_1DLLHscan_11limits.root");
  TFile* File = new TFile("../LLHScans/test_t2k_NSI_LLHscans_allstartatzero.root");

  if (!File->IsOpen()) {
    std::cerr << "Error: Unable to open file " <<  std::endl;
    return;
  }

  //Just draw the NSI parameters

  std::vector<TString> MaCh3Name = {
    "Eps_emu",
    "Eps_mumu",
    "Eps_etau",
    "Eps_ee",
    "Eps_tautau",
    "Delta_emu",
    "Delta_etau",
    "Delta_mutau",
    "DownCoup",
    "ElecCoup",
    "UpCoup",
    "delta_cp"
  }; 

  int total_systs = MaCh3Name.size();

  TString mach3_full_prefix="full";
  TString mach3_sample_prefix="sam";
  TString mach3_penalty_prefix="xs";

  // Okay now we can

  TDirectoryFile* MaCh3_Full = (TDirectoryFile*)File->Get("Total_LLH");
  TDirectoryFile* MaCh3_Sample = (TDirectoryFile*)File->Get("Sample_LLH");
  TDirectoryFile* MaCh3_Penalty = (TDirectoryFile*)File->Get("xsec_LLH");

  // okay we now want 3 output files
  TString full_llh = "NSIFitLLH_1000points_OA24_FULL_newlimit_10limitsforeps_allstartatzero.pdf";
  TString sample_llh = "NSIFitLLH_1000points_OA24_SAMPLE_newlimits_10limitsforeps_allstartatzero.pdf";
  TString penalty_llh = "NSIFitLLH_1000points_OA24_PENALTY_newlimits_10limitsforeps_allstartatzero.pdf";

  // Should make 3 TCanvases as well
  TCanvas* full_llh_canvas = new TCanvas("full_llh_canvas", "full_llh_canvas", 1000, 800);
  TCanvas* sample_llh_canvas = new TCanvas("sample_llh_canvas", "sample_llh_canvas", 1000, 800);
  TCanvas* penalty_llh_canvas = new TCanvas("penalty_llh_canvas", "penalty_llh_canvas", 1000, 800);
  full_llh_canvas->Draw();
  sample_llh_canvas->Draw();
  penalty_llh_canvas->Draw();

  // Now need to write these to files
  full_llh_canvas->Print(full_llh+"[");
  sample_llh_canvas->Print(sample_llh+"[");
  penalty_llh_canvas->Print(penalty_llh+"[");

  for(int i=0; i<total_systs; i++){
    // Could this be done with a function... yes
    // Would it be easier ... yes
    // oh well

    // Get systematics names
    TString mach3_systematic = MaCh3Name[i];

    TString MaCh3_full_llh_name = mach3_systematic+"_"+mach3_full_prefix;        
    TString MaCh3_sample_llh_name = mach3_systematic+"_"+mach3_sample_prefix;
    TString MaCh3_penalty_llh_name = mach3_systematic+"_"+mach3_penalty_prefix;

    std::cout << MaCh3Name[i] << "   " << MaCh3_full_llh_name << std::endl;

    //TH1D* full_llh_stack = mach3_hist_make(MaCh3_Full, MaCh3_full_llh_name);
    //full_llh_canvas->cd();
    //full_llh_stack->SetTitle("Full LLH "+mach3_systematic+";Systematic Variation;LLH");
    //full_llh_stack->Draw();
    //full_llh_canvas->Print(full_llh);
    
    TH1D* sample_llh_stack=  mach3_hist_make(MaCh3_Sample, MaCh3_sample_llh_name);
    sample_llh_canvas->cd();
    sample_llh_stack->SetTitle("Sample LLH "+mach3_systematic+";Systematic Variation;LLH");
    sample_llh_stack->Draw();
    sample_llh_canvas->Print(sample_llh);
    
    //TH1D* penalty_llh_stack = mach3_hist_make(MaCh3_Penalty, MaCh3_penalty_llh_name);
    //penalty_llh_canvas->cd();
    //penalty_llh_stack->SetTitle("Penalty LLH "+mach3_systematic+";Systematic Variation;LLH");
    //penalty_llh_stack->Draw("nostack");

    //std::cout << "HERE" << std::endl;

    //full_llh_canvas->Clear();
    sample_llh_canvas->Clear();
    //penalty_llh_canvas->Clear();

    
  }

  // Finish off
  //full_llh_canvas->Print(full_llh+"]");
  sample_llh_canvas->Print(sample_llh+"]");
  //penalty_llh_canvas->Print(penalty_llh+"]");
}
