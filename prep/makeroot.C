void makeroot() {
  auto oldfile = TFile::Open("/home/jpivarski/Downloads/2011MCNtuples.root");
  TTree* oldtree;
  oldfile->GetObject("aod2nanoaod/Events", oldtree);

  oldtree->SetBranchStatus("*", 0);
  oldtree->SetBranchStatus("run", 1);
  oldtree->SetBranchStatus("luminosityBlock", 1);
  oldtree->SetBranchStatus("event", 1);
  oldtree->SetBranchStatus("MET_pt", 1);
  oldtree->SetBranchStatus("MET_phi", 1);
  oldtree->SetBranchStatus("Muon_pt", 1);
  oldtree->SetBranchStatus("Muon_eta", 1);
  oldtree->SetBranchStatus("Muon_phi", 1);
  oldtree->SetBranchStatus("Muon_mass", 1);
  oldtree->SetBranchStatus("Muon_charge", 1);
  oldtree->SetBranchStatus("GenPart_pt", 1);
  oldtree->SetBranchStatus("GenPart_eta", 1);
  oldtree->SetBranchStatus("GenPart_phi", 1);
  oldtree->SetBranchStatus("GenPart_pdgId", 1);

  auto newfile = TFile::Open("HiggsZZ4mu.root", "recreate");
  newfile->SetCompressionAlgorithm(ROOT::kZSTD);
  newfile->SetCompressionLevel(9);

  auto newtree = oldtree->CloneTree();

  newfile->Write();
  newfile->Delete("Events;4");
  newfile->Close();
}
