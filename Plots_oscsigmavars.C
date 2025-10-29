#include "TROOT.h"
#include "TFile.h"
#include "TH1.h"
#include "TStyle.h"
#include "TCanvas.h"
#include "TLegend.h"
#include "TGraphAsymmErrors.h"
#include <vector>
#include <iostream>

void Plots_oscsigmavars(std::string filename, int sample_id) {
  //gStyle->SetOptStat(0);

  std::vector<std::string> samplenames = {"FHC1Rmu", "FHC1Re", "FHCnumuCC1pi", "RHC1Rmu", "RHC1Re"};
  std::vector<std::string> samplenames2 = {"FHC 1R#mu", "FHC 1Re", "FHC #nu_{#mu} CC1#pi^{+}", "RHC 1R#mu", "RHC 1Re"};

  float _margin_l     = 0.1;
  float _margin_r     = 0.1;
  float _margin_t     = 0.1;
  float _margin_b     = 0.1;
  float _title_size   = 0.05;
  float _label_size   = 0.04;
  float _title_offset = 1.2;
  float _a_small_num  = 1e-10;


  TFile file(filename.c_str(), "READ");

  if (!file.IsOpen()) {
    std::cerr << "Error: Unable to open file " << filename << std::endl;
    return;
  }
  int i_sample = sample_id;
  if(sample_id<0 || sample_id>5){
    cerr << "I don't know which sample this is" << endl;
    return;
  }
  std::cout << "Plotting sigma variations for sample " << samplenames2[i_sample] << std::endl;

  ifstream csvfile;
    
  //Osc parameters:
  std::vector<std::string> osc_par_name = {
    "Eps_emu",
    "Eps_ee",
    "Eps_etau",
    "Eps_mumu",
    "Eps_mutau",
    "Delta_emu",
    "Delta_etau",
    "Delta_mutau",
    "delta_cp",
    "sin2th_23",
    "sin2th_13",
    "sin2th_12",
    "delm2_23",
    "delm2_12",
    "baseline"
  };

  std::vector<std::string> variations = {"p3", "p1", "n1", "n3"};
  Color_t colors[4] = {kBlue, kCyan, kViolet, kRed};
  int linestyles[4] = {2,3,3,2};

  double hmax = 0.;

  TCanvas* canvas = new TCanvas("canvas", "Error Bands", 800, 600);
  canvas->SetMargin(_margin_l, _margin_r, _margin_t, _margin_b);
  canvas->SetGrid();

  std::string pdfname = "../all_sigma_variation_plots"+samplenames[i_sample]+".pdf";
  canvas->Print((pdfname + "[").c_str());  // Open the multipage PDF
    
  std::string plotname;

  for (int i = 0; i < osc_par_name.size(); ++i) {
    std::string paramname = samplenames[i_sample] + "_2024_osc_par_";
    std::vector<TH1D*> h_sigma;
    for (int i_sig = 0; i_sig < 4; ++i_sig) {
      std::string name_sigmavar = paramname + osc_par_name[i] + "_" + variations[i_sig];
      TH1D *htmp = (TH1D*)file.Get(name_sigmavar.c_str());
      //TH1D *htmp2 = (TH1D*)file.Get(name_sigmavar.c_str());

      std::cout << name_sigmavar << std::endl;

      if (!htmp) {
	std::cerr << "Error: Unable to open sigma variation histogram " << name_sigmavar << std::endl;
	file.Close(); // Close the file before returning
	//delete canvas; // Delete canvas before returning
	return;
      }

      std::cout << "Adding " << name_sigmavar << std::endl;

      htmp->SetLineStyle(1);
      htmp->SetLineWidth(1);
      htmp->SetLineColor(colors[i_sig]);
      h_sigma.push_back(htmp);
         
    }

    std::cout << "I have this many plots to draw in one canvas " << h_sigma.size() << std::endl; 
    
    //std::string htitle = samplenames2[i_sample] + " " + osc_par_name[i] + " #sigma Variation";
    //plot_sigmavar_spectra(canvas, h_sigmavar, plotname, htitle); //Draw spectra

    canvas->cd();
    //gPad->SetTickx();
    //gPad->SetTicky();

    //Drawing all the histogram into one
    h_sigma[0]->SetTitle((samplenames2[i_sample] + " " + osc_par_name[i] + " #sigma Variation").c_str());
    h_sigma[0]->GetYaxis()->SetTitleOffset(_title_offset);
    h_sigma[0]->GetYaxis()->SetTitle("No. of events");
    h_sigma[0]->GetXaxis()->SetTitle("Reconstructed #nu energy [MeV]");
    h_sigma[0]->Draw("HIST");
    
    for(int i_sig=1; i_sig<4; ++i_sig){
      h_sigma[i_sig]->Draw("HIST SAME");
    }

    TLegend* legend = new TLegend(0.7, 0.7, 0.9, 0.9);
    //legend->AddEntry(h_nom, "Nominal spectra", "l");
    legend->AddEntry(h_sigma[3], "-3#sigma variation", "l");
    legend->AddEntry(h_sigma[2], "-1#sigma variation", "l");
    legend->AddEntry(h_sigma[1], "+1#sigma variation", "l");
    legend->AddEntry(h_sigma[0], "+3#sigma variation", "l");

    legend->Draw();
    //c->Print(plotname.c_str());
    //c->SetName(htitle.c_str());
    //c->Clear();
    // delete legend;

    gStyle->SetOptStat(0);  // Turn off stats box
    gStyle->SetLineWidth(2);
    gStyle->SetTitleSize(0.05, "XYZ");
    gStyle->SetLabelSize(0.04, "XYZ");
    gStyle->SetTitleOffset(1.2, "Y");
    gStyle->SetPadTickX(1);
    gStyle->SetPadTickY(1);
    gPad->Update();

    canvas->Update();
    canvas->Print(pdfname.c_str());  // Add current canvas as a new page
    
    //canvas->Print(("../"+paramname + osc_par_name[i] + ".pdf").c_str());
    //file.Close();
    //delete canvas; // Cleanup canvas before returning
  }
  canvas->Print((pdfname + "]").c_str());  // Close the multipage PDF
  file.Close();
  delete canvas; // Cleanup canvas before returning
  
}


