import awkward as ak
import uproot

oldfile = uproot.open("/home/jpivarski/Downloads/2011MCNtuples.root")
oldtree = oldfile["aod2nanoaod/Events"]

HLT_IsoMu24 = oldtree["HLT_IsoMu24"].array()
HLT_IsoMu24_eta2p1 = oldtree["HLT_IsoMu24_eta2p1"].array()
HLT_IsoMu17_eta2p1_LooseIsoPFTau20 = oldtree["HLT_IsoMu17_eta2p1_LooseIsoPFTau20"].array()
Muon_pt = oldtree["Muon_pt"].array()
Muon_eta = oldtree["Muon_eta"].array()
Muon_phi = oldtree["Muon_phi"].array()
Muon_mass = oldtree["Muon_mass"].array()
Muon_charge = oldtree["Muon_charge"].array()

hlt = ak.zip({"IsoMu24": HLT_IsoMu24, "IsoMu24_eta2p1": HLT_IsoMu24_eta2p1, "IsoMu17_eta2p1_LooseIsoPFTau20": HLT_IsoMu17_eta2p1_LooseIsoPFTau20})
muons = ak.zip({"pt": Muon_pt, "eta": Muon_eta, "phi": Muon_phi, "mass": Muon_mass, "charge": Muon_charge})
array = ak.Array({"hlt": hlt, "muons": muons})

ak.to_parquet(array, "HiggsZZ4mu.parquet", list_to32=True, use_dictionary=False, compression="ZSTD", compression_level=9, use_byte_stream_split=["muons.pt", "muons.eta", "muons.phi", "muons.mass"])
