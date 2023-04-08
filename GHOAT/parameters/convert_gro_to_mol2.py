import parmed as pmd

host_dict = {"OAH":"oa","OAMe":"oam"}
host_oldresname_dict = {"OAH":"CLP","OAMe":"OCB"}
host_newresname_dict = {"OAH":"OCT","OAMe":"OAM"}
coords = "SYSTEM.crd"
topol = "SYSTEM.top"
filetoconvert = "b.gro"
#import nglview as nv
from pathlib import Path
cwd = Path().absolute()
print(cwd)
import os
CHARMMPRM = Path("CHARMMPRM")
parpath = cwd/CHARMMPRM
(cwd/CHARMMPRM).mkdir(parents=True, exist_ok=True)
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      #print(name)
      #print(os.path.join(root, name))
      #print(os.path.dirname(root))
      #print(os.path.basename(root))
      #print(os.path.basename(name))
      if("bound" in root and name == coords):
            print(os.path.join(root, name))
            print(root)
            print(((root).split("_")[1]).split("/"))
            components=(((root).split("_")[1]).split("/"))

            #filepath = Path("host-"+host_dict[components[0]]+components[1].replace("G", "-lda-guest-")+".pdb")
            #print(cwd/filepath)
            amber = pmd.load_file(os.path.join(root, topol),os.path.join(root, coords))
            amber.residues[0], amber.residues[1] = amber.residues[1], amber.residues[0]
            #amber= amber["(:{})".format(host_oldresname_dict[components[0]])] + amber["(!:{})".format(host_oldresname_dict[components[0]])]           
            for res in amber.residues:
                  if res.name == host_oldresname_dict[components[0]]:
                        res.name = host_newresname_dict[components[0]]
            guest = amber["(:MOL)"]
            host = amber["(:{})".format(host_newresname_dict[components[0]])]
            hostfilepath = Path("host-"+host_dict[components[0]]+".mol2")
            guestfilepath = Path(components[1].replace("G", "lda-guest-")+".mol2")
            host.save(str(hostfilepath), overwrite=True)
            guest.save(str(guestfilepath), overwrite=True)
            filepath_rtf = Path("host-"+host_dict[components[0]]+components[1].replace("G", "-lda-guest-")+".rtf")
            filepath_prm = Path("host-"+host_dict[components[0]]+components[1].replace("G", "-lda-guest-")+".prm")
            pmd.charmm.CharmmParameterSet.from_structure(amber).write(top=str(parpath/filepath_rtf), par=str(parpath/filepath_prm))
   #for name in dirs:
   #   print(os.path.join(root, name))
#amber = pmd.load_file('/home/greg/Desktop/GHOAT.py/GHOAT/equil/guest-5/full.prmtop', '/home/greg/Desktop/GHOAT.py/GHOAT/equil/guest-5/full.inpcrd')
#amber.save('../output/CHARMM/restraints/host_restraints.pdb', overwrite=True)
