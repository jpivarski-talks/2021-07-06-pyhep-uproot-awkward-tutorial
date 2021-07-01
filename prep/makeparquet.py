import awkward as ak
import uproot

oldfile = uproot.open("/home/jpivarski/Downloads/2011MCNtuples.root")
oldtree = oldfile["aod2nanoaod/Events"]

run = oldtree["run"].array()
luminosityBlock = oldtree["luminosityBlock"].array()
event = oldtree["event"].array()
MET_pt = oldtree["MET_pt"].array()
MET_phi = oldtree["MET_phi"].array()
Muon_pt = oldtree["Muon_pt"].array()
Muon_eta = oldtree["Muon_eta"].array()
Muon_phi = oldtree["Muon_phi"].array()
Muon_mass = oldtree["Muon_mass"].array()
Muon_charge = oldtree["Muon_charge"].array()
GenPart_pt = oldtree["GenPart_pt"].array()
GenPart_eta = oldtree["GenPart_eta"].array()
GenPart_phi = oldtree["GenPart_phi"].array()
GenPart_pdgId = oldtree["GenPart_pdgId"].array()

met = ak.Array({"pt": MET_pt, "phi": MET_phi})
muons = ak.zip(
    {
        "pt": Muon_pt,
        "eta": Muon_eta,
        "phi": Muon_phi,
        "mass": Muon_mass,
        "charge": Muon_charge,
    }
)
gen = ak.zip(
    {
        "pt": GenPart_pt,
        "eta": GenPart_eta,
        "phi": GenPart_phi,
        "pdgId": GenPart_pdgId,
    }
)
array = ak.Array({
    "run": run,
    "luminosityBlock": luminosityBlock,
    "event": event,
    "MET": met,
    "muons": muons,
    "gen": gen,
})

ak.to_parquet(
    array,
    "HiggsZZ4mu.parquet",
    list_to32=True,
    use_dictionary=False,
    compression="ZSTD",
    compression_level=9,
    use_byte_stream_split=[
        "MET.pt",
        "MET.phi",
        "muons.pt",
        "muons.eta",
        "muons.phi",
        "muons.mass",
        "gen.pt",
        "gen.eta",
        "gen.phi",
    ],
)
