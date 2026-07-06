std::string PrettyTitle(const std::string& var, bool applyAbs = false) {
    std::string base;
    if (var == "Eps_emu" || var == "Eps_Emu")      base = "#epsilon_{e#mu}";
    else if (var == "Eps_etau" || var == "Eps_eTau") base = "#epsilon_{e#tau}";
    else if (var == "Delta_emu" || var == "Delta_Emu") base = "#delta_{e#mu}";
    else if (var == "Delta_etau" || var == "Delta_eTau") base = "#delta_{e#tau}";
    else base = var;
    return applyAbs ? ("|" + base + "|") : base;
}

// Decide which variables should be drawn as absolute values.
// Only Eps_emu (handle both common spellings).
bool UseAbs(const std::string& var) {
    return (var == "Eps_emu" || var == "Eps_Emu");
}

 
// Build expression (with or without abs()) for TTree::Draw.
std::string ExprWithAbs(const std::string& var) {
    return UseAbs(var) ? ("abs(" + var + ")") : var;
}

//Colour palette
void SetWhiteBluePalette()
{
    const Int_t NRGBs = 3;
    const Int_t NCont = 255;

    // Define colour stops (from 0 → 1)
    Double_t stops[NRGBs] = { 0.00, 0.50, 1.00 };

    // RGB values
    Double_t red[NRGBs]   = { 1.00, 0.55, 0.00 };
    Double_t green[NRGBs] = { 1.00, 0.75, 0.20 };
    Double_t blue[NRGBs]  = { 1.00, 0.95, 0.60 };

    TColor::CreateGradientColorTable(
        NRGBs, stops, red, green, blue, NCont
    );

    gStyle->SetNumberContours(NCont);
}


void Draw_NSIfitparams(std::string InputFile, std::string OutputFile, bool do2D = false ) {
   // Open the ROOT file
    TFile *file = TFile::Open(InputFile.c_str(),"READ");

    if (!file || file->IsZombie()) {
        std::cerr << "Error opening file!" << std::endl;
        return;
    }

    // Get the TTree
    TTree *tree = (TTree*)file->Get("posteriors");
    if (!tree) {
        std::cerr << "TTree 'posteriors' not found!" << std::endl;
        file->Close();
        return;
    }

    //variables to draw
    std::vector<std::string> variables = {
        "Delta_emu",
        "Eps_emu",
	//"Eps_ee",
        //"Eps_etau",
	//"Eps_mumu",
	//"Eps_mutau",
        //"Delta_emu",
	//"Delta_etau",
	//"Delta_mutau",
	"delta_cp",
	//"sin2th_23"
	//"sin2th_13",
	//"sin2th_12",
	//"delm2_23",
	//"delm2_12"
    };
    
    //auto PrettyTitle = [](const std::string& var) -> std::string {
    // if (var == "Eps_emu")  return "#epsilon_{e#mu}";
    // if (var == "Eps_etau") return "#epsilon_{e#tau}";
    // if (var == "Delta_emu") return "#delta_{e#mu}";
    // if (var == "Delta_etau") return "#delta_{e#tau}";
    // return var; // fallback
    //};
    
    for (const auto& var : variables) {
        // Create unique histogram name
        std::string histName = "h_" + var;
        std::string drawCmd = var + ">>" + histName + "(100)";
	//std::string drawCmd = "abs(Eps_emu)>>" + histName + "(100)";
	
        // Draw the variable into a named histogram
        tree->Draw(drawCmd.c_str(), "", "hist");
        TH1F *h = (TH1F*)gDirectory->Get(histName.c_str());
        if (!h) {
            std::cerr << "Could not get histogram for variable: " << var << std::endl;
            continue;
        }

        // Create a canvas
        TCanvas *c = new TCanvas(Form("c_%s", var.c_str()), Form("%s distribution", var.c_str()), 800, 600);
        gPad->SetLeftMargin(0.15);
        gStyle->SetOptStat(0);

        // Set axis titles
        if (var == "Eps_emu") {
            h->GetXaxis()->SetTitle("#epsilon_{e#mu}");
        } else if (var == "Eps_etau") {
            h->GetXaxis()->SetTitle("#epsilon_{e#tau}");
        } else if (var == "Delta_emu") {
            h->GetXaxis()->SetTitle("#delta_{e#mu}");
	 } else if (var == "Delta_etau") {
            h->GetXaxis()->SetTitle("#delta_{e#tau}");    
        } else {
            h->GetXaxis()->SetTitle(var.c_str());  // fallback
        }

        h->GetYaxis()->SetTitle("Entries");
        h->GetYaxis()->SetTitleOffset(1.4);

        // Draw
        h->Draw("hist");

        // Save to file
	std::string out1D = var + "_" + OutputFile;
        c->SaveAs(out1D.c_str());

        delete c; // Clean up
    }

// === 2D PLOTS ===

    if(do2D){
      
    for (size_t i = 0; i < variables.size(); ++i) {
  //const std::string& xvar = variables[i];
    
      const std::string& xvar = variables[i];
      const bool xAbs = UseAbs(xvar);
      const std::string xExpr = ExprWithAbs(xvar);


    // Determine X range for root to draw things properly

      double xmin = tree->GetMinimum(xvar.c_str());
      double xmax = tree->GetMaximum(xvar.c_str());
      if (!(xmin < xmax)) { xmin = 0.0; xmax = 1.0; }
      if (xAbs) xmin = 0.0;

     
      for (size_t j = i + 1; j < variables.size(); ++j) {
       const std::string& yvar = variables[j];
       const bool yAbs = UseAbs(yvar);
       const std::string yExpr = ExprWithAbs(yvar);
       const char* selection = "";
	    
       double ymin = tree->GetMinimum(yvar.c_str());
       double ymax = tree->GetMaximum(yvar.c_str());
       if (!(ymin < ymax)) { ymin = 0.0; ymax = 1.0; }
       if (yAbs) ymin = 0.0;

            // Name and binning
            //std::string h2name = "h2_"+ Sanitize(yvar) + (yAbs ? "_ABS" : "") +
	    //                    "_vs_" + Sanitize(xvar) + (xAbs ? "_ABS" : "");
	    
	   
	    std::string h2name = "h2_" + yvar + (yAbs ? "_ABS" : "") + "_vs_" + xvar + (xAbs ? "_ABS" : "");
            int nbx = 100, nby = 100;
	    
  // Draw two variables into a TH2F plot
            std::string draw2D = yExpr + ":" + xExpr + ">>" + h2name +
                                 Form("(%d,%g,%g,%d,%g,%g)", nbx, xmin, xmax, nby, ymin, ymax);

            tree->Draw(draw2D.c_str(), selection, "colz");
            TH2F* h2 = (TH2F*)gDirectory->Get(h2name.c_str());
            if (!h2) {
                std::cerr << "Could not get 2D histogram for pair: " << yvar << " vs " << xvar << std::endl;
                continue;
            }

	    
  // Canvas
            TCanvas *c2 = new TCanvas(Form("c2_%s_vs_%s",
                                           yvar.c_str(),
                                           xvar.c_str()),
                                      Form("%s vs %s",
                                           PrettyTitle(yvar, yAbs).c_str(),
                                           PrettyTitle(xvar, xAbs).c_str()),
                                      900, 800);
            gPad->SetLeftMargin(0.15);

            // Axis labels
            h2->GetXaxis()->SetTitle(PrettyTitle(xvar, xAbs).c_str());
            h2->GetYaxis()->SetTitle(PrettyTitle(yvar, yAbs).c_str());
            h2->GetZaxis()->SetTitle("Entries");
            h2->GetYaxis()->SetTitleOffset(1.4);


	    
	    // 1, 2, 3 sigma levels, this probably needs some editing
	    double sigmaLevels[3] = {2.30, 6.18, 11.83};

	    TH2F* hcont = (TH2F*)h2->Clone("hcont");
	    hcont->SetContour(3, sigmaLevels);

	    // Styling
	    hcont->SetLineColor(kBlack);
	    hcont->SetLineWidth(2);


            // Optional: dynamic range
            // gPad->SetLogz();

         // Draw here, also make it smoother
	    SetWhiteBluePalette();
            h2->Draw("colz");

	    // Draw contour lines on top
	    // hcont->Draw("SAME");


	    //correlations, doesn't really work?
        //double corr = h2->GetCorrelationFactor();
        //TLatex lat;
        //lat.SetNDC(true);
        //lat.SetTextSize(0.035);
        //lat.DrawLatex(0.16, 0.93, Form("#rho = %.3f", corr));

	std::string out2d = yvar + xvar +"_2D_" + OutputFile;
	c2->SaveAs(out2d.c_str());

        delete c2;
      }  
    }
    }

    
else {
  std::cout << "Not Making 2D plots";
 }

    file->Close();
}

