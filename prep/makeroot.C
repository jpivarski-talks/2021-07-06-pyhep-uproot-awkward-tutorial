void makeroot() {
  auto oldfile = TFile::Open("/home/jpivarski/Downloads/2011MCNtuples.root");
  TTree* oldtree;
  oldfile->GetObject("aod2nanoaod/Events", oldtree);

  oldtree->SetBranchStatus("*", 0);
  oldtree->SetBranchStatus("HLT_IsoMu24", 1);
  oldtree->SetBranchStatus("HLT_IsoMu24_eta2p1", 1);
  oldtree->SetBranchStatus("HLT_IsoMu17_eta2p1_LooseIsoPFTau20", 1);
  oldtree->SetBranchStatus("Muon_pt", 1);
  oldtree->SetBranchStatus("Muon_eta", 1);
  oldtree->SetBranchStatus("Muon_phi", 1);
  oldtree->SetBranchStatus("Muon_mass", 1);
  oldtree->SetBranchStatus("Muon_charge", 1);

  auto newfile = TFile::Open("HiggsZZ4mu.root", "recreate");
  newfile->SetCompressionAlgorithm(ROOT::kZSTD);
  newfile->SetCompressionLevel(9);

  auto newtree = oldtree->CloneTree();

  newfile->Write();
  newfile->Delete("Events;4");
  newfile->Close();
}
