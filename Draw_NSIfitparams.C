std::string PrettyTitle(const std::string& var, bool applyAbs = false) {
    std::string base;
    if (var == "Eps_emu" || var == "Eps_Emu")      base = "#varepsilon_{e#mu}";
    else if (var == "Eps_etau" || var == "Eps_eTau") base = "#varepsilon_{e#tau}";
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

bool CompareWeights(const std::pair<double,double>& a, const std::pair<double,double>& b){
          return a.second > b.second;
        }
std::map<double, std::vector<std::pair<double,double>>>
GetCredibleRegions1D(TH1* hist,const std::vector<double>& levels = {0.68, 0.90, 0.99}){
    std::vector<std::pair<double,double>> values; // (x, weight)

    for (int i = 1; i <= hist->GetNbinsX(); ++i) {
        double w = hist->GetBinContent(i);
        if (w > 0.0) {
            values.emplace_back(hist->GetBinCenter(i), w);
        }
    }

    std::map<double, std::vector<std::pair<double,double>>> regions;

    if (values.empty()) {
        for (double lvl : levels) {
            regions[lvl] = {};
        }
    }
    std::sort(values.begin(), values.end(), CompareWeights);
    double total = 0.0;
    for (const auto& v : values) {
        total += v.second;
    }

    double binWidth = hist->GetBinWidth(1);

    for (double lvl : levels) {

        double acc = 0.0;
        std::vector<double> selected;

        for (const auto& [x, w] : values) {
            acc += w;
            selected.push_back(x);

            if (acc / total >= lvl)

                break;
        }

        std::sort(selected.begin(), selected.end());

        std::vector<std::pair<double,double>> intervals;

        double start = selected.front();
        double prev  = selected.front();

        for (size_t i = 1; i < selected.size(); ++i) {

            double x = selected[i];

            if (std::abs(x - prev) > 1.5 * binWidth) {

                intervals.emplace_back(
                    start - 0.5 * binWidth,

                    prev  + 0.5 * binWidth
                );

                start = x;
            }

            prev = x;
        }

        intervals.emplace_back(
            start - 0.5 * binWidth,
            prev  + 0.5 * binWidth
        );

        regions[lvl] = intervals;
        }
    
      return regions;
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
	//"delta_cp",
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
	
	double integral = h->Integral("width");

	if (integral > 0.0)
	  h->Scale(1.0 / integral);

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

        //h->GetYaxis()->SetTitle("Entries");
	h->GetYaxis()->SetTitle("Posterior Density");
        h->GetYaxis()->SetTitleOffset(1.4);

        // Draw
        h->Draw("hist");

	
	// Credible regions
	// Calculate credible regions
auto regions = GetCredibleRegions1D(h);

// Create histograms for the HPD regions
TH1F* h99 = (TH1F*)h->Clone(Form("%s_99", h->GetName()));
TH1F* h90 = (TH1F*)h->Clone(Form("%s_90", h->GetName()));
TH1F* h68 = (TH1F*)h->Clone(Form("%s_68", h->GetName()));

h99->Reset();
h90->Reset();
h68->Reset();

// Fill only bins belonging to each HPD region
for (int ibin = 1; ibin <= h->GetNbinsX(); ++ibin) {

    double x = h->GetBinCenter(ibin);
    double y = h->GetBinContent(ibin);

    for (const auto& interval : regions[0.99]) {
        if (x >= interval.first && x <= interval.second)
            h99->SetBinContent(ibin, y);
    }

    for (const auto& interval : regions[0.90]) {
        if (x >= interval.first && x <= interval.second)
            h90->SetBinContent(ibin, y);
    }

    for (const auto& interval : regions[0.68]) {
        if (x >= interval.first && x <= interval.second)
            h68->SetBinContent(ibin, y);
    }
}

// Colours (68%, 90%, 99%)
std::vector<int> colours = {
    kGreen-6,
    kGreen+2,
    kGreen+4
};

h68->SetFillColor(colours[0]);
h90->SetFillColor(colours[1]);
h99->SetFillColor(colours[2]);

h68->SetLineColor(colours[0]);
h90->SetLineColor(colours[1]);
h99->SetLineColor(colours[2]);

h68->SetFillStyle(1001);
h90->SetFillStyle(1001);
h99->SetFillStyle(1001);

// Draw darkest/largest first
h99->Draw("hist");
h90->Draw("hist same");
h68->Draw("hist same");

// Draw posterior outline on top
h->SetFillStyle(0);
h->SetLineColor(kBlack);
h->SetLineWidth(2);
h->Draw("hist same");

// Legend
TLegend* leg = new TLegend(0.15,0.72,0.40,0.88);
leg->AddEntry(h68,"68% Credible Interval","f");
leg->AddEntry(h90,"90% Credible Interval","f");
leg->AddEntry(h99,"99% Credible Interval","f");
leg->Draw();
	
	// root nonsense needed
	gPad->Update();

	//	double ymax = h->GetMaximum();
	//	std::vector<double> levels = {0.68, 0.90, 0.99};
	//	std::vector<int> colours = {kGreen-6, kGreen+2, kGreen+4};
	

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

